
> [!warning] Warning
>
> This page is incomplete. [help make it better!](/contributing.md)

## Basics

A Set stores a collection of values with **no duplicates.** Sets have no inherent order, so you can't rely on expecting any value to come before any other value when iterating through them.

Some set functions include:

* `add(T x)`
* `contains(T x)`
* `size()`

## ArraySet

An ArraySet is an array-based solution to a set implementation.

* Objects get added to an array that gets [resized](../../asymptotics/amortization.md) when it's too full.
* In order to allow for iteration, we can use one of two methods:
  *   One method is to use **iterators** which work very similarly to Python iterators:

      ```java
      Iterator<Integer> seer = set.iterator();
      while (seer.hasNext()) {
        System.out.println(seer.next());
      }
      ```
  * Another method is to implement the `Iterator` and `Iterable` interface.
    * Iterator must implement `hasNext()` and `next()` methods
    * Requires generic type
    * Iterable must implement `iterator()` method which returns the Iterable object
    * Allows usage of for/foreach loops
