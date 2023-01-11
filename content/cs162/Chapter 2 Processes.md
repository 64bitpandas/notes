---
title: "Chapter 2: Processes"
---

# The Process Abstraction

A **process** is an execution environment with restricted rights. 

A process consists of:

- An address space
- Thread(s) of control running in that address space
- System states associated with threads (files, etc)

The process abstraction creates a tradeoff between protection and efficiency: communication is easier *within* processes, but harder *between* processes.

# UNIX Process Management

## Creating Processes: fork and exec

### Forking

In UNIX-based systems, the primary way to create new processes is to **fork** an existing process. This creates a child process with a single thread, and copies all code and resources available to the parent process at that point in time.

Forking can be done with the C library function `pid_t fork()`. `fork` returns a process ID (pid) that allows us to identify which process is currently running: 

- When `pid > 0`, then we are in the parent process, and a new child process was created here.
- When `pid = 0`, then we are currently inside of a child process that was just created.
- When `pid < 0`, an error occurred in the original process and no new processes were created.

When `fork` is called, the following operations are carried out by the kernel:

1. Create and initialize the process control block (PCB)
2. Create and initialize a new address space
3. Copy over the contents of the parent processes' address space
4. Copy over the execution context of the parent, including the program counter and open files
5. Mark the new process as ready

### **Forking Pitfalls**

- **Don't fork in a multithreaded process!** Fork only copies one thread, so any other threads will vanish. (The exception to this rule is if `exec` is called within the child process, since this replaces the entire process anyways and the destruction of threads is desired.)
- **Parent and child processes work with entirely separate address spaces.** For example, take the code below:
    
    ```c
    int main(void) {
    	int* alligator = malloc(sizeof(int));
    	*alligator = 3;
    	pid_t pid = fork();
    	printf("%d"\n, *alligator);
    	if (pid == 0) { // this runs inside child process
    		*alligator = 100;
    	}
    	return 0;
    }
    ```
    
    Even though we cannot guarantee which order the parent and child processes run in, we can say with certainty that two `3`'s will be printed. This is because the parent and child processes operate on a different stack and heap space, so even if `*alligator` is set to `100` in the child process before the parent process can execute, the parent process still accesses its own version of `alligator` which remains unchanged.
    

### Exec

What if instead of copying a process, we wanted to create a whole new, unrelated one that does something different? 

This is where the `exec` family of functions comes in. These functions consist of:

- `int execl(const char *path, const char *arg, ...);`
- `int execlp(const char *file, const char *arg, ...);`
- `int execle(const char *path, const char *arg, ..., char * const envp[]);`
- `int execv(const char *path, char *const argv[]);`
- `int execvp(const char *file, char *const argv[]);`
- `int execvpe(const char *file, char *const argv[], char *const envp[]);`

The parameters passed in represent:

1. The program that should be executed (in a string format to its file path), such as `/usr/bin/ls`
2. Any arguments that should be passed into the program. The `execl` family takes in a list of strings as arguments, whereas the `execv` family takes in one array of strings as arguments.

Some of the functions have special behaviors:

- The `execlp` and `execvp` functions search the system's PATH variable (which contains typical locations for executables, like `/usr/bin`) so that you do not need to pass in the full path every time. For example, `execvp("ls")` should work fine, even if `ls` is not inside of the current directory.
- The `execle` and `execvpe` functions allow specifying custom locations to search for executables in addition to PATH.

### Wait

The `wait` syscall pauses the parent process until the child process finishes running or is otherwise terminated. In C, this syscall can be made with the following function:

`pid_t wait(int *wstatus)`

Here, `*wstatus` is a pointer to some integer variable. When the child process completes, `wstatus` is set to the return value of the process.

As an example:

```c
int main(void) {
	pid_t pid = fork();
	int exit;
	if (pid != 0) {
		wait(&exit);
	}
	printf("%d\n", pid);
}
```

The following code will print `0`, then whatever the child process PID was. This is because the parent must wait until the child process executes in its entirety before continuing from line 5 (wait).

There is also the `pid_t waitpid(pid_t pid, int *status, int options)` function, which waits for a specific child process to terminate rather than all child processes.

# Communication Between Processes

Typically, processes are protected from each other since they can only access their own portions of physical memory.

![Untitled](Chapter%202%20Processes/Untitled.png)

To circumvent this protection, there are several methods:

**Use a file.** Processes can share file descriptors.

- Simple, but very expensive for non-persistent communication

**Shared memory:** edit translation maps to support a special portion of shared address space

**POSIX Pipe:** finite memory buffer that can be written to and read from using `pipe`

- If producer tries to write when pipe is full, it gets blocked
- If consumer tries to read when pipe is empty, it gets blocked
- Implemented as a fixed-size queue
- EOF received when the last write descriptor is closed

**Threads are lighter (share data), processes are more strongly isolated**
