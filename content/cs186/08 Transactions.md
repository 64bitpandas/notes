## Introduction

Transactions are collections of operations that can be treated like a single unit.

## Relevant Materials


## ACID and Concurrency

We want all transactions to obey ACID:

- **Atomicity:** either all operations happen, or none of them
- **Consistency:** database remains in a consistent state with its constraints
- **Isolation:** it should appear as if we only run 1 transaction at a time (even if they’re actually run concurrently)
- **Durability:** once a transaction commits, it persists

Transaction operations:

- Commit: indicates a successful transaction, changes should be saved
- Abort: indicates an unsuccessful transaction, changes should be reverted

Concurrent transitions are better:

- Increase throughput (processor and disk utilization) → more transactions are completed per second
- Decrease latency → transactions complete more quickly

## Serializability

- A **schedule** is the order in which we execute operations in a set of transactions.
- A **serial schedule** is a schedule in which every transaction completes without interleaving (finish all parts of one transaction from start to finish before moving to the next)
- **Two schedules are equivalent if:**
    - They involve the same transactions
    - Each transaction’s operations are completed in the same order
    - The final state after all transactions is the same
- Isolation = serializable = schedule is equivalent to a serial schedule
- In order to check serializability, we will check if they are **conflict serializable:**
    - Two operations are in a schedule conflict if
        - at least one operation is a write
        - the operations are on different transactions
        - the operations work on the same resource
    - Two operations are conflict equivalent if every conflict is ordered in the same way.
    - A schedule is conflict serializable if it is conflict equivalent to a serial schedule.
- **View serializability** refers to conflict serializability in which blind writes (intermediate writes that are overwritten without a read in between) are ignored. Checking view serializability is an NP complete problem.

![Untitled](Transactions/Untitled.png)

## Dependency Graphs

- Each node = one transaction
- If an operation in transaction $T_i$ conflicts with an operation in $T_j$, and the operation in $T_i$ comes first, then create an edge between the $T_i$ and $T_j$ nodes.
- To find equivalent schedules, run topological sort on all involved graphs. **All conflict serializable schedules have an acyclic dependency graph.** So if a graph has a cycle, it is not conflict serializable.

![Untitled](Transactions/Untitled%201.png)

# Locking

A transaction may lock a resource in two ways:

- S lock (shared): allows a transaction to read a resource
    - Multiple transactions can hold S lock on the same resource at the same time
- X lock (exclusive): allows a transaction write a resource
    - No other transaction can have any type of lock on the same resource as a transaction with an X lock on it
    
    ![Untitled](Transactions/Untitled%202.png)
    

## Deadlock

Deadlock occurs when there is a cycle of transactions all waiting for each other to release their locks.

### Deadlock Avoidance

Deadlock avoidance: catching deadlocks before they occur

- Wait-die: if $T_i$ wants a lock but $T_j$ holds a conflicting lock:
    - If $T_i$ higher priority, wait for $T_j$ to release
    - If $T_i$ lower priority, abort (die)
- Wound-wait:
    - If $T_i$ is higher priority, $T_j$ aborts
    - If $T_i$ is lower priority, it waits for $T_j$ to finish
- If no explicitly defined priority, we can assign priority by age (current time - start time)

### Deadlock Detection

To perform deadlock detection, we can draw a **waits-for graph**:

- One note per transaction
- If $T_i$ holds a lock that conflicts with the lock that $T_j$ wants (i.e. $T_j$ waits for $T_i$), add an edge from $T_j$ to $T_i$
- Deadlock occurs if there is a cycle in the graph

## Two Phase Locking (2PL)

2PL is one method of enforcing conflict serializability.

There are two phases:

1. From start until a lock is released, the transaction is only acquiring locks (acquiring step)
2. From after a lock is released to the end of the transaction, the transaction is only releasing locks (release phase)

Transactions cannot acquire any lock after it has released a lock.

Strict 2PL only allows releasing of locks at the end of the transaction. This avoids cascading aborts (when unrelated transactions are aborted due to lock release schedule).

## Multigranularity Locking

- Tuple-level locking: one lock per tuple (high locking overhead due to a scan requiring many locks)
- Table-level locking: one lock per table (low concurrency since any update locks the entire table)
- **Multigranularity Locking:** based on operation, allow for different types of locks
    - Scans = lock entire table = lower overhead
    - Update tuple = lock only the affected tuple = higher concurrency
    - For each lock, transactions must hold **intent locks (IX, IS)** at all higher levels of granularity
        - Indicate a future requirement to lock at a higher level
        - Example: If S lock on tuples is requested, we need intent locks on database, table, and page
        - IX = intent to acquire exclusive lock on lower level
        - IS = intent to acquire shared lock on lower level
        - SIX = shared + intent to acquire exclusive lock at lower level. (equivalent to having both S and IX locks - can read entire table and acquire X locks when needed)
        - In order to acquire S, a transaction must also have the IS lock (same for X)

![Untitled](Transactions/Untitled%203.png)