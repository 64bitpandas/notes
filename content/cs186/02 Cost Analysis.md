# Cost Analysis

In order to make efficient queries, we need a measure of how good or fast a query is. Knowing that queries operate on records, which are stored on pages in a file on disk, we can use the following cost model for analysis:

- $B$ = number of data blocks in file
- $R$ = number of records per block
- $D$ = average time to read or write disk block

For analysis, we will use the following assumptions:

- We are mostly concerned about the **average** case.
- The workload is **uniform random.**
- Inserts and deletes operate on **single records.**
- Equality selections will have **exactly one match.**
- Heap files always **insert to the end of the file.**
- Sorted files are always sorted according to search key.
- Packed files are compacted after deletions.

## Operation Costs

| Operation | Heap File | Sorted File | Explanation |
| --- | --- | --- | --- |
| Scan all records | ⁍ | ⁍ | All records = need to access every block in the file |
| Equality Search | ⁍ (expected) | ⁍ | Heap: on average, need to go through half the file
Sorted: Binary search runtime |
| Range Search | ⁍ | ⁍ | Heap: no guarantee on location of elements in desired range
Sorted: binary search to find start of range; range is ⁍ pages long |
| Insertion | ⁍ | ⁍ | Heap: read last page, then write page
Sorted: find location (binary search), then insert and shift rest of file |
| Deletion | ⁍ | ⁍ | Heap: need to find page first, then write it back (hence the +1)
Sorted: find location (binary search), then delete and shift rest of file  |


