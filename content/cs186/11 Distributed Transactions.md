# Distributed Transactions

If 

## 2 Phase Commit

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

All results must be unanimous in order to commit. Any one node that can’t commit should cause the entire transaction to abort.

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

If a participant doesn’t recover, coordinator respawns new participant using log records; destroy old participant

If the coordinator doesn’t recover, 2PC doesn’t work (use 3PC, etc)

### Distributed Deadlock

Suppose multiple machines have running transactions, and each machine has its own waits-for graph.

To evaluate deadlock, union all of the waits-for graphs and check for cycles.

## 2PC Timing (Problem solving strategies)

The best case time for a transaction to complete using 2PC:

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

Time to abort:

Phase 1:

- Coordinator sends prepare message
- Committing participants flush prepare, aborting participants add abort record
    - max (times for aborts to send, times for commits to send + flush time)

Phase 2:

- Coordinator sends abort message
- Under abort optimization, no ACK is required.