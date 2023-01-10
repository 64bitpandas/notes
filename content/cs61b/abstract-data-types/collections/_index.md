---
linkTitle: "Collections"
BookCollapseSection: true
weight: 10
---

![An overview of all the Collections in Java.](<../../img/assets/image (3).png>)

**Collection** is a Java interface for common abstract data types that store multiple items in them.

## Sub-Interfaces

* **Lists** are indexed sequences with duplication. The two most common types are [**ArrayLists**](/cs61b/abstract-data-types/collections/arrays.md#array-lists)  and [**Linked Lists**](linked-lists.md).
* [**Sets**](/cs61b/abstract-data-types/collections/sets.md)  are non-indexed sequences with no duplication. (That is, every value in a set is unique.)
* **Maps** are key-value pairs. See [Hashing and Hash Tables](/cs61b/abstract-data-types/hashing.md) for a description on one common map implementation, the HashMap. All keys in a map must be unique, but values can be duplicated.
* [**Stacks and Queues**](/cs61b/abstract-data-types/collections/stacks-and-queues.md)  are two ordered collections that have two core behaviors:
  * push(T x): puts x on the top.
  * pop(): Removes the first item. (See the stacks and queues page for more information.)

## Common Functions

* **Membership tests** `contains()` and `containsAll()` that can determine whether or not an element is in the collection.
* `size()` to get the number of items in the collection.
* `isEmpty()` returns true if there is nothing in the collection.
* `iterator()` returns an Iterator object to go through all the values in the collection.
* `toArray()` converts the collection to a standard Java array.
* **Optional** functions that aren't implemented in the interface: `add, addAll, clear, remove, removeAll, retainAll (intersection)`
  * Throws `UnsupportedOperationException` if not implemented.
