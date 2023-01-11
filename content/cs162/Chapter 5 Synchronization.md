---
title: "Chapter 5: Synchronization"
---

## Race Conditions and Locks

If two independent threads need to modify and read the same values, there could be multiple outputs depending on the order that the threads run in. How do we resolve this?

**Synchronization** deals with coordination among threads and their shared data

**Mutual Exclusion:** Only one thread does something at one time (excludes the other threads)

- Subtype of synchronization

**Critical Section:** code that only one thread can execute at once (consequence of mutual exclusion)

# High Level Concurrency API

## Locks

**Lock:** An object that only one thread can hold at a time (provides mutual exclusion)

- `lockacquire()` or `pthread_mutex_lock` waits until lock is free, then marks as busy
- `lockrelease()` or `pthread_mutex_unlock` frees a lock (calling thread no longer holds the lock)

## Semaphores

A general type of lock that holds a non-negative integer.

- `P()` or `down()`: waits for semaphore to be positive, then decrements by 1
- `V()` or `up()`: increments semaphore by 1

Can be used for mutual exclusion by setting it down, running critical section, then setting it up.

![Untitled](Chapter%205%20Synchronization/Untitled.png)

Semaphores can also be used for signaling other threads:

![Untitled](Chapter%205%20Synchronization/Untitled%201.png)

## Monitors

## Send/Receive

## Condition Variables

### Readers/Writers

# Atomic Operations

## Load/Store

## Disable Ints

## Test and Set

## Compare and Swap