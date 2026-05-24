---
title: "Memory Management"
weight: 40
---

## Main

`int main(int argc, char *argv[])`

### Arguments

`argc` contains the **number of strings** inputted. The executable is one, and each argument is one.

`argv` is a pointer to an array with the argument strings. Can also be represented as `char **argv`

## Memory Management

![[/cs61c/img/Memory-Management/Untitled.png]]

### The Stack

The stack contains local variables (exist inside functions). 

- Grows from the top down
- Last in first out (LIFO)
- Memory is freed when the function returns.
- `main()` is treated like a function
- Automatic memory management: deleted without manual deletion
- A new **stack frame** gets created every time a new function is called
    - Return address (parent)
    - Arguments
    - Local variables

### The Heap

The heap contains memory that is specifically requested. It grows dynamically upwards.

We can work with the heap using the following commands:

- `void *malloc(size_t n)` allocates a block of uninitialized memory
    - Does not guarantee adjacent blocks if called multiple times
    - Returns a pointer to the block (or `NULL` if out of memory)
    - Usage: `int *p = (int *) malloc(sizeof(int));`
- `calloc()` allocates a block of zeroes
- `free(void *p)` frees a previously allocated block of memory
- `realloc(void *p, int size)` changes the size of a previously allocated block
    - If `*p` is `NULL`, then `realloc` acts like `malloc`

Heap Management errors: 

- **Memory Leak:** forgot to deallocate memory, resulting in inaccessible blocks that can't be cleared properly. Can lead to running out of memory
- **Double Free:** call free() twice on the same memory
- **Use after free:** attempt to access data after freeing it

### Static

**Static Data** includes all variables that are declared outside functions. This data is loaded at the start and cannot be modified.

**Code** is like static data in that it cannot be modified after the program is loaded. This includes `#define` symbols and function definitions.

## Endianness

Endianness is the order in which data is stored.

**Big Endian:** The first character is the most significant byte.

**Litle endian:** The first character is the least significant byte.

x86 is little endian, network communications are done in big endian.

## Alignment

For structs and other memory things where storing different types might need to be standardized, we have default alignment rules that are centered around the 32-bit architecture.

`int` needs to be **word aligned** (starts at multiples of 4).

`short` needs to be **half-word aligned** (starts at multiples of 2)

For example, if we have a struct with an `int, char, short, char*, char`:

- The int takes 4 bytes.
- The char takes 1 byte → now at 5.
- The short needs to be aligned to 6 → now at 8.
- The char* doesn't need to be aligned and takes 4 bytes → now at 12.
- The char doesn't need to be aligned → now at 13.
- At the end, we need to add 3 bytes to align it to 16.