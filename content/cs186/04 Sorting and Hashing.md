
When dealing with disk operations, traditional sorting algorithms tend to create lots of random accesses and can be quite slow. We’ll explore a few strategies for creating optimized algorithms for sorting databases.

## Single-Pass Streaming

Single-pass streaming is an approach for mapping inputs to their desired outputs while minimizing memory and disk usage.

**Main idea:** There are two buffers (input and output). Continuously read from the input buffer and convert them into outputs to place in the output buffer. Only write to disk when the output buffer fills,

![Untitled](Sorting%20and%20Hashing/Untitled.png)

**Optimization: double buffering**
- The main thread runs the function that converts inputs into outputs.
- A second I/O thread runs simultaneously to handle the filling and draining of input and output buffers.
- If the main thread is ready for a new buffer to compute, swap buffers between the two threads.

## Two-Way External Merge Sort

**Main idea:** As input buffers are streaming in, sort each input buffer, then merge two input buffers together into one output buffer using merge sort. Repeat until all pages are merged.

![Untitled](Sorting%20and%20Hashing/Untitled%201.png)

For larger input sets that span multiple pages, several passes are required. In each pass, pages are merged together and double in size.

**I/O Cost Analysis**
- Suppose we have $N$ pages.
- In every pass, we read and write each page in file, causing $2N$ IO’s.
- The number of passes is logarithmic in nature: $\lceil \log_2 N \rceil + 1$
- Multiplying the number of passes by the cost per pass gives a total cost of $2N \cdot (\lceil log_2 N \rceil + 1)$.

## General External Merge Sort

In a typical system, we have more than 3 pages available to us at a time. So, we can merge more than two pages at a time.

We can leverage the full power of our buffer pool to minimize the number of pages created in the 0th pass:

If we have $B$ pages in our buffer pool, then for every pass after the 0th pass, merge $B-1$ pages into one output buffer. (Since there is no output in pass 0, it can use all $B$ pages.)

**Runtime Analysis**

- The number of passes now becomes $1 + \lceil \log_{B-1} \lceil N / B \rceil \rceil$.
- The total IOs per pass does not change from 2-way merge sort.
- So, the total number of IOs becomes  $2N \cdot (1 + \lceil \log_{B-1} \lceil N / B \rceil \rceil)$.
- The number of required passes decreases exponentially with respect to the number of buffer pages.

## Hashing

Hashing is best for when we don’t care about the absolute order of elements, but only to group similar elements together. 

**Main idea:** use a hash function. Stream values with similar hash values to the same partition. Then, re-hash in memory using a different hash function and write the results to disk.

Essentially, by partitioning the values, we are splitting a large file into many smaller files, each one with at most $B$ pages.

Since these smaller files can each fit into the buffer, we can then use a more specific hash function to split them apart however we wish.

![Untitled](Sorting%20and%20Hashing/Untitled%202.png)

**Recursive partitioning:** if the first division step doesn’t divide into small enough partitions (# pages > B), just keep dividing using different hash functions until the files are the correct size.

- If all of the elements in a partition are the same, then immediately write it to disk instead of recursing as to avoid an infinite loop.

The number of input buffers read does not necessarily equal the number of output buffers created, since some output partitions could not be completely full.