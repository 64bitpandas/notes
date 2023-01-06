---
weight: 2
---

## What is Access Control?

In Java, we can specify the **level of access** certain variables and methods have. With this power, we can show or hide these variables to other classes and references on demand!

There are **4** modifier levels that get progressively more open:

* **Private:** Only this class can see it.
* **Package Protected (the default level):** All classes in the **same package** can see it.
* **Protected: Subclasses** (that inherit from the parent) can also see it.
* **Public:** All classes in the program can see it.

![A chart comparing the different access modifiers. The black bar is the default ("package protected").](<../img/assets/image (5).png>)

## Why do we need access control?

Access control works really well with other OOP concepts to help structure programs better and make them easier to understand. Here are some of the major benefits:

* Access control is **self documenting.** Usually, there's a reason for making certain variables private and others public, and no more needs to be said for that to be understood.
* **It's safe to change private methods without worrying about breaking things.** If a method is private, we know that the only references are within the same class, so we can edit them however we want without making other classes error as well.
* **Private/protected variables don't need to be understood by users.** If someone needs to use your program, they don't need to learn how to use any private methods since those will be hidden to them.

## Practice

Let's see how access control can be used to hide variables in different situations:

```java
package P;
public class A {
    int def; // Variable with default access
    protected int prot; // Variable with protected access
    private int priv; // Variable with private access
    
    static class NestedA { ... }
}

public class B extends A { ... }

===================
package Q;
public class C extends P.A { ... }

```

{{< tabs "q1" >}}
{{< tab "Question 1" >}}
Which variables can be accessed in B?
{{< /tab >}}

{{< tab "Answer" >}}
`def` and `prot` since B is in the same package as A.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q2" >}}
{{< tab "Question 2" >}}
Which variables can be accessed in C?
{{< /tab >}}

{{< tab "Answer" >}}
`prot` only, since C is in a different package but extends A.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q3" >}}
{{< tab "Question 3" >}}
Which variables can be accessed in NestedA?
{{< /tab >}}

{{< tab "Answer" >}}
None of them, because NestedA is static and cannot reference any non-static variables.
{{< /tab >}}
{{< /tabs >}}
