---
title: "Heap Vulnerabilities"
weight: 40
---

## C++ Vtables

C++ is an object oriented language that has polymorphism, instance variables, methods, etc.

To support these features, every class has a **vtable** (function pointer table). Each object then points to its vtable, where pointers can be dereferenced from.

![[/cs161/img/Heap-Vulnerabilities/Untitled.png]]

Vtables exist in the heap. Vulnerability: add shellcode and point to it

![[/cs161/img/Heap-Vulnerabilities/Untitled 1.png]]

## Heap Overflow

Objects are allocated in the heap (malloc), but writes to a buffer in the heap are not checked. Attackers can overflow the heap and overwrite the vtable pointer of the next object to point to a malicious vtable.

## Use After Free

If an object is deallocated too early, attackers can allocate the same memory and overwrite portions of it.

## Nop Sleds

Instead of needing to jump to the exact address of the code, attackers can add a large number of `nop` instructions so that running code near the desired location will lead to the code being run.