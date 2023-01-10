---
title: "Distributed Transactions"
weight: 110
---

## Introduction
In some situations (like in datacenters), the computation needed for transactions gets to be too great for a single computer to handle.

One solution for this is to build *wide*- connect a whole bunch of computers together, and have them all work on the same thing! However, this comes with its challenges.

One such challenge is how we can still preserve ACID properties of transactions when each computer is working independently. What happens if one computer crashes?

## Relevant Materials
 - [Note 16](https://notes.bencuan.me/cs186/coursenotes/n16-DistXact.pdf)
 - [Discussion 12](https://docs.google.com/presentation/d/1G1A93sgcPWIDSZklHyqya62VFqMbsFnSnKap9vi8AG0/edit)


## Two Phase Commit
Two Phase Commit (which has no relation to Two Phase Locking, except by name) is a method of establishing consensus between distributed nodes running the same transaction. The main idea is to guarantee that either all nodes complete successfully, or none will commit.

![Untitled](Distributed%20Transactions/Untitled.png)

**Phase 1: voting**
- Coordinator asks participants to vote by sending a PREPARE message to all participants.
- Participants send VOTE YES or VOTE NO to coordinator.
- Participants log and flush either a PREPARE or ABORT record to the log, keeping track of the coordinator ID.
- After the coordinator receives a message from all participants, the coordinator logs and flushes either a COMMIT or ABORT record to log

**Phase 2: results**
- Coordinator tells participants to COMMIT or ABORT.
- Participants log and flush COMMIT or ABORT to log.
- Participants send ACK to coordinator.
- Coordinator logs (but does not need to flush) an END record to the log, to remove it from the transaction table.

All results must be unanimous in order to COMMIT. Any one node that can’t commit should cause the entire transaction to ABORT.

### Recovery
- If we have a COMMIT or ABORT log record, we know what to do. (The coordinator should send commit or abort messages periodically until all ACKs are received.)
- If we have a PREPARE log record, but no commit/abort, then we’re at a participant node that should send a message to the coordinator inquiring about the status of the transaction.
- If we have no prepare, commit, or abort, then something crashed.
    - If at a participant node, abort the transaction (did not send YES)
    - If at a coordinator node, respond to all future votes with ABORT.
- It is never possible to COMMIT if either the coordinator or participants have written an ABORT.
- It is never possible to ABORT if any one participant has written COMMIT.

### Optimization

**Presumed abort:** a transaction should abort if we have no log records locally.

When a transaction aborts:
- Coordinator cleans up locally- remove transaction from table if it doesn’t have ACKs
- If participant receives ABORT, do not send ACKs
- If transaction not in coordinator’s transaction table when participant inquires, ABORT
- Don’t store participant IDs in abort records
- Abort records do not need to be flushed

### Blocking

If a node crashes during the voting (first) phase, any participant that voted yes keeps locks and waits for commit or abort

If a participant doesn’t recover, coordinator respawns new participant using log records; destroy old participant.

If the coordinator doesn’t recover, 2PC doesn’t work (use 3PC, etc).

### Distributed Deadlock

Suppose multiple machines have running transactions, and each machine has its own waits-for graph.

To evaluate deadlock, union all of the waits-for graphs and check for cycles.

## 2PC Timing (Problem solving strategies)

**Problem: Find the best case time for a transaction to complete using 2PC:**

Phase 1:
- Coordinator sends a prepare message (coordinator send time)
- Participants flush to log (flush time)
- Participants send Yes message (max of participant send times)
- Coordinator flushes a commit log (flush time)

Phase 2:
- Coordinator sends commit message (coord send time)
- Participants flush commit record (flush time)
- Participants send ACK (max of participant send times)
- Coordinator flushes END record (flush time)

**Problem: Find the minimum time it takes for 2PC to abort.**

Phase 1:
- Coordinator sends prepare message
- Committing participants flush prepare, aborting participants add abort record
    - max (times for aborts to send, times for commits to send + flush time)

Phase 2:
- Coordinator sends abort message
- Under abort optimization, no ACK is required.