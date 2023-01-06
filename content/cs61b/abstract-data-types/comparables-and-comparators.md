---
weight: 999
---

## What is it?

A **Comparable** is a **generic type** that allows standardized comparisons between objects.

In other words, anything that has a `compareTo()` method can be a Comparable!

Many Java libraries already use Comparable without you knowing! Some of the more well-known ones are `Collection` and `String`.

### CompareTo can't return anything you want!

There are some very specific properties CompareTo needs to have! Usually, we take them for granted but might forget about them when making our own.

* If `x` and `y` are the **same object**, `y.compareTo(x)` must return **0.**
* `x.compareTo(y)` must return the **negative** of `y.compareTo(x)`. (if one throws an error, the other must too!)
* If `x` and `y` are the **same object**, `x.compareTo(z)` must **equal** `y.compareTo(z)` **for all z.**

### Defining a Comparable subclass

```java
public class MyComparable implements Comparable<MyComparable> {
    public int foo;
    ...

    /** Instance method that has nothing to do with comparable */
    public void doSomething() {
        ...
    }

    /** Comparable method used to compare objects of this type */
    public int compareTo(Object o) {
        MyComparable mc = (MyComparable) o;
        return ...
    }
}
```

## **Comparators**

Comparators are used instead of higher order functions in order to provide a **callback** function to methods. One example of where it is used commonly is `Collections.sort`. You can pass in a comparator here to change how items are sorted- for example, you could sort `Person` objects by their `height` variable.

**The interface is as follows:**

```java
public interface Comparable<T> {
 int compare(T o1, T o2);
}
```

### How is it different from Comparables???

Comparable is used to compare **itself** to **other objects**; a Comparator compares **two other objects but not itself.**

