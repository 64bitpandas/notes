---
title: "Exam Problem Guide"
---

# Number Representation

- **Convert -29 to Two's Complement binary and -127 biased binary. (8 bits)**
    
    **Two's Complement:** 
    
    First, represent +29 in binary with an extra sign bit:
    
    `0b00011101`
    
    Now, negate all bits:
    
    `0b11100010`
    
    Add one:
    
    `0b11100011`
    
    **Biased:**
    
    First, add 127 to -29 to get 98.
    
    Represent 98 in binary:
    
    `0b01100010`
    

- **Number Representation Facts**
    
    A $n$ digit two-complement number stores $2^n$ negative numbers and $2^{n-1}$ positive numbers.
    
    ![[/cs61c/img/Exam-Problem-Guide/Untitled.png]]
    

- **Endianness**
    
    Supposing we have a 32-bit integer `a = 0xABCD_EFGH`. 
    
    If it was stored in **little endian,** the **least significant** 32-bit block is stored first. So, `a[3] = AB` and `a[0] = GH` .
    
    If it was stored in **big endian**, then **the most significant** 32-bit block is stored first. So, `a[0] = AB` and `a[3] = GH` .
    
- **Floating Point**
    
    ![[/cs61c/img/Exam-Problem-Guide/Untitled 2.png]]
    
    ![[/cs61c/img/Exam-Problem-Guide/Untitled 1.png]]
    
    **Example: convert 16.375 to binary.**
    
    1. Determine the whole number component (16 → 10000)
    2. Determine the fractional component (.375 = $\frac{1}{4} + \frac{1}{8}$ → 011)
    3. Shift the result over until it becomes the format 1.xxxxxx...
        
        10000.011 = 1.0000011 x $10^{4}$
        
    4. Encode the exponent by biasing it.
        
        $4 - (-127) = 131$ → 100011
        
    5. Remove the leading 1 and combine.
        
        `0b0 100011 0000011000000000000000000`
        
    
    **Denorm:**
    
    Denorm occurs when all exponent bits are 0 and the significant is nonzero. The denorm exponent is equal to `bias - 1`. 
    
    - The smallest possible denormalized number is $2^{implicit\ exponent} \times 2^{bits\ in\ mantissa}$.
    - Denormalized numbers do not have an implicit leading 1.

# C Basics

## Printf

![[/cs61c/img/Exam-Problem-Guide/Untitled 1.png]]

## Memory Locations

**Code:** 

- Functions, e.g. `main`
- `#define` symbols
- Pointers to functions, e.g. `&main`

**Stack:**

- Pointer addresses

**Heap:**

- Malloc, calloc, realloc
- Dereferenced pointer `*ptr` to an allocated space

**Static:**

- Constants
- Variables declared outside of functions
- Static strings `char *r = "foo"`

## **[Int Ranges](https://web.archive.org/web/20210730042130/https://clickhouse.tech/docs/en/sql-reference/data-types/int-uint/#int-ranges)**

- `Int8` — [-128 : 127]
- `Int16` — [-32768 : 32767]
- `Int32` — [-2147483648 : 2147483647]
- `Int64` — [-9223372036854775808 : 9223372036854775807]
- `Int128` — [-170141183460469231731687303715884105728 : 170141183460469231731687303715884105727]

## Arrays and Strings

Create a n-length array using `int arr[n]`.

Two ways to index: `x[i]` or `*(x+i)`

Ways to compute length of string: `strlen(a)` or `sizeof(a) - 1` or `len = 0; while (*a++) { ++len++;}`

Number of bytes in a string: `strlen(a) + 1`

String literals (`char* foo = "bar"`) are read only. Writing to them will cause an error

## Unions and Structs

Union size = size of the largest individual element in the union

Struct size = sum of all elements in the struct

## Pointer-foo

