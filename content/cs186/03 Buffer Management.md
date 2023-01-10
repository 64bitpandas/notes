---
title: "Buffer Management"
weight: 30
---

## Introduction
So far, we've established the fact that the disk is slow, and memory is fast- and that one of the biggest challenges in database implementation is in minimizing the number of times we need to incur I/Os by transferring data in between disk and memory.

Since memory is limited, we need to figure out a clever way to re-use information once it's read into memory, while still allowing new information to come in when needed. This way, we can minimize the number of times we need to read the disk in order to find something.

The system that does this is the **buffer manager.** It employs a **page replacement policy** to decide which pages to evict when the buffer is full and a new page is read from disk.

## Relevant Materials
 - [Note 5](https://notes.bencuan.me/cs186/coursenotes/n05-BufferMgmt.pdf)
 - [Discussion 3](https://docs.google.com/presentation/d/1ZZxV_EziQJd47w3MNo72X4z8c7upX4KGiMqvuEI-vnM/edit#slide=id.g157c8825e69_0_0): view this for buffer management walkthroughs!

## Page Replacement Policies

### LRU
**L**east **R**ecently **U**sed policy: evict the page that was least recently accessed. This makes intuitive sense because if a page hasn't been used in a long time, then it's likely we don't need it anymore!

### Clock
Although LRU seems pretty good, it can get quite inefficient since we need to keep track of the latest access time for every page in the buffer, and quickly find the oldest time (probably using some sort of heap).

Thankfully, we can approximate LRU with the Clock policy! Rather than strictly using the latest access time, we'll instead add a **reference bit** to each frame.

See [Discussion 4](https://docs.google.com/presentation/d/1ZZxV_EziQJd47w3MNo72X4z8c7upX4KGiMqvuEI-vnM/edit#slide=id.g157c8825e69_0_58) for a walkthrough, or if you prefer to read the algorithm, go to the next section.

### Detailed Clock Algorithm

**On initialization:** Set the clock hand to point to the 0th entry, and set all reference bits to 0.
  
**When trying to access a page from memory:**
1.  Iterate through the entire cache looking for the page. If found, set the reference bit of the page to 1 and return the page. *DO NOT* move the clock hand!
2. If not found, go back to the clock hand's location and do the following:
	1. Skip all pinned pages. (A page is pinned if it's currently in use, meaning we cannot evict it from the cache.)
	2. If the current entry has a reference bit of 0, then set the reference bit to 1, evict that entry, replace it with the desired entry from disk, and return it.
	3. Otherwise, set the reference bit to 0, advance the clock hand, and repeat the previous 2 steps.

### MRU
Another major issue with LRU (and Clock, to some extent) is that it struggles with repeated patterns that are longer than the number of buffer frames available.

For example, the access policy ABCDEABCDEABCDEABCDE would result in $0$ hits if we had $4$ or fewer buffer frames, since $E$ would always evict $A$, $A$ would then evict $B$ which would evict $C$, and so on. This problem is known as **sequential flooding.**

The solution to sequential flooding is to use **M**ost **R**ecently **U**sed policy, replacing the page that was used the earliest. If we fed the ABCDE example into a MRU policy, it would result in far more hits (since only two replacements would be needed per cycle, rather than 5).

## Exam Tips
A very common exam question would look something like this:

> Given the access pattern ABCDEDEFG and a buffer manager with 4 frames, what is the hit rate of <LRU/MRU/Clock>? Express your answer as "X/Y", where X is the number of hits and Y is the total number of requests.

In my opinion, the best way to tackle these problems is to draw a grid that looks something like this:

| Frame | A     | B   | C   | D   | E   | D   | E   | F   | G   |
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1     |  |     |     |     |     |     |     |     |     |
| 2     |   |     |     |     |     |     |     |     |     |
| 3     |   |     |     |     |     |     |     |     |     |
| 4     |   |     |     |     |     |     |     |     |     |

Then, for each access, list which pages are in the buffer at that point in time, marking the hits. Below is an example for LRU, which would have a hit rate of $2/9$:

| Frame | A     | B   | C   | D   | E   | D   | E   | F   | G   |
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1     | A |  A   |  A   |  A   |  E   |     |  HIT   |  E   |  E   |
| 2     |   |  B   |  B   |  B   |  B   |     |     |   F  |   F  |
| 3     |   |     |   C  |  C   |  C   |     |     |  C   |   G  |
| 4     |   |     |     |  D   |   D  |  HIT   |     |  D   |  D   |

Clock is a bit harder to do, but still managable. I prefer still using the grid method, rather than drawing out the clock face and having to keep erasing the clock hand to advance it. I usually do this by keeping track of the hand position and reference bits. In the example below, the `+`  represents the clock hand, and the reference bit is the number after each page letter:

| Frame | A     | B   | C   | D   | E   | D   | E   | F   | G   |
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1     | +A1 |  +A1   |  +A1   |  +A1   |  +E1   |   +E1  |  +E1 (HIT)   |  E0   |  E0   |
| 2     |     |  B1   |  B1   |  B1   |  B0   |  B0   |  B0   |   +F1  |   F0  |
| 3     |     |       |   C1  |  C1   |  C0   |   C0  |   C0  |  C0   |   +G1  |
| 4     |     |       |       |  D1   |   D0  |  D1 (HIT)   |  D1   |  D1   |  D1   |


