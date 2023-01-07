# Disks, Buffers, Files

## Devices

**Hierarchy:**

![Untitled](Disks,%20Buffers,%20Files/Untitled.png)

Page = Block = atomic unit for disk IO (can’t write a fractional page)

Sequential runs are assumed to be fast.

### HDD

Hard drives are magnetic disks that contain tracks of data around a cylinder. 

HDD's are generally good for sequential reading, but bad for random reads.

![Untitled](Disks,%20Buffers,%20Files/Untitled%201.png)

**Disk Latency = Queueing Time + Controller Time + Seek Time + Rotation Time + Transfer Time**

- Queuing Time: amount of time it takes for the job to be taken off the OS queue
- Controller Time: amount of time it takes for information to be sent to disk controller
- Seek Time: amount of time it takes for the arm to position itself over the correct track
- Rotation Time (rotational latency): amount of time it takes for the arm to rotate under the head (average is 1/2 a rotation)

**Disk space management:**

- provides an API to read and write pages to device
- Organizes bytes on disk into pages
- Provides locality for the ‘next’ sequential page
- Abstracts filesystem and device details

## Representations

A **Database file (DB FILE)** is a collection of pages, which each contain a colection of records.

- Can span multiple machines and files in the filesystem
- Types of DB file structures:
    - Unordered **heap files** (arbitrarily placed across pages)
        - As file shrinks or grows, pages are deallocated
        - Requirements: keep track of pages, free space, and records in page
        - Use a **page directory** that includes free byte count and pointer to referenced pages
        - Best for frequent stores, rare lookups
    - Clustered heap files (records and pages are grouped by a field)
    - Sorted files (records and pages in a sorted order)
        - Best for infrequent stores, frequent lookups
    - Index files (B+ trees, linear hashing, etc) that may also point to records in other files

### Pages

- The **page header** includes metadata like free space, # of records, pointers, bitmaps, slot table...
- If records are fixed length, we can pack them densely:
    
    ![Untitled](Disks,%20Buffers,%20Files/Untitled%202.png)
    
    - We can easily append to add. To delete, we would need to rearrange the pointers (can be expensive).
- We can also have **unpacked** fixed length records:
    
    ![Untitled](Disks,%20Buffers,%20Files/Untitled%203.png)
    
    - Keep a **bitmap** of free and empty slots in the header.
    - To add, find an empty slot in the bitmap and mark it as filled.
    - To delete, just flip the bitmap reference to 0.
- For variable length records:
    - Use **slotted page records**
    - Relocate the page header into the footer. (This will allow for the slot directory to be extended.)
    - In the footer, store pointers to free space containing the length and pointer to the next record.
    - Can be prone to fragmentation (will need to be addressed somehow).
    - Can also be used for fixed length records to handle null records

### Records

Fixed length records:

- Field types are the same for all records, so just store the type information in memory. Variables can be accessed in the same location every time.

Variable length records:

- Move all variable length fields to the end of the record
    
    ![Untitled](Disks,%20Buffers,%20Files/Untitled%204.png)
    
- Create a header in the beginning to point to the end of variable length fields (compute beginning based on presence of other variables)

## Evaluating File Structures

There are two primary criteria used for evaluating the effectiveness of a file structure: **IO Cost** (total number of read and write operations), and **record size** (the number of bytes needed to store each record).

### Calculating Record Size

Records consist of atomic values like ints and chars. Typically, records also include pointers (depending on implementation) as well as variable length records.

![Untitled](Disks,%20Buffers,%20Files/Untitled%205.png)

For a standard record in a linked list, the following is required:

- $N$ bytes for each variable, where $N$ is its size in the chart above
- One 4-byte pointer in the header for every variable length record
- If nullable, each **non-primary key** takes 1 bit in the bitmap. Make sure to round up to the nearest byte.
- If using a slotted page implementation for variable length records, we’ll need 8 additional bytes in the header (free pointer, slot count) and 8 additional bytes in every record (record length, record pointer).

The maximum number of records that can be stored in a page is equal to the page size divided by the minimum record size, rounded down to the nearest integer.

- For slotted page, it would be the floor of (page size - 8 bytes) / (min record size + 8 bytes) due to the additional metadata needed.

The slot directory in a slotted page implementation has the following items:

- slot count (4 bytes)
- free space pointer (4 bytes)
- (record pointer + record size) tuple for every record (8N bytes)

### Calculating IO Cost

For a linked list implementation,