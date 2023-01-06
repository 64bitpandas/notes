---
title: "Generic Types"
weight: 5
---

Sometimes, we want things to support **any type**, including user defined types that we don't know about! For example, it would make sense that we don't care what type we make a `List` out of, since it's just a whole bunch of objects put together.

The Java solution is **generics!** Generic types are denoted by a `<>` and can be appended to **methods and classes.** Here's an example with classes:

```java
/**
  * Creates a type SomeClass that takes * in a generic SomeType. SomeType can * be named anything.
*/
public class SomeClass<SomeType> {
    private SomeType someThing;

    public void someMethod(SomeType stuff) {
        doStuff(stuff);
    }
}

...
/** Creates a new instance of SomeClass, setting SomeType to String.
    We don't need to put the type on the right since it's already
    defined on the left. */
SomeClass<String> aClass = new SomeClass<>();
```

In this example, `SomeType` is a **Generic Type Variable** that is not a real type, but can still be used inside the class as normal.

On the other hand, `String` is an **Actual Type Argument** that replaces `SomeType` during runtime. Now, every time `SomeType` is used in `SomeClass` Java treats it exactly like a `String`.

## Generic Subtypes

Like in [Dynamic Method Selection](dynamic-method-selection.md), adding inheritance makes things tricky! Let's look at an example:

```java
List<String> LS = new ArrayList<String>();
List<Object> LO = LS; // Line 3
LO.add(42); // Line 4
String s = LS.get(0); // Line 5
```
{{< tabs "q1" >}}
{{< tab "Question 1" >}}
Will **line 3** error?
{{< /tab >}}
{{< tab "Q1 Answer" >}}
**No**, line 3 is valid and will not error! This is because Object is a **superclass** of String. Generics work in a very similar way to the [inheritance rules](inheritance.md).
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q2" >}}
{{< tab "Question 2" >}}
Will **line 4** error?
{{< /tab >}}

{{< tab "Q2 Answer" >}}
**No**, line 4 is valid and will not error! This is because LO is a **list of Objects** and integers are a **subtype** of Object, as all things are.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q3" >}}
{{< tab "Question 3" >}}
Will **line 5** error?
{{< /tab >}}

{{< tab "Q3 Answer" >}}
**Yes,** line 5 will error! This is because we put 42 into LO, which is an integer. Since LO is pointing to the same object as LS, 42 is also in LS! That means we are trying to assign a String equal to an integer.
{{< /tab >}}
{{< /tabs >}}

> [!info] Content Note
>
> Arrays have slightly different behavior than this and will throw an `ArrayStoreException` if types are mismatched in any way.

## Type Bounds

Sometimes, we want to **put constraints** on what kinds of types can be passed into a generic type.

One way of doing is is to specify that a generic type must fit within a **type bound**: here, T must be some subtype of a specified type `Number`.

We can also do it the other way and specify that a type can be a **supertype** of a specified type. Both of these examples are shown below:

```java
class SomeClass<T extends Number> {
    // A method that takes a type parameter T and takes any SUPERCLASS
    // of T as a list generic type.
    static <T> void doSomething(List<? super T> L) { ... }
}
```

## Limitations of Generic Types

The biggest limitation is that **primitive types cannot be used as generic types.** For example, `List<int>` is invalid and will not work!

One workaround to this is to use the reference-type counterparts to primitives, such as `Integer`, `Boolean`, `Character` and so on. However, converting between these types and primitive types, which is called **autoboxing,** has significant performance penalties that must be taken into consideration.

Another limitation is that **instanceof** does not work properly with generic types. For instance, `new List<X>() instanceof List<Y>` will always be true regardless of what types X and Y are.
