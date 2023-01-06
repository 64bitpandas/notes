## What are Heaps?

A heap is a **specific order of storing data,** often in a list. Heaps are very similar to binary trees, but have some differences:

* Unlike trees, heaps **only care about the root node.** Usually, the root node is either the **largest** or **smallest** value in the heap (corresponding with max-heaps and min-heaps), and we don't care too much about the rest.
* Every element in the heap must be **larger than all its children** (in a max-heap) or **smaller than all its children** (in a min-heap). This is known as the **heap property.**

When stored in a list, there is an **important rule** to figure out how to identify parent nodes and their children: **a node's parent has an index equal to half of that node's index.** More specifically, `parentIndex = nodeIndex / 2` where `/` has floor-division properties.

![Converting a heapified list into a min-heap diagram.](<../../img/assets/image (60).png>)

## The Heapify Algorithm

The most important heap algorithm is **heapify**, which converts any non-heap list into a heap. This algorithm is vital to most heap functions like insert or remove, since these functions often break the heap structure before fixing it with heapify.

**Here's how it works:**\
****(This example is an excerpt from my [Sorting Guide](https://docs.google.com/document/d/1dUfzdh5V3okrwFbB9o0PgtEBaLHyCqJFwpQWyQ53IeU/edit). The example provided is a max-heap \[5,6,2,4,1].)

Start with the element in the middle of the array (which is the root of the heap).

![](<../../img/assets/image (61).png>)

If the root is smaller than either of its children (larger for a min-heap), swap it with its largest child (smallest for a max-heap).

![](<../../img/assets/image (62).png>)



If the root was swapped, recursively call heapify on the new position. Otherwise, stop recursion.

After heapify is complete, it should look like this:

![](<../../img/assets/image (63).png>)

## Practical Applications

[Lab 9](https://inst.eecs.berkeley.edu/\~cs61b/sp20/materials/lab/lab9/index.html) is a fantastic resource for practicing heap implementations and working with the algorithms that are needed to work with heaps (like heapify, insert, remove). Since this lab goes into plenty of detail about how each of these algorithms work, I won't explain them too much here.

Heap sort relies on the heap structure to provide consistent nlogn sorting! I have more information about this on page 11 in my [sorting guide](https://docs.google.com/document/d/1dUfzdh5V3okrwFbB9o0PgtEBaLHyCqJFwpQWyQ53IeU/edit).
