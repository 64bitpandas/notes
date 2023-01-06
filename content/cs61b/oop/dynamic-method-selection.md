---
weight: 3
---
# Dynamic Method Selection

> [!warning] Content Note
>
> This is a **very tricky topic**. Make sure you are comfortable with [inheritance](inheritance.md) and [access control](access-control.md)before proceeding!

Inheritance is great and all, but it does have some issues. One of the biggest issues lies in overriding: **if two methods have exactly the same name and signature, which one do we call?**

In a standard use case, this is a pretty simple answer: whichever one is in the class we want! Let's look at some basic examples.

```java
public class Dog {
    public void eat() { ... } // A
}

public class Shiba extends Dog {
    @Override
    public void eat() { ... } // C
}
```

{{< tabs "q1" >}}
{{< tab "Question 1" >}}
Which method is called when we run:

```java
Dog rarePupper = new Dog();
rarePupper.eat();
```
{{< /tab >}}

{{< tab "Q1 Answer" >}}
It's **A** 🐕 Dog doesn't know anything about `Shiba` or any other classes, so we can just look at the Dog.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q2" >}}
{{< tab "Question 2" >}}
What about when we call:

```java
Shiba doge = new Shiba();
rarePupper.eat();
```
{{< /tab >}}

{{< tab "Q2 Answer" >}}
This calls **C**! This works intuitively because `Shiba` overrides `Dog` so all `Shibas` will use C instead of A.

![](<../img/assets/image (8).png>)
{{< /tab >}}
{{< /tabs >}}

## Things Get Wonky: Mismatched Types

There's an interesting case that actually works in Java:

```java
Dog confuzzled = new Shiba();
```

What??? Shouldn't this error because `Dog` is incompatible with `Shiba`?

It turns out that **subclasses can be assigned to superclasses.** In other words, `Parent p = new Child()` works fine. This is really useful for things like [Interfaces](inheritance.md#interfaces) and generic [Collections](../abstract-data-types/collections/) because we might only care about using generic methods, and not the specific implementation that users chose to provide.

However, **it is important to note that it doesn't work the other way.** `Child c = new Parent()` will error because the child might have new methods that don't exist in the parent.

**Let's see how this makes inheritance really tricky:**

```java
/** The following problems are inspired by Spring 2020 Exam Prep 5. */

public class Dog {
    public void playWith(Dog d) { ... } // D
}

public class Shiba extends Dog {
    @Override
    public void playWith(Dog d) { ... } // E
    public void playWith(Shiba s) { ... } // F
}
```

{{< tabs "q3" >}}
{{< tab "Question 3" >}}
Which method(s) run when we call:

```java
Dog rarePupper = new Shiba();
rarePupper.playWith(rarePupper); // aww rarePupper is lonely :(
```
{{< /tab >}}

{{< tab "Q3 Answer" >}}
**E** is called! What happens is that the **dynamic type** is chosen to **select the method from,** but the **static type** is used to **select the parameters.** `rarePupper`'s **** dynamic type is `Shiba` but its static type is `Dog` so `Shiba.playWith(Dog)` is chosen as the method.

![rarePupper in action](<../img/assets/image (10).png>)
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q4" >}}
{{< tab "Question 4" >}}
Which is called when we run**:**

```java
Dog rarePupper = new Shiba();
Shiba doge = new Shiba();
rarePupper.playWith(doge); // rarePupper is happy :) borks all around
```
{{< /tab >}}

{{< tab "Q4 Answer" >}}
**E** is called again! Bet ya didn't see that coming 😎

**Why is it not F? I thought doge and rarePupper were both** `Shiba`**?**\
****When the compiler chooses a method, it **always** starts at the **static method.** Then, it keeps going down the inheritance tree until it hits the **dynamic method.** Since F has a **different signature** than D, it isn't an **overriding method** and thus the compiler won't see it. But E is (since it has the same signature as D), so that is why it is chosen instead.

![bork bork bork :DDD](<../img/assets/image (11).png>)
{{< /tab >}}
{{< /tabs >}}

## Adding more insanity: Static vs. Dynamic

By now, you should have a pretty good understanding of the **method selection** part of DMS. But why is it **dynamic?**

You may have noticed that there are **two** type specifiers in an instantiation. For example, `Dog s = new Shiba()` has type `Dog` on the left and `Shiba` on the right.

Here, `Dog` is the **static type** of `s`: it's what the compiler believes the type should be when the program is compiled. Since the program hasn't run yet, Java doesn't know what exactly it is- it just knows it has to be some type of `Dog`.

Conversely, `Shiba` is the **dynamic type:** it gets assigned during runtime.

### The type rules

Just remember: **like chooses like.** If a method is **static**, then choose the method from the **static type.** Likewise, if a method is **not static,** choose the corresponding method from the **dynamic type.**

Let's try some examples!

```java
public class Dog {
    public static String getType() {
        return "cute doggo";
 
    @Override // Remember, all objects extend Object class!   
    public String toString() {
        return getType();
    }
}

public class Shiba extends Dog {
    public static String getType() {
        return "shiba inu";
    }
}
```

{{< tabs "q5" >}}
{{< tab "Question 5" >}}
What prints out when we run:

```java
Dog d = new Shiba();
System.out.println(d.getType());
```
{{< /tab >}}

{{< tab "Q5 Answer" >}}
`cute doggo` gets printed because `getType()` is a static method! Therefore, Java looks at the **static type** of `d`, which is `Dog`. \
(If `getType()` weren't static, then `shiba inu` would have been printed as usual.)
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q6" >}}
{{< tab "Question 6" >}}
What prints out when we run:

```java
Shiba s = new Shiba();
System.out.println(s);
```
{{< /tab >}}

{{< tab "Q6 Answer" >}}
`cute doggo` also gets printed!! This is because static methods **cannot be overridden.** When `toString()` is called in `Dog`, it doesn't choose `Shiba`'s `getType()` because `getType()` is static and the static type is `Dog`.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q7" >}}
{{< tab "Question 7" >}}
What prints out when we run:

```java
Dog d = new Shiba();
System.out.println(((Shiba)d).getType());
```
{{< /tab >}}

{{< tab "Q7 Answer" >}}
This time, `shiba inu` gets printed. This is because casting temporarily changes the **static type:** since the static type of `d` is `Shiba` in line 2, it chooses the `getType()` from `Shiba`.
{{< /tab >}}
{{< /tabs >}}

## That's all, folks!

If you want some **even harder** problems, [check this out](https://inst.eecs.berkeley.edu/\~cs61b/sp20/materials/disc/examprep5.pdf) and also [this](https://inst.eecs.berkeley.edu/\~cs61b/sp20/materials/disc/examprep6.pdf).

![bai bai!](<../img/assets/image (12).png>)
