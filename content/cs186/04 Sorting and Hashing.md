---
title: "Sorting and Hashing"
weight: 40
---

## Introduction
When dealing with disk operations, traditional sorting algorithms tend to create lots of random accesses and can be quite slow. We’ll explore a few strategies for creating optimized algorithms for sorting databases that work around our limited memory and buffer management abilities.

## Relevant Materials
 - [Note 6: Sorting](https://notes.bencuan.me/cs186/coursenotes/n06-Sorting.pdf)
 - [Note 7: Hashing](https://notes.bencuan.me/cs186/coursenotes/n07-Hashing.pdf)
 - [Discussion 4: Sorting](https://docs.google.com/presentation/d/1ZZxV_EziQJd47w3MNo72X4z8c7upX4KGiMqvuEI-vnM/edit#slide=id.g157c8825e69_0_1744)
 - [Discussion 5: Hashing](https://docs.google.com/presentation/d/1vsnH3HhD5SlBZpfnLkeUAoYLeoD9jOQ_0ADcS5A7hR0/edit#slide=id.g4fe834b467_0_0)

## Single-Pass Streaming

Single-pass streaming is an approach for mapping inputs to their desired outputs while minimizing memory and disk usage. We will see this principle being used for many algorithms in this course.

**Main idea:** There are two buffers (input and output). Continuously read from the input buffer and convert them into outputs to place in the output buffer. Only write to disk when the output buffer fills.

![Untitled](Sorting%20and%20Hashing/Untitled.png)

**Optimization: double buffering**
- The main thread runs the function that converts inputs into outputs.
- A second I/O thread runs simultaneously to handle the filling and draining of input and output buffers.
- If the main thread is ready for a new buffer to compute, swap buffers between the two threads.

## Two-Way External Merge Sort

Two-Way External Merge Sort is a building block to generalized merge sort.

**Main idea:** As input buffers are streaming in, sort each input buffer, then merge two input buffers together into one output buffer using merge sort. Repeat until all pages are merged.

![Untitled](Sorting%20and%20Hashing/Untitled%201.png)

For larger input sets that span multiple pages, several passes are required. In each pass, pages are merged together and double in size.

**I/O Cost Analysis**
- Suppose we have $N$ pages.
- In every pass, we read and write each page in file, causing $2N$ IO’s.
- The number of passes is logarithmic in nature: $\lceil \log_2 N \rceil + 1$
- Multiplying the number of passes by the cost per pass gives a total cost of $2N \cdot (\lceil log_2 N \rceil + 1)$.

## General External Merge Sort

In a typical system, we have more than 3 buffer pages available to us at a time. So, we can merge more than two pages at a time. Let's walk through how this might look like (with the example from Discussion 4):

![ms](<Sorting and Hashing/Pasted image 20230108224822.png>)

### Pass 0
In the example above, we have 8 data pages of 2 records each. Since we can only fit 4 pages in the buffer at once, we will need multiple passes.

For pass 0, the goal is to create the largest sorted runs possible by filling the buffer with records. Since our buffer can fit 4 pages at once, we'll end up creating 2 sorted runs of 4 pages each. **Pass 0 does not need to use an output buffer, since we're not streaming anything!** Every set of 4 pages is self-contained.

Eventually, we'll create the two runs below by grouping 4 pages together and sorting them in memory:
```
[0, 1, 6, 9, 10, 17, 20, 25] (pages 0-3)
[2, 3, 4, 7, 8, 11, 12, 15] (pages 4-7)
```

This process takes $2N$ I/Os, where $N$ is the total number of pages, because we need to first read all the pages then write them all back out once they're sorted into runs.

### Pass 1
For the next pass, we *do* need an output buffer, since we must persist data in between runs to combine them. This is what it might look like in memory:
![p1](<Sorting and Hashing/Pasted image 20230108225437.png>)
Now that we're using general external merge sort, you can see that we can merge up to 3 sorted runs at the same time ($N-1$). But since only 2 were created, the final input buffer will be left empty. 

The process of sorting in-memory is as follows:
1. Read in all of the input pages.
2. Find the minimum value out of all of the input pages.
3. Write that value to the output buffer, and delete it from its source input buffer.
4. If the output buffer is full, write it to disk and empty it.
5. If all input buffers are full, flush the rest of the output buffer to disk and we're done!

### Calculating the Number of Passes
The number of passes required to sort $N$ pages when we have $B$ buffers is given by the equation below:
$$1 + \lceil \log_{B-1} \lceil N / B \rceil \rceil$$
The $1$ at the front is for Pass 0. This creates $N/B$ runs of length $B$. 

Then, in every pass, we combine $B-1$ runs into a single run. The algorithm completes when the number of runs left is $1$, so we need to figure out how many times to divide the initial number of runs $N/B$ by $B-1$ before it becomes $1$, which can be done using the $\log$ term. 

One implication of this equation is that the number of required passes decreases exponentially with respect to the number of buffer pages!

### Calculating the I/O Cost of External Sort
The I/O cost calculation is actually pretty simple once we know the number of passes. In each pass, we read every page in and write every page out once, so we can just multiply the number of passes by $2N$:
$$2N(1 + \lceil \log_{B-1} \lceil N / B \rceil \rceil)$$


## External Hashing

Hashing is best for when we don’t care about the absolute order of elements, but only to group similar elements together. This is useful for GROUP BY operations.

In 61B, we learned how to create hash tables using an array of linked lists. However, this method only works if we have enough memory to store the entire collection of data at the same time, so we'll need to modify this a bit!


### Divide and Conquer
The main idea of external hashing is use a two-step process:
1. Break down the problem into smaller parts until each subpart can fit entirely into memory.
2. Combine the partitions back together to create one big hash table. 
![Untitled](Sorting%20and%20Hashing/Untitled%202.png)

Essentially, by partitioning the values, we are splitting a large file into many smaller files, each one with at most $B$ pages.

Since these smaller files can each fit into the buffer, we can then use our normal methods to create an in-memory hash table, which will group everything together.

### How is this different from sorting?
There are a few important differences:
1. Rather than creating a smaller number of longer runs for each pass, we're creating a larger number of smaller runs.
2. In the real world, no hash function can always uniformly partition data. So, we will probably end up having some groups being larger than others.
3. We might end up only filling a part of a page in some partitions, even though we started with completely full pages. This means that the number of writes per pass might be greater than the number of reads. (Example: If we had $N=35$ and created $10$ uniform partitions, each partition would be $4$ pages long (3.5 rounded up). So we'd have 35 reads, and 40 writes.)

### Use unique hash functions!
If we used the same hash function to create partitions in every pass, then our partitions would never get smaller! So, for every pass of external hashing, we must use a different hash function.

Another related issue is when we have a very large number of identical values, since they won't ever be broken down. When implementing hashing, we should add in a check for this case and stop recursively partitioning if it occurs.

### Calculating I/O Cost of Hashing
As a consequence of the above, we can't write a clean formula for calculating the I/O cost of hashing. Luckily, there is a straightforward process we can use instead.

For this part, let's suppose that $B=10$ and we have $N=100$ pages to hash. Our first hash function creates one partition of size $50$, one partition of size $29$, and seven partitions of size $3$. All future hash functions are uniform (i.e. they create $B-1$ partitions of equal size).

#### Pass 1
First, let's calculate the I/O cost of the first pass:
* We read in all $N=100$ pages, which takes $100$ I/Os.
* We write $50 + 29 + 7*3$ pages, which takes $100$ I/Os
* In total, Pass 1 takes $200$ I/Os.

#### Pass 2
For the next pass, we only advance the partitions which don't fit in memory ($n \le B$). In this case, only the two large partitions (50 and 20) satisfy this, so they are recursively partitioned.
 - It takes $50 + 29 = 79$ I/Os to read in the data for this pass.
 - The partition of size $50$ gets broken down into $B-1=9$ equal partitions of size $\lceil 50/9 \rceil = 6$. This incurs $9*6=54$ I/Os to write the grouped partition back to disk.
 - The partition of size $29$ gets broken down into $9$ equal partitions of size $\lceil 29/9 \rceil = 4$. This incurs $9*4=36$ I/S to write.
 - In total, this pass incurs $79 + 54 + 36 = 169$ I/Os.

#### Conquer
Now, all of our partitions fit into disk so we can run the conquer phase to group them back together! To do so, we need to read in every partition we have into memory, and write the grouped version back.

To regroup, this is what our recursively partitioned data looks like right now:
 - $7$ partitions of size $3$, from the first pass
 - $9$ partitions of size $6$, from recursively partitioning the $50$ page partition
 - $9$ partitions of size $4$, from recursively partitioning the $29$ page partition

So, to read and write all of this will take $2 \times (8*2 + 9*6 + 9*4) = 212$ I/Os

#### Total
The I/O cost of hashing in this example is $200 + 169 + 212 = 581$ I/Os.
![diagram](<Sorting%20and%20Hashing/Pasted%20image%2020230109000909.png>)
