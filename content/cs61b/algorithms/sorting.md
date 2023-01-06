---
title: "Sorting"
weight: 998
---

> [!important] Sorting Guide
>
> For more information about specific sorting algorithms covered in 61B, see my [guide on sorting](https://docs.google.com/document/d/1dUfzdh5V3okrwFbB9o0PgtEBaLHyCqJFwpQWyQ53IeU/edit) that covers all of the sorts in far greater detail 🙂

## Why sort?

* It makes searching for a specific value much faster (e.g. binary search). Typically, searching through an unsorted list requires a full scan ($\Theta(N)$​ runtime).
* It's easy to see if two items in list are equal: just compare to see if any neighboring values are the same.

## Properties of a Sorting Algorithm

A sorting algorithm changes a sequence based on a **total order.** A total order is:

* **Total:** All items can be compared with one another
* **Reflexive:** An item can be compared to itself
* **Antisymmetric:** x <= y AND y <= x IFF y == x
* **Transitive:** If x <= y and y <= z, then x must be <= z

A sorting algorithm could be **stable** if it does not change relative order of equivalent entries. For example, if Bob and I both owned Toyota Corollas, and the list of cars were sorted by model, if Bob's car came before mine originally it must also come before mine in the sorted list after a stable sort.



## Sorting Algorithm Classifications

* **Internal sort:** Keeps all data in primary memory
* vs. **External sort:** Processes data in batches, then merges them together at the end
* **Comparison-based sort:** The only thing we know about keys are their relative orders
* **Radix sort:** Uses information other than keys
* **Insertion sort:** Insert items at their appropriate positions one at a time
* **Selection sort:** Chooses items and places them in order

## Sorting in Java

Java automatically chooses the best sorting algorithm for a given list if you call the `Arrays.sort` method.

```java
String[] x = new String[] {"Vat", "Bat", "Cat"};

Arrays.sort(x); // mutates x into Bat, Cat, Vat
Arrays.sort(x, Collections.reverseOrder()); // mutates x into Vat, Cat, Bat
Arrays.sort(x, 0, 2) // sorts the first two elements, leaving the rest unchanged (Cat, Vat, Bat)
```

## Inversions

Inversions are used as a measure for how sorted a list is. For every two elements that are swapped compared to a sorted list, we add one inversion.

* As an example, if `1 2 3 4 5` is a sorted list, `1 4 3 2 5` would have one inversion (`4` and `2` are swapped).
* 0 inversions mean a list is perfectly sorted.
* In the worst case, a reversed list will have $(N \cdot (N-1))/2$ inversions.

## The Guide to Sorting Algorithms

[A comprehensive guide to sorting algorithms, now with memes!](https://docs.google.com/document/d/1dUfzdh5V3okrwFbB9o0PgtEBaLHyCqJFwpQWyQ53IeU/edit)
