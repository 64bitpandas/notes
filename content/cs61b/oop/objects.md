---
title: "Java Objects"
weight: 4
---

There are two main categories of objects in Java: **Primitive Types** and **Reference Types.** This page will give a brief overview of both, and close off with some info about the mystical **Object** class.

## Primitive Types

**Primitive types** are built in to Java and have **fixed memory sizes.** Different types require different amounts of memory.

If you remember [environment diagrams](http://albertwu.org/cs61a/notes/environments), you may recall that some variables are put straight into the boxes, while others have an arrow pointing to them. The reason for this is that it actually denotes primitive vs. reference types! **Primitive types go straight in the box** because they aren't mutable (i.e. you can't change the objects contained in the box since they're just constant literals like numbers).

**There are 8 primitive types in Java.** Here's a table of their properties! (If you don't know what "signed" means, go to [Modular Arithmetic and Bit Manipulation](/cs61b/misc-topics/modular-arithmetic.md).)

| Type    | Bits | Signed | Default | Examples                      |
| ------- | ---- | ------ | ------- | ----------------------------- |
| boolean | 1    | no     | false   | true, false                   |
| byte    | 8    | yes    | 0       | 3, (int)17                    |
| short   | 16   | yes    | 0       | None - must cast from int     |
| char    | 16   | no     | \u0000  | 'a', '\n'                     |
| int     | 32   | yes    | 0       | 123, 0100 (octal), 0xff (hex) |
| long    | 64   | yes    | 0       | 123L, 0100L, 0xffL            |
| float   | 32   | yes    | 0.0     | 1.23f, -1.23e10f, .001f       |
| double  | 64   | yes    | 0.0     | 1.23e256d, 1e1d, 1.2e-10d     |

> [!hint]  A quick aside on Strings 🧵
>
> You may have noticed that strings are not on this list. That is because unlike in Python, they aren't a primitive type! Under the hood, Strings are a reference type that are very similar to a char array.

## Type Conversion

Java will automatically convert between primitive types if **no information is lost** (
from byte to int).

Conversion in the other direction (from a larger to smaller container) requires an explicit cast (e.g., `(char) int`). The compiler will treat a cast object as though its static type is the cast type, but this will only work if the cast type is the same as or a parent of the dynamic type. However, relative to the assigned static type, the cast type could be a child of the static type or a parent of the static type.

**Assignment statements are an exception to this**: `aByte = 10` is fine even though 10 is an int literal. This is because arithmetic operations (+, \*, ...) automatically promote operands (e.g., `'A' + 2` is equivalent to `(int)'A' + 2`)

However, **this doesn't work if you are trying to add a larger type to a smaller type** (e.g., `aByte = aByte + 1` since operands become an int type which cannot be set equal to a byte type. **But += works**!

## Reference Types

A **reference type** refers to basically anything that's not primitive 😅

This includes **user-defined objects** as well as many common Java built-in types such as **arrays, strings, and** [**collections**](../abstract-data-types/collections/)**.**

Here are some major differences that set them apart from primitive types:

* Reference types can take an **arbitrary amount of memory.** Unlike primitives which have a fixed memory for each type, objects like arrays can expand to hold lots of things inside it.
* Reference types are referred to using **addresses.** When you say something like `int[] arr = new int[5]`, `arr` only stores a 64-bit **memory address** which **points** to the real object, a 5-length integer array. Again, think back to the arrow in environment diagrams, and how those work.
* By default, reference types can be set to **null** which is represented as an **address of all zeroes.** Or, the **new** keyword can be used to set it to a specific address.
* Reference objects can be **lost** if all pointers to it are reassigned. For example, if I now enter `arr = null;`, the original 5-length array still exists, but just has nothing to refer to it.

## The Equals Sign

The assignment operator (`=`) has **different behaviors** for primitive types and references types.

For **primitive types,** `y = x` means "**copy** **the bits** from y into a new location, then call them x". Here, the **entire object** is copied- this means that changing y will NOT change x even though they are set "equal".

For **reference types,** `obj1 = obj2` means "**copy the address** stored in obj1 to obj2". Here, `obj1` and `obj2` are referring to the **exact same object,** and mutating one will change the other.

> [!info] A clarification on reference type assignment
>
> By mutating, I mean changing the **internals** of an object (for example, accessing an array index or doing something like `obj1.value = 1`. If you change the actual **address** of `obj2`, as in `obj2 = obj3`, this does **not** change `obj1` because `obj2` is now referring to a completely different object!
{% endhint %}

## The Object Class

In Java, **all objects inherit from the master Object class.** Here are some important properties of Object that will be useful to know:

* `String toString()`: By default, this prints out the class name followed by the memory address (e.g., `Object@192c38f`). This can be overridden to make more user-friendly names for objects.
* `boolean equals(Object obj)`: By default, this checks if the two objects are actually the same object (same memory address). This can be overridden to check if specific contents of objects are the same, rather than checking if they are literally the same object. (Like `"foo"` should equal `new String("foo")`)
* `int hashCode()`: Returns a numeric hash code for the object that should differentiate it from other objects. **This should be overridden if** **`equals()` is overridden** since `x.hashCode()` should equal `y.hashCode()` if `x.equals(y)` is true!
* `Class<?> getClass()`: Returns the class of this object.

Object has plenty of other methods and properties as well, but these aren't as important. If you want to learn about them, feel free to refer to the [Java documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html).
