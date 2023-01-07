---
title: "What is an I/O and why should I care?"
weight: -1
---
If you're taking 186, you've probably heard or experienced some variation of the following:
 - This class has a lot of I/O counting on exams
 - I/Os are weird, sometimes you can read like 5 things at the same time but it's still one I/O for some reason
 - I/O counting is tedious and boring and I will never do it after this class, so why do I need to do it??????

While I can't guarantee that you'll ever count I/Os after this class, my hope for this article is to justify why it's necessary for understanding key database design concepts, and how the principles can be applied to real-world issues in query optimization. It's like learning how to multiply numbers by hand when we have calculators: although functionally obsolete, we still need to understand the mechanics before we can start taking the shortcut.


## The Problem

The biggest issue that most database solutions solve is that **disks are slow and memory is fast, but we don't have enough memory to store everything we need.**

Think about trying to process hundreds of gigabytes of data on your computer (very common for applications like machine learning), even though you only have something like 16GB of RAM.

If we want our operations to complete in a reasonable amount of time, we'll want to do as much as possible within RAM. Most of the algorithms you've likely encountered in 61B assume that we have an *infinite* amount of fast memory, and that all operations took the same amount of time, since we only cared about asymptotic runtimes.

However, in the real world, reading something from memory could be hundreds of thousands of times faster than reading something from disk. As such, when evaluating the runtime of an algorithm we only care about how long it takes to transfer something from disk into memory so that we can access it. This basic unit of time is what we call the Input-Output cost, or "an I/O" for short.


## Definition of an I/O

> [!abstract] Summary
> 
> **An I/O is a single read or write event where one page of data is transferred between memory and disk.**

A **page** is the basic ("atomic") unit of information on disk: since it's more efficient than reading one byte at a time, nearly all modern hard drives and SSDs have some hard-coded block size in their firmware, such that any data accessed from them will always be delivered one block at a time. These blocks are then converted into pages, which also have a fixed size, in the operating system.

For the purposes of this class, **"block" and "page" can be used interchangably.** In most contexts we will refer to it as a page. However, in general, [there is a difference.](https://stackoverflow.com/questions/22137555/whats-the-difference-between-page-and-block-in-operating-system)

A very important thing to note down is that **there is no such thing as a fractional I/O.** If we need to read 4.1 pages' worth of data, it will really take 5 I/Os since the last page needs to be read in its entirety.

## Applications

The primary application for evaluating I/O cost is for [query optimization](<cs186/07 Query Optimization>), where we need to decide which operation is the most efficient out of several possibilities. 

**Why can't we just use asymptotic runtime?**
 - We're dealing with known, finite input sizes: We may decide to use a different algorithm for a 1000-row table versus a 10000000-row table, even if the algorithm for the former has poorer asymptotic properties.
 - The difference between a $O(n)$ algorithm and an $O(2n)$ algorithm can get extremely noticable when we have millions (or billions) of rows in a table.
 - The runtime depends on the data that we put in. For instance, certain types of joins (like Sort-Merge Join) perform poorly when we have large amounts of duplicate data. Since we already know (or can approximate) what data we have, we can use this knowledge to estimate how much of the data will need to be accessed to complete the operation, which may be dramatically better or worse than its average runtime.

## Practice

Here are some basic I/O problems to test your understanding, before moving onto applying it to more involved algorithms. **For all of the below problems, assume that one page can store 5 (five) integers, and that all available space on a page will be used before a new page is created.**

{{< tabs "q1" >}}
{{< tab "Q1" >}}
Alice has an array `[1, 2, 3, 4, 5]` stored on disk. She changes the `3` into a `6`, then writes the updated array back to disk. How many I/Os did this operation incur? 
{{< /tab >}}
{{< tab "Q1 Solution" >}}
**2 I/Os**. One to read the entire array (since it's on the same page), and one to write the entire array back.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q2" >}}
{{< tab "Q2" >}}
Bob has an array `[10, 7, 9, 8, 6]` stored on disk. He performs an in-place Insertion Sort and reads the result, but does not save it. How many I/Os did this operation incur? 
{{< /tab >}}
{{< tab "Q2 Solution" >}}
**1 I/O**, which is incurred when Bob reads the entire array from disk. No I/Os are incurred for actually performing the sort, since all of the swapping operations are done in memory which do not count.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q3" >}}
{{< tab "Q3" >}}
**Challenge:** How many I/Os does it take to insert a page at the end of a linked list of $N$ pages? Assume the pointer to the next page is stored within each page (so no additional data is needed).
{{< /tab >}}
{{< tab "Q3 Solution" >}}
**N + 2 I/Os.** To find the end of the linked list, we first need to read all $N$ pages. Then, we need to perform 2 writes- one to update the next pointer of the now second-to-last page, and one to write the new page.
{{< /tab >}}
{{< /tabs >}}