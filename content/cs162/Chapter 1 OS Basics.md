---
title: "Chapter 1: OS Basics"
---

# What is an operating system?

An operating system has three main roles:

- **Referee:** The OS manages protection, isolation,  and allocation of resources between processes.
- **Illusionist:** The OS provides an abstraction between hardware and user programs that provides an illusion ****of easy-to-access resources such as files and available processors.
- **Glue:** The OS provides common services, sharing, authorization, networking, and communication between processes and external devices.

> Q1.1. Consider a modern web browser (such as Chrome or Firefox) which plays a similar role to an operating system. What considerations does a web browser need to make as a referee, illusionist, and glue?
> 

### Four Fundamental OS Concepts

The OS uses the four abstractions below to fulfill its roles:

1. **Threads** provide the basic unit of concurrency that fully describes a program.
2. **Processes** provide an execution environment for thread(s).
3. **Addresses** provide a way for threads and processes to access physical memory safely.
4. **Dual Mode Operation** provides a layer of privilege and security for running sensitive operations. 

Threads and processes will be covered in depth in future sections.

# The Kernel

One of the major requirements of an operating system is to provide **protection** from buggy or malicious programs. A design paradigm that allows for this is the **operating system kernel,** which is a fully trusted platform operating at the lowest software level of the system. This has several benefits:

- **Reliability:** Even if user programs crash, the kernel can still be running and handle the exception.
- **Security:** User programs must first interface through the kernel to request sensitive operations. The kernel can prevent malicious programs from executing undesired behavior.
- **Privacy:** The kernel facilitates what data can be transferred between user programs, so one program cannot read sensitive information from others.
- **Fair resource allocation:** The kernel can distribute computing power between user programs, so that one cannot block the others from executing.

The kernel is only a small portion of the entire operating system, since it is often beneficial to treat system libraries as user programs to allow for safer implementation.

## Dual Mode Operation

In order to provide protection, the kernel separates instructions into two main modes of execution: **kernel mode** (protected), and **user mode** (normal program execution). The mode is represented as a single state bit in hardware.

### Privileged Instructions

**Privileged instructions** are allowed only in kernel mode. These include changing memory access and handling interrupts, among other things. Attempting to execute privileged instructions in user mode will cause a **processor exception** that prompts the hardware to transfer control to an exception handler.

Typically, every process has two stacks, one for executing privileged instructions in kernel mode, and one for executing user code.

### Memory Protection: Base and Bound (B&B)

Base and Bound is a simple protection scheme for user address spaces, which allows for the operating system to allocate distinct chunks of memory for each program.

![Untitled](Chapter%201%20OS%20Basics/Untitled.png)

In this scheme, each program's address space has a **base** (where the data starts) and a **bound** (where the data ends).

- To translate from virtual to physical address spaces, the OS can add the base value to every address.
- If the address requested exceeds the bound, then an exception should occur.
- Implementing base and bound in software requires relocating the loader (because translation occurs during runtime).
- The primary benefit of Base and Bound is that it protects OS and isolates program without an addition to the address path (since you cannot physically access addresses outside of bounds).

### Mode Transfer

![Untitled](Chapter%201%20OS%20Basics/Untitled%201.png)

**There are three types of** **unprogrammed control transfer** from user mode to kernel mode:

1. **Syscalls:** When a process requests a system service (like `exit`), then save the requested syscall ID and arguments into registers, switch into kernel mode, and execute the syscall. Syscalls are similar to function calls, except that the function address is not given (so it cannot be exploited).
2. **Interrupts:** When external asynchronous events trigger a context switch, save the current execution state and jump to a kernel interrupt handler. Some common types of interrupts are **timer interrupts** (triggers at a specific time, typically to kill hung programs) and **IO interrupts** (e.g. triggers when a disk read completes). If multiple interrupts are queued, they are stored in an **interrupt vector** which alternates address of interrupt handler, and properties of the corresponding interrupt. Below is an illustration of an interrupt vector.
    
    ![Untitled](Chapter%201%20OS%20Basics/Untitled%202.png)
    
3. **Traps/Exceptions:** If a process triggers an internal hardware event, typically caused by undesired behavior, then execution stops and control is transferred to an exception handler in the kernel to allow the system to continue operating normally. Some examples include segfaults, read/write access violations, and divide by zero errors.
    
    

There are several types of control transfer from kernel mode to user mode:

- **Creating a new process:** the kernel copies the desired program into memory, sets the program counter to point to the first instruction, sets the stack pointer to the base of the user stack, and switches to user mode.
- **Resuming after an unprogrammed control transfer** (syscall, interrupt, exception): the kernel restores the program counter to its original user-mode state, restores the registers, and switches to user mode.
- **Switching to a different process**: the kernel saves the current process state in the process control block (PCB), and switches to user mode. The previous process can be resumed in the future.

# The Basic Problem of Concurrency

In hardware, we only have one of each resource (CPU, RAM, etc.) but in software, we have many processes that each need to believe they have exclusive access to hardware.

The OS needs to coordinate activity using a **multiprogramming API** and virtual machine abstraction.

**Properties of multiprogramming:**

- All virtual CPUs share the same non-CPU resources (IO, memory...)
- Every thread can access data and instructions for other threads (enables sharing, but bad for protection) but cannot overwrite OS functions
- To create protection, the OS must ensure processes don't access memory they should not be able to view (segfaults)

### Multiprocessing vs Multiprogramming

**Multiprocessing:** multiple CPUs

**Multiprogramming:** multiple processes

**Multithreading:** multiple threads

![Untitled](Chapter%201%20OS%20Basics/Untitled%203.png)

From the user's perspective, multiprocessing and multiprogramming can be indistinguishable.

**Concurrency is not parallelism:** concurrency is MTAO, parallelism is simultaneous.

- Two threads on one core is concurrent, but not parallel

### Addresses

- Every program has a distinct address space for execution (not physical address space).
- Depending on the address space, different actions can occur on read or write (nothing, regular behavior, ignore writes, IO, fault...)

![Untitled](Chapter%201%20OS%20Basics/Untitled%204.png)

---

# Solutions

Q1.1:

- Referee: Manage multiple tabs/webpages running simultaneously, handle tab switching, allocate computing resources to active tabs, prevent one buggy tab from crashing the entire browser.
- Illusionist: Even if webpages or parts of a page are served from many different servers or locations, all of the information is available in one place for the user.
- Glue: Provide a portable environment where webpages work on many different machines (computers, phones, different OS's...)