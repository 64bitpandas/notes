---
title: "CALL"
weight: 70
---

![[/cs61c/img/CALL/Untitled 2.png]]

## The Language Execution Continuum

![[/cs61c/img/CALL/Untitled.png]]

As languages get more high level, they tend to become easier to write but run more slowly.

An **interpreter** is a program that executes other programs. Higher level languages are less efficient to interpret since they optimize for readability or accessibility rather than performance.

One alternative to interpreting is **translation*,*** which is when a high level language is converted into a lower level language. 

Even machine code is worth interpreting for simulators and emulators (Apple silicon transition is a notable example).

### Interpretation vs Translation

- Generally, it is easier to write an interpreter.
- Interpreters can give better debugging and error information since the end result is more influenced by the high level language rather than a lower level language.
- Interpreters provide instruction set and platform independence.

Recently though, this distinction is becoming smaller and smaller with developments in JIT compilation (e.g. Java).

## The CALL Chain

**CALL stands for Compiler, Assembler, Loader, Linker.**

### The Compiler

The compiler takes in high level code as an input, and outputs assembly code.

The compiling step has multiple steps:

 - The **lexer** converts the input into tokens, and recognizes patterns and problems in the tokens.

 - The **parser** turns tokens into an **abstract syntax tree** that recognizes problems in the structure of the program itself.

 - **Semantic analysis and optimization** takes place, which may reorganize the code to improve efficiency, or recognize semantic errors.

 - **Code generation:** output the assembly code.

### The Assembler

The assembler takes in assembly code and outputs object code. 

Some tasks of the assembler:

- Use **directives:** instructions to assembler, but not direct machine instructions. For example:
    - `.text` directive tells the assembler to put items into the text segment.
    - `.data` tells the assembler to put items into the data segement.
    - `.globl sym` creates a label in global memory that is accessible from other files.
    - `.string str` creates a string and null-terminates it.
    - `.word w1...wn` stores 32-bit quantities in subsequent memory.
- Replaces pseudo-instructions
    - We can perform **tail call optimization** with the `tail` pseudoinstruction. This is usable when we have tail recursion, where after exiting a particular frame there is no information that needs to be tracked in that frame anymore. This means we can jump straight back to the original location rather than needing to jump back once for each frame that was opened.
- Creates object file, which contains the following information:
    - Object file header, the size and position of pieces of object file
    - Text segment, the machine code
    - Data segment, the binary representation of static data
    - Relocation information: code that needs to be processed later
    - Symbol table: list of file labels and static data
    - Debugging information: [http://www.skyfree.org/linux/references/ELF_Format.pdf](http://www.skyfree.org/linux/references/ELF_Format.pdf) (created with `gcc -g` to better map assembly to original code)
    

### Producing Machine Code

There are a number of things that need to be addressed when converting into machine code:

- Simple operations (arithmetic, etc): can be converted directly into a binary string.
- Branches and labels: these are PC-relative, so we need to figure out where in the program we will be in order to replace pseudo-instructions.
- The forward reference problem: Branches can either jump forwards or backwards in the code. We can fill out labels properly by going over the code in 2 passes. In the first pass, we keep track of the location of labels in the code. In the second pass, we actually convert those labels into positions since we know all of them already.
- Jumps and references to static data: If we have items that need to be accessible to/from other files, we can create a **symbol table,** which is a list of items that may be accessed by other files. The `.globl` and `.data` directives are processed and stored.
- A **relocation table** is also created to list the items that this file needs to find later (external label jumps, data in static memory accessed by `la` and so on).

### The Linker

The linker takes in object code file(s) as input, and outputs executable code (`a.out`, etc). The process of combining several object files into one is what's known as **linking.**

![[/cs61c/img/CALL/Untitled 3.png]]

Steps that the linker follows:

1. Combine all text segments
2. Combine all data segments
3. Resolve references: go through the relocation table and fill in absolute addresses now that we have the final binary and know where everything will be located.

There are three types of addresses:

1. PC-relative addressing (`beq` `bne` `jal`): never relocate.
2. External function reference (`jal`): always relocate.
3. Static data reference (`auipc` `addi`): always relocate.

Resolving References:

- The linker assumes that the first word of the first text segment is at the address `0x04000000`.
- The linker knows the length of each segment, and the ordering. It needs to calculate the absolute address of each label and piece of data.
- To resolve references, the linker will search for references in the program symbol tables. If it can't be found, then the linker will search library files.

### The Loader

The loader loads executable binaries into memory and begins the execution. It doesn't necessarily create another code file; rather, it performs actions based on what the code is supposed to do.

Typically, the loader is a component of the OS. 

Tasks that the loader performs:

- Read executable header (size and location of text and data segments)
- Creates address space and allocates stack memory to store the program and its information
- Copies information and data from executable into address space
- Copies arguments onto the stack
- Initializes machine registers: clears previous data, then assigns stack pointer
- Sets PC
- Jumps to start routine and steps through program
- If main routine returns, the program is terminated with an exit call

## Dynamically Linked Libraries

The CALL stack described above runs on *statically linked libraries,* in which any libraries that need to be accessed are stored in the program. This keeps things simple at the expense of memory and redundancy. 

The alternative is dynamically linked libraries, where libraries are accessed at runtime rather than during linking. This can be seen in OS's (`.dll`, `.so`)... and allow the same library code to be used by multiple programs at the same time. However, this makes things significantly more complex, loading takes longer, and having the executable itself is generally not enough to actually run the program. 

DLL's also sometimes randomize the layout (where external addresses are stored, etc) to make memory exploits significantly harder to pull off.