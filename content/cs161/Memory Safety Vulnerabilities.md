---
title: "Memory Safety Vulnerabilities"
weight: 30
---

# Buffer Overflow Attacks

## out-of-bounds write

Overwriting bytes in a later position by making the current value much larger than anticipated. 

- This works because C doesn't check memory boundaries.
- Vulnerable code: `gets()` writes bytes until it encounters a newline. If there's no newline, then it may overwrite far more than intended.
- The following is an example. Attackers can simply write 21 ones into `name` and write a 1 into `authenticated`, thus logging in.

```c
char name[20];
int authenticated = 0;

void bad(void) {
	...
	gets(name);
  ...
}
```

## Stack Smashing

When overflows overwrite RIP to jump to a new address and run a custom script.

- Most common type of buffer overflow
- Python style ASCII note: `\x` means hex. So `\x41 == 'A'` for example
- **x86 is little endian** so the addresses need to be broken up. If we wanted to store `0xdeadbeef` into an address, it would look like `\xef\xbe\xad\xde`.

Steps for stack smashing attack:

1. Find a memory safety vulnerability
2. Write malicious shellcode (runs a shell script) at a known memory address
3. Overwrite RIP with address of shellcode
4. Return from original function (will execute shellcode)

Three methods of stack smashing placement:

![[/cs161/img/Memory-Safety-Vulnerabilities/Untitled.png]]

![[/cs161/img/Memory-Safety-Vulnerabilities/Untitled 1.png]]

![[/cs161/img/Memory-Safety-Vulnerabilities/Untitled 2.png]]

## Memory-Safe Code

- Rather than using `gets`,  use `fgets` which allows you to specify a maximum size.
- Use `strncpy` (more compatible, less safe) or `strlcpy` (less compatible, more safe) instead of `strcpy`
- Use `strnlen` instead of `strlen`
- tl;dr **use boundary checking!**

## Signed/Unsigned Vulnerability

Observe this code:

```c
void f(int len, char *data) {
  char buf[64];
	memcpy(buf, data, len);
}
```

`len` is signed, but `memcpy` takes in a `size_t` which is **unsigned.** Therefore, if an attacker passes in a negative number to `len`, it will be cast to a very large positive number and lots of data will be dumped.

## Integer Overflow Vulnerability

If we pass in a `int len` and then `malloc(len + n)` where `n` is any positive number, then we would enable an integer overflow. If an attacker passes in `0xFFFFFFFF`, then malloc will overflow the heap.

The way to fix this vulnerability is to add a check for `if(len > SIZE_MAX - n)` before proceeding.

## String Format Vulnerabilities

If the arguments into `printf` are mismatched, undesired behavior may occur

Example: `printf("%d\n");` without a second integer argument will cause printf to look 4 bytes up the stack anyways and print whatever was there before (could be secrets)

![[/cs161/img/Memory-Safety-Vulnerabilities/Untitled 3.png]]

`printf("%s")` will look 8 bytes above the RIP of printf and continue printing until a null byte is reached.

`%n` treats the next argument as a pointer and writes the number of bytes printed into that address. For example, `printf("item %d:%n", 987, &val)` will write 9 bytes into `&val` (item = 4, space = 1, colon = 1, 987 = 3)

**Defending Against String Format Vulnerabilities:**

- Hard-code all string formats so user can't exploit with input
- Sanitize inputs to remove all formatting