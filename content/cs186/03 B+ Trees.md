# B+ Trees

## The Representation

![Untitled](B+%20Trees/Untitled.png)

**Main idea:** a search tree with a high branch factor. (Lower depth = faster runtime!)

- Recursively index the key file such that:
    - **Great than or equal to index:** Go to the right
    - **Less than the index:** Go to the left

All entries within each node are sorted.

### Occupancy Invariant

The **order** of the tree, $d$, is defined such that each interior node is at least partially full:

- $d \le E \le 2d$

where  $E$ is the number of entries in a node. In other words, every node must have at least $d$ entries and at most $2d$ entries.

The **fan-out** is equal to $2d+1$. (This is the max number of pointers in each node.) The amount of data a B+ tree can store grows exponentially based on the fan-out factor: $f^h$ where $f$ is the fanout and $h$ is the height of the tree.

At typical capacities (fan-out of 2144), at a height of 2 the tree can already store $2144^3 = 9855401984$ records!

## Disk Storage

On the disk, a B+ Tree consists of **indexed files** which have data pages and index pages. (Data pages go first.)

- Index pages include key-value pairs of an index and a pointer.
- Data pages are allocated dynamically and may not be in sequential order. (next and prev pointers can be used)

There are three primary methods of storing data:

1. Store by value: directly store all data into the leaf pages.
    1. Makes it very inefficient to access values if using an alternate index
2. Store by reference: store <key, recordId> pairs in the index
3. Store by pointers: store <key: [ptrs...]> pairs. Allows for large numbers of duplicate entries.

## Operations

### Insertion

B+ Tree insertion is guaranteed to maintain the occupancy invariant.

For the following steps, we will use the example of trying to insert the value $21$ into the tree below:

![Untitled](B+%20Trees/Untitled%201.png)

1. Find the leaf node where the value should go (using binary search):
    
    ![Untitled](B+%20Trees/Untitled%202.png)
    
2. If the leaf node now has more than $2d$ entries:
    1. Split the leaf node into two leaf nodes $L_1$ and $L_2$ with $d$ and $d+1$ entries, respectively.
    
    ![Untitled](B+%20Trees/Untitled%203.png)
    
    b. **Copy** the first value of $L_2$ into the parent node and adjust pointers to include $L_1$ and $L_2$.
    
    ![Untitled](B+%20Trees/Untitled%204.png)
    
3. If the parent is now overflowed, then recurse and do the algorithm again. But this time, instead of copying the first value, we will **move** it instead (doesn’t stay in the original node).

### Deletion

In practice, the occupancy invariant is often not strictly enforced. This is because rearranging the tree is less efficient than having a good-enough approximation. 

Therefore, for B+ Tree deletion, just identify the leaf node that contains the desired value to delete, and simply remove it. Nothing else needs to be done.

This is acceptable in practice because it is usually far more common to insert values into a B+ tree than it is to delete them, and insertions will restore the occupancy invariant quickly.

## Optimizations and Improvements

### Bulk Loading

B+ Tree operations are rather inefficient in that we currently always need to start searches from the root. In addition, there is poor cache utilization due to large amounts of random access.

Bulkloading a B+ tree creates a slightly different structure, but has some nice guarantees that allow it to be used when constructing new trees from scratch.

In bulk loading:

1. Sort the data by a key.
2. Fill leaf pages up to size $f$ (the **fill factor**).
3. If the leaf page overflows, then use the insertion split algorithm from a normal B+ tree.
4. Adjust pointers to reflect new nodes if needed.

### Sibling Pointers

To aid in tree traversal, we can add previous and next pointers between the child nodes:

[[]]

When stored in sequential order, data nodes can be visited from other data nodes more quickly.

### Variable Length Records

## Indexing

We can index a collection on any **ordered** subset of columns.

In an ordered index (such as a B+ Tree), the keys are ordered **lexicographically** by the search key columns:

- First, order by the 1st column.
- If there are rows with identical values in the 1st column, sort them by the 2nd column.
- Continue until all columns are processed.

### Composite Search Keys

A **composite search key** on a set of columns $(k_1, \cdots, k_n)$ matches a query if:

- the query is a conjunction of zero or more **equality clauses:**
    - `k1 = v1 AND k2 = v2 .. k_m = v_m`
- and at most 1 **range clause:**
    - either $k_{m+1} < v_{m+1}$ or $k_{m+1} > v_{m+1}$

Intuitively, a composite search key matches a continuous range of rows in the lexicographically sorted table.

### Indexing By Reference

Rather than storing the data directly in B+ tree entries, we should store pointers (references) instead. This allows for multiple trees to be constructed on the same set of data, regardless of how it is represented on disk. In this way, data can be indexed in multiple columns.

### Clustered Indexes

![Untitled](B+%20Trees/Untitled%205.png)

In a clustered index, data on disk is roughly sorted (clustered) with respect to an index. This benefits accesses using that index, but may hurt performance for other indices.

- Clustering can only be done if data is stored by reference (not by value).
- Clustered indexes are more expensive to maintain (since we need to periodically update the order of files and reorganize).
- Clustered indexes also work best when heap files have extra unfilled space to accommodate inserts, resulting in a larger number of pages.