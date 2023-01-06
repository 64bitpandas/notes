# Asymptotics Practice

> [!info] Content Note
>
> Make sure to review [Asymptotic Analysis Basics](asymptotics.md) before proceeding with these problems.

## Introduction

Asymptotics is a very intuition-based concept that often doesn't have a set algorithm for computing. The best way to get good at analyzing programs is to practice!

With that said, here are some problems of increasing difficulty for you to enjoy 😊

> [!hint] Read before you do the problems!
>
> For all of the below problems, assume that all undefined functions have a constant O(1) complexity.

## Loops

{{< tabs "q1" >}}
{{< tab "Question 1" >}}
What runtime does this function have?

```java
void throwHalfOfMyItems(int n) {
    for (int i = 0; i < n; i += 1) {
        if (i % 2 == 0)
            throwItem(n);
    }
}
```
{{< /tab >}}

{{< tab "Q1 Answer" >}}
$
\Theta(n)
$

**Explanation:** The method `throwItem()` runs `n/2` times. Using the simplification rules, we can extract the constant `1/2` to simply get `n`.

![Keep the change, ya filthy animal.](<../img/assets/image (40).png>)
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q2a" >}}
{{< tab "Question 2a" >}}
What runtime does this function have?

```java
void lootShulkerBoxes(int n) {
    for (int box = n; box > 0; box -= 1) {
        for (int stack = 0; stack < n; stack += 1) {
            for (int i = 0; i < 64; i += 1) {
                lootItem(i * stack * box);
            }
        }
    }       
}
```
{{< /tab >}}

{{< tab "Q2a Answer" >}}
$
\Theta(n^2)
$

**Explanation:** There are **three** nested loops in this problem. Whenever there are nested loops whose runtimes are independent of each other, we need to **multiply** the runtimes in each loop.\
So, we get: $\Theta(n * n * 64)$ which simplifies into `n^2`

![That's a lot of items to loot...](<../img/assets/image (41).png>)
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q2b" >}}
{{< tab "Question 2b" >}}
I've tweaked the previous problem a little 😁 Try to spot the difference and see if it changes the runtime at all!

```java
void lootShulkerBoxes(int n, int stacksToLoot) {
    for (int box = n; box > 0; box -= 1) {
        for (int stack = stacksToLoot; stack > 0; stack -= 1) {
            for (int i = 0; i < 64; i += 1) {
                lootItem(i * stack * box);
            }
        }
    }       
}
```
{{< /tab >}}

{{< tab "Q2b Answer" >}}
$
\Theta(n)
$

**Explanation:** Even though `stacksToLoot` is a user input, we're only concerned about finding the runtime for `n` so `stacksToLoot` can be treated like a constant! Therefore, we now have $\Theta(n * s* 64)$ where `s = stacksToLoot` which simplifies into `n`.

![ok now this is getting a bit overboard](<../img/assets/image (42).png>)
{{< /tab >}}
{{< /tabs >}}

## Recursion

The following two problems are inspired by [this worksheet](https://inst.eecs.berkeley.edu/\~cs61b/sp20/materials/disc/discussion8.pdf).

{{< tabs "q3" >}}
{{< tab "Question 3" >}}
TREEEEEEEEE recursion 🌳🌲🌴

```java
void plantJungleSaplings(int n) {
    if (n > 0) {
        for (int i = 0; i < 4; i += 1) {
            plantJungleSaplings(n - 1);
        }
    }
}
```
{{< /tab >}}

{{< tab "Q3 Answer" >}}
$
\Theta(4^n)
$

**Explanation:** This tree recursion creates a tree with `n` layers. Each layer you go down, the number of calls multiplies by 4!

![Tree diagram for method calls.](<../img/assets/image (48).png>)

This means that the number of calls in total will look like this:

$
\sum_{i=1}^{n}4^i
$

And if you remember your power series, you'll know that this sum is equal to $4^{n+1}-1$ which simplifies into the final answer.

![an image that makes you long for TreeCapacitator](<../img/assets/image (49).png>)
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q4" >}}
{{< tab "Question 4" >}}
Let's replace the 4 in the previous problem with **n** and see what insanity ensues.

```java
void plantCrazySaplings(int n) {
    if (n > 0) {
        for (int i = 0; i < n; i += 1) { // This line changed
            plantCrazySaplings(n - 1);
        }
    }
}
```
{{< /tab >}}

{{< tab "Q4 Answer" >}}
$
\Theta(n!)
$

**Explanation:** This tree recursion creates a tree with `n` layers. Each layer you go down, the number of calls multiplies by `n-1`...

![What a mess (!)](<../img/assets/image (51).png>)

This means that the number of calls in total will look like this:

$
\sum_{i=1}^{n} \frac{n!}{i!}
$

Since `n!` is not dependent on `i` it can be factored out of the sum to produce this:

$
n!\sum_{i=1}^{n} \frac{1}{i!}
$

Hey, that looks a lot like the Taylor series for $e$! Since `e` is a constant, it simply reduces to `n!`.
{{< /tab >}}
{{< /tabs >}}

## Best and Worst Case Runtimes

{{< tabs "q5" >}}
{{< tab "Question 5" >}}
Here's a case where the best case and worst case runtimes are different. Can you figure out what they are? (Let `n = items.length`).

```java
Item[] hopperSort(Item[] items) {
    int n = arr.length; 
    for (int i = 1; i < n; ++i) { 
        int key = items[i]; 
        int j = i - 1; 
        while (j >= 0 && items[j].compareTo(key) > 0) { 
            items[j + 1] = items[j]; 
            j = j - 1; 
        } 
        items[j + 1] = key; 
    } 
}
```
{{< /tab >}}

{{< tab "Q5 Answer" >}}
**Best Case:** $\Theta(n)$ if the array is nearly sorted except for a couple values. In this case, the `while` loop will only run a small number of times, so the only loop left is the for loop.

**Worst Case:** $\Theta(n^2)$if the array is totally reversed. This will cause the `while` loop to run on the order of `O(n)` times, resulting in a nested loop.

**Note:** HopperSort is literally just Insertion Sort 😎🤣

![hoppers rate 64/64](<../img/assets/image (45).png>)
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q6" >}}
{{< tab "Question 6" >}}
Here's a mutual recursion problem! What are the best and worst cases for `explodeTNT(n)`? What are their runtimes?

```java
void explodeTNT(int n) {
    if (n % 2 == 0) {
        digDirts(n - 1, true);
        digDirts(n - 2, false);
    } else {
        digDirts(n / 2, true);
    }
}

void digDirts(int n, boolean isTNT) {
    if (isTNT) {
        explodeTNT(n / 2);
    }
    removeDirt(); // not implemented, assume O(1) runtime
}
```
{{< /tab >}}

{{< tab "Q6 Answer" >}}
**Best Case:** $\Theta(\log(n))$ if n is even. This will result in n being halved every function call.

**Worst Case:** $\Theta(n)$if n is odd. See the tree below for an illustration of what happens in this case- hopefully the diagram will make it clearer as to why it's O(n).

![A diagram of what happens in the worst and best cases.](<../img/assets/image (46).png>)

![don't play with tnt, kids](<../img/assets/image (47).png>)
{{< /tab >}}
{{< /tabs >}}

## Challenge Problems

These problems are quite difficult. Don't be concerned if you don't feel confident in solving them (I certainly don't).

{{< tabs "q7" >}}
{{< tab "Question 7" >}}
A huge disaster :ooo

```java
//initially start is 0, end is arr.length.
public int PNH(char[] arr, int start, int end) {
    if (end <= start) {
        return 1;
    }
    int counter = 0; 
    int result = 0;
    for (int i = start; i < end; i += 1) {
        if (arr[i] == 'a') {
            counter += 1;
        }
    }
    for (int i = 0; i < counter; i += 1) {
        result += PNH(arr, start + 1, end);
    }
    int mid = start + (end - start) / 2;
    return PNH(arr, start, mid) + PNH(arr, mid + 1, end);
}
```
{{< /tab >}}

{{< tab "Q7 Answer" >}}
**Best Case:** $\Theta(n\log(n))$ If none of the characters in char\[] is 'a', then each call to PNH does $\Theta(n)$ work. Total work per layer is always N, with logN layers total.

**Worst Case:** $\Theta(n!)$ All of characters in char\[] is 'a'. In this case, the for loop recursive calls will dominate the runtime, because it'll be the main part of the recursive tree. The interval start to end is decreased by one in the for loop recursive calls, while that interval is halved in the return statement recursive calls. This means the return statement recursive calls will reach the base case in logn levels, while the recursive calls in the for loop will take n levels. Thus, we can proceed with the same analysis as question 4.
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q8" >}}
{{< tab "Question 8" >}}
Congrats for making it this far! By now you should be an expert in asymptotic analysis :P Here's one last problem:

```java
//initially start is 0, end is arr.length.
public int lastOne(char[] arr, int start, int end) {
    if (end <= start) {
        return 1;
    }
    else if (arr[start] <= arr[end]) {
        return lastOne(arr, start + 1, end - 1);
    } else {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        return lastOne(arr, start + 1, end) 
        + lastOne(arr, start, end - 1) 
        + lastOne(arr, start + 1, end - 1);
    }
}
```
{{< /tab >}}

{{< tab "Q8 Answer" >}}
**Best Case:** $\Theta(n)$ if the else if case is always true. This will produce a tree with height n/2, where each height does constant work.

**Worst Case:** $\Theta(3^n)$ if else if case is never true. Sorry no diagram yet :((
{{< /tab >}}
{{< /tabs >}}
