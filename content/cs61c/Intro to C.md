---
title: "Intro to C"
weight: 20
---

![[/cs61c/img/Intro-to-C/Untitled.png]]

## C: The Universal Assembly Language

**What's the big deal with C?**

- **It's wildly popular.** C and its derivatives have been around for 40+ years and won't be going away anytime soon.
- **It's highly configurable.** Whatever you want to do, C can probably do it.
- **It's good if you have limited memory.** Microprocessors are best used when running C because memory allocation is a must when you only have like 4kb of RAM.

### Compilation

C compilers map programs directly into **machine code** (bitstrings). In comparison:

- Java has architecture-independent bytecode that uses a JIT compiler to run.
- Python converts a program to bytecode at runtime.

This means that compiled C programs are **architecture specific.** Individual C files are individually compiled, then combined using a **linker** which creates one unified output executable.

Before the compiler processes the code, the code first runs through the **C Pre-Processor (CPP).** Everything beginning in a '#' is a CPP macro (like `#include, #define..` ) 

- **These are not actual functions.** They simply change the **text** of the program before compilation! This can create really weird errors: for instance, if we `#define f(x) y++` then instead of creating a function that evaluates to `y++`, the CPP will rewrite all instances of `f(x)` into `y++` so you could get something like `y++ + y++`.

### Variables

![[/cs61c/img/Intro-to-C/Untitled 1.png]]

There are additionally different types of integers:

- `sizeof(long long) >= sizeof(long) >= sizeof(int) >= sizeof(short)`
- The actual size of any of these types are not guaranteed, except for `short` being at least 16 bits and `long` being at least 32 bits. In practice, all could actually be the same size.

To define a variable:

```c
int normalvar = 42;
const int constvar = 42;
enum colors {RED, GREEN, BLUE};

float do_the_thing (int x) {
	return 0.3;
}
```

Some important notes about variable declarations:

- **All variables must be declared before they can be used.** (same as Java)
- **All declarations must be at the beginning of a block.** (different from Java)
- **If a variable is declared but not initialized, it holds undefined garbage.**

### Structs

Since C predates OOP, standard objects don't exactly exist. Instead, we have **structs** which define properties for a variable:

```c
typedef struct thing {
	int stuff1;
	int stuff2;
	struct thing *next_thing;
} Thing;

Thing thing1;
thing1.stuff1 = 5;
thing1.stuff2 = 10;
...
```

A struct is just an instruction on how to arrange a bunch of bytes in a bucket. We can use `sizeof(struct foo)` to get the number of bytes used by `foo`.

### Unions

There are also **unions,** which are similar to structs except that it takes the same space as the **largest element.** (So if there were an `int` and `char` , a struct would take 5 bytes but a union would take only 4. Unions are like an **or** expression- the object is this or that (but not both)- whereas a struct is like an **and** expression- both this and that.

Unions can be used to create switchable types:

```c
enum FieldType {type1, type2, type3};
union test {
	char *a;
	int b;
}
struct foo {
	FieldType type;
	union bar data;
}

struct foo *f;
switch(f->type) {
	case type1:
		...
}
```

### Arrays

Arrays are **statically sized.** An array object is simply a pointer to the 0th element.

- To declare an array: `int ar[32]` makes a 32-integer array
- `char *string` is *almost* the same as `char string[]`
- Doing array operations is basically just doing pointer arithmetic but nicer: `a[i]` is similar to doing `*(a+i)` to access the `i`th element.

> ⚠️ **When an array is passed into a function,** **its size is lost.** Therefore, a size must be explicitly passed into the function as an integer in order to use this information.
>
> There is also **no check for bounds.** It is entirely possible to overwrite an unrelated piece of memory before/after an array if the length of the array is exceeded.

### Strings

A **string** in C is just an array of characters: `char string[] = "abc"`.

- The last character is followed by a **null terminator,** `0` or `\0`.
- To get the length of a string: (both are equivalent)

![[/cs61c/img/Intro-to-C/Untitled 2.png]]

**Copying a string:** Suppose we have a string `b` that we want to copy to `a`. Then,

```c
a = malloc(sizeof(char) * (strlen(b) + 1));
strcpy(a, b)
// alternative
strncpy(a, b, strlen(b) + 1);
```

Strings are **not immuable!** (except for constant strings which are global variables that cannot be written to)

**String/char functions:**

- getchar
- gets
- printf
- scanf

### Undefined Behavior

There are parts of C where the behavior is undefined. This means that the behavior is **unpredictable** and the compiler pretty much does whatever it wants. This can create issues like:

- programs running one way on one computer, and another way on another
- programs running differently each time
- programs running differently on different inputs