```c
// Arrow Notation //
Point p1;
Point p2;
Point *paddr = &p1;

int h = paddr -> x; // get x of object pointed to by paddr
int h = (*paddr).x; // same thing, but dereferenced
int h = p1.x; // gets the same exact value too

// Pointer equality demo //
int x = 1
int *p = &x
int *q = *p
p == q // FALSE, the pointers exist at different locations in memory
*p == *q // TRUE, p and q both point to x

// Pointers to addresses and functions //
char *foo(char *a, int b) {...} //function that takes in a string and integer
char *(*f)(char *, int) // pointer to a function that takes in string+int
f = &foo //assign foo to f
printf("%s\n", (*f)("cat", 3)) // call f 
```

# CALL

![[/cs61c/img/Exam-Problem-Guide/Untitled 2.png]]

### The Compiler

The compiler takes in high level code as an input, and outputs assembly code.

The compiling step has multiple steps:

 - The **lexer** converts the input into tokens, and recognizes patterns and problems in the tokens.

 - The **parser** turns tokens into an **abstract syntax tree** that recognizes problems in the structure of the program itself.

 - **Semantic analysis and optimization** takes place, which may reorganize the code to improve efficiency, or recognize semantic errors.

 - **Code generation:** output the assembly code.

The compiler also determines increment size for pointer arithmetic.

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
    - Debugging information: [ELF Format (archive.org)](https://web.archive.org/web/20231219125922/http://www.skyfree.org/linux/references/ELF_Format.pdf) (created with `gcc -g` to better map assembly to original code)

### Producing Machine Code

There are a number of things that need to be addressed when converting into machine code:

- Simple operations (arithmetic, etc): can be converted directly into a binary string.
- Branches and labels: these are PC-relative, so we need to figure out where in the program we will be in order to replace pseudo-instructions.
- The forward reference problem: Branches can either jump forwards or backwards in the code. We can fill out labels properly by going over the code in 2 passes. In the first pass, we keep track of the location of labels in the code. In the second pass, we actually convert those labels into positions since we know all of them already.
- Jumps and references to static data: If we have items that need to be accessible to/from other files, we can create a **symbol table,** which is a list of items that may be accessed by other files. The `.globl` and `.data` directives are processed and stored.
- A **relocation table** is also created to list the items that this file needs to find later (external label jumps, data in static memory accessed by `la` and so on).

### The Linker

The linker takes in object code file(s) as input, and outputs executable code (`a.out`, etc). The process of combining several object files into one is what's known as **linking.**

The linker primarily deals with statically linked libraries (external data) by copying it over.

![[/cs61c/img/Exam-Problem-Guide/Untitled 3.png]]

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
- Loads dynamically linked libraries
- Creates address space and allocates stack memory to store the program and its information
- Copies information and data from executable into address space
- Copies arguments onto the stack
- Initializes machine registers: clears previous data, then assigns stack pointer
- Sets PC
- Jumps to start routine and steps through program
- If main routine returns, the program is terminated with an exit call

# Hardware

![[/cs61c/img/Exam-Problem-Guide/Untitled 2.png]]

![[/cs61c/img/Exam-Problem-Guide/Untitled 5.png]]

**Period = CLK-to-Q Delay + CL Delay + Setup Time**

**Clock Frequency = 1 / Critical Path Period**

**Hold Time Violation:** When hold time is less than clk-to-Q + best case

# Datapath

![[/cs61c/img/Exam-Problem-Guide/Untitled 4.png]]

![[/cs61c/img/Exam-Problem-Guide/Untitled 5.png]]

**IF: Instruction Fetch -** looks into instruction memory (IMEM) and returns the machine code representation of the instruction at the program counter (PC)

**ID: Instruction Decode -** uses machine code instructions to figure out what registers we are reading or writing to. Also handles immediates and sign extension if necessary

**EX: Execute -** determines if a branch needs to be taken, OR computes logical instructions in the ALU

**MEM: Data Memory -** if we have a load or store instruction, then we will read from or write to our memory (DMEM)

**WB: Writeback -** determines the value that will be written back to the destination register