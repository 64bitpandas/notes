# Exceptions

## Basics

An **exception** occurs when something unintended occurs and the interpreter must exit.

While this might sound like a bad thing, we can often throw our own exceptions to handle known errors or edge cases more gracefully.

### Exceptions in Java

In Java, there are two types of exceptions: **checked** and **unchecked.**

**Checked** exceptions are handled during compile time, and are included in the method declaration. As an example:

```java
public void openFile() throws IOException {
    ...
}
```

* All children that override this method must also throw the same exceptions.

**Unchecked** exceptions are not handled during compile time, and thus are thrown during runtime. All `Error` or `RuntimeException` types are unchecked; all other exceptions are checked. Some examples of unchecked exceptions are dividing by zero (`ArithmeticException`), or accessing an index that doesn't exist (`IndexOutOfBoundsException`).

![Some of the more common Exception types in Java.](<../img/assets/image (4).png>)

## Creating Custom Exceptions

We can use the `throw` keyword to create exceptions with custom error messages as follows:

```java
public void divide(int a, int b) {
    if (b == 0) {
        throw new Exception("Error Message");
    } else {
        return a / b;
    }
}
```

This is often used within a `try catch` block, as such:

```java
public void divide2() {
    int a = 0;
    try {
        return 10 / 0;
    } catch(Exception e) {
        System.out.println("oops!");
    }
 }
```

An alternate to custom exceptions is to simply handle exception cases. For example, we can add a check to make sure a number is not zero before running a division operation.

## Try/Catch/Finally Example

Let's check your understanding of exception handling!

```java
static String tryCatchFinally() {
        try {
            System.out.println("trying");
            throw new Exception();
        } catch (Exception e) {
            System.out.println("catching");
            return "done catch";
        } finally {
            System.out.println("finally");
        }
    }
```

{% tabs %}
{% tab title="Q1" %}
What will be printed (and in what order) when `tryCatchFinally()` is run?
{% endtab %}

{% tab title="Q1 Answer" %}
First, `trying` will be printed.

Since an Exception is thrown, the catch block will run next, so `catching` is printed next.

Since finally blocks _always_ run regardless of result, `finally` is printed last.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Q2" %}
Suppose the same code were run, but without the `catch` block. What would this code do?

```java
static String tryFinally() {
        try {
            System.out.println("trying");
            throw new Exception();
        } finally {
            System.out.println("finally");
        }
}
```
{% endtab %}

{% tab title="Q2 Answer" %}
If the try block throws an uncaught Exception (i.e. if catch block does not exist or catch block does not handle the type of Exception that is thrown in the try block), Java halts execution of the try block, **executes the finally block**, then raises a runtime error.\
\
So, the following sequence would occur:\
1\. `trying` is printed.\
2\. `finally` is printed.\
3\. The program exits with a `RuntimeException`.
{% endtab %}
{% endtabs %}
