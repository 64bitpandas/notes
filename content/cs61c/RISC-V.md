---
title: "RISC-V"
weight: 60
---

# Quick Reference

[[RISC-V Quick Reference]]

# Intro to Assembly Language

![[/cs61c/img/RISC-V/Untitled.png]]

Assembly Language is one level closer to the hardware than most programming languages. It has human-readable instructions (add, etc), which directly correspond to numerical representations in machine code.

## Instruction Set Architecture (ISA)

The job of a CPU is to execute **instructions,** which are primitive operations. Each instruction is simple and does a small amount of work, but if we chain together many instructions, we can create a program.

CPU's belong to families with their own sets of instructions (these are the ISAs). Common examples are: ARM, x86, MIPS, RISC-V.

There are two main philosophies for instruction sets: **RISC (Reduced Instruction Set Computing)** and **CISC** (complex instruction set computing).

## Assembly Language Programming

Although high-level programming languages are certainly more convenient and feature-rich, assembly has the potential to be far more efficient. As compilers get better and better though, assembly is no longer as necessary as it used to be.

Each assembly is tied to a particular ISA.

Additionally, one major benefit of assembly is that it is **consistent**- in other words, all assembly code can easily be translated into binary strings without the need to make assumptions. Every operation has a machine code equivalent.

### Registers

Assembly language doesn't have variables like higher level programming languages. Instead, assembly uses **registers,** which are memory addresses stored directly in the CPU.

There are only a **limited number of spaces** (since we don't have infinite memory). In RISC, we can only perform arithmetic operations on registers. (CISC allows pointer operations additionally). This is one of the major drawbacks of assembly.

![[/cs61c/img/RISC-V/screenshot-2021-02-04_113606.png]]

**Smaller is faster.** Registers store far less memory (often measured in bytes) than DRAM (often measured in GB). However, they can be 100-500 times faster to access than DRAM.

**No data types.** Everything is just bits; at the assembly level, type information is not stored.

Recall how memory is stored:

- 8 bits make a byte.
- One word is 4 bytes.
- Word addresses are the rightmost byte of a word, and are 4 bytes apart.

### The State of the Computer

At its core, a computer program's state is made up of 3 things:

1. Where in the program we are (PC, the Program Counter)
2. The local variables (registers)
3. States that persist across functions (memory)

# RISC-V

![[/cs61c/img/RISC-V/Untitled 1.png]]

The complete RISC-V 32I ISA

RISC-V is a simple, royalty-free instruction set that has many applications from microcontrollers to supercomputers. 

RISC-V has **32 registers** (x0 to x31). x0 always holds the value 0 and can only be read, not written (so only 31 registers actually usable). Each register has **32 bits** (64 in some other machines).

Integers must be aligned on 4-byte boundaries. While this is technically not *required*, unaligned integers are very slow to process and lack *atomicity* (simple divisibility) which introduces bugs. 

Most data is split into words: 32-bit chunks. Each register is one word long, operations are also one word long, and `lw`, `sw` each load or store one word at a time.

RISC-V is **little endian:** the least significant byte is the smallest address.

### Syntax

RISC-V instructions have an **opcode** (instruction name) and **operands** (typically registers to access).

For example: `add x1, x2, x3` will sum the values held in the registers `x2`, and `x3` then saves it in the register `x1`.

### Immediates

**Immediates** are used to provide numerical constants to instructions. We need to use a new opcode to use them: for example, `addi x3, x4, -10` adds the constant -10 value to x4 and stores it in x3.

We can use this to copy registers: `addi x3, x4, 0` copies the value of `x4` to `x3`.

### No-ops

A **no-op** is an instruction that does nothing. These are useful because:

- They can fill space to align data.
- We might need to replace code later.
- It increments a counter.

To do a no-op in RISC-V, we can use `ADDI x0, x0, 0` to per form a NOP. 

### Data Transfer

How do we transfer memory between registers and DRAM? 

We can use the `lw` (load word) keyword to get data stored at a particular address, and `sw` (store word) to save data to a register: `lw x1 12 (x13)` or 

To load and store bytes, we can use `lb` and `sb` in the same format as `lw, sw`.  

As an example, what happens if we run:

```wasm
addi x11, x0, 0x8f5
sw x11, 0 (x5)
lb x12, 1 (x5)
```

First, we'd store `0x8f5` into `x11`.

Then, we would store a *word* into `x11`, which would sign extend and write `0xfffff8f5` (since `8f5` starts with a leading 1).

Finally, we would load `x12` shifted by 1 byte, which would leave us with `0xf8`. However, this would *also* need to be sign extended and therefore `0xfffffff8` is the final result. (if we did `lbu` instead, then it would have just returned `0xf8` due to lack of sign extension). 

### Bit Twiddling

RISC-V supports standard bit operations:

![[/cs61c/img/RISC-V/Untitled 2.png]]

We can also append `i` to the end of these instructions to handle operations with constants.

### Control Flows

RISC-V doesn't support standard `if for while` etc. that high level languages do, but we can:

- `beq register1, register2, L1`: **branch if equals**- go to instruction `L1` if the two registers have equal value.
- `bne register1, register2, L1`: **branch not equal**- runs `L1` if the two registers are not equal (opposite of `beq`).
- `blt`, `bge`: **branch less than, branch greater than or equal:** Usage same as above.
- `bltu`, `bgeu`: unsigned versions of `blt`, `bge`.

Here's a for loop in RISC-V:

```python
add x3 x0 x0
j check # Jump to check instruction

loop_start:
	... # code here

addi x3 x3 1 # Increments x3 by 1
check:
	li x4 10 # loads constant 10 into x4. Equivalent to addi x3 x0 10
	blt x3 x4 loop_start # If x3 < x4, run loop_start
```

RISC-V has unconditional branches (jumps):

- `jal rd offset`: **jump and link**: Store the next instruction `rd` after the jump to `offset`. `j offset` is a pseudoinstruction which is equivalent to `jal x0 offset`.
    - Example: `jal ra, foo` will jump to the `foo` instruction after setting `ra` to point to the current function.
- `jalr rd rs (offset)`: **jump and link register:** same as `jal`, except the destination is `rs + immediate`. `jr rs` is a pseudoinstruction for `jalr x0 rs`.
    - Example: `jalr s1` will go to the function pointed to by the address stored in `s1`.

### Pseudoinstructions

These instructions expand to larger instructions depending on the context.

![[/cs61c/img/RISC-V/Untitled 3.png]]

![[/cs61c/img/RISC-V/Untitled 4.png]]

### Program Execution

RISC-V instructions are stored in chunks of 32 bits. 

There exists a **program counter** (PC) that keeps track of where in execution we are.

The **Application Binary Interface** (ABI) defines our "calling convention": rules that all function calls must follow. Here's a chart of register names (no more `x0`, `x5`, etc.):

![[/cs61c/img/RISC-V/Untitled 5.png]]

- Saved registers are ones where it should be guaranteed that a callee function will not tamper with. It should be in the same state before and after any given call.
- `a0, a1` are reserved for return values.
- `ra` A return address pointing to the point of origin.
- `sp` points to the bottom of the stack.
- `fp` points to the top of the call frame. It's also known as `s0`, the first saved registers.

**Six fundamental steps in calling a function**

1. Put paramters in a place where the function can access them.
2. Transfer control to the function.
3. Get local storage needed for the function.
4. Run the function itself.
5. Put the result of the call in a place where the calling code can access it.
6. Return control to the origin.

Here's an example of a function in RISC-V: (translated from C)

![[/cs61c/img/RISC-V/Untitled 6.png]]

We can see that just like in C, we can think about a function call operating in a stack. We need to push things to the stack to operate on them, then pop them when we're done.

## Instruction Formats

Now, let's see how RISC-V represents assembly code in terms of machine code (going down one lvel).

### Instructions as Numbers

Each 32-bit instruction word is divided into **fields.** Each field tells the processor something about the instruction.

There isn't a one-size-fits-all field division, so instead there are a number of standards that instructions can be one of.

### Summary of RISC-V Instruction Formats

- **R:** register-register arithmetic and logical operations
- **I:** register-immediate ALU operations
- **S:** stores
- **B:** branches
- **U:** upper immediate instructions
- **J:** jumps

![[/cs61c/img/RISC-V/Untitled 7.png]]

### R-Format Instructions

- **Opcode:** a 7-bit field that contains the actual instruction.
    - All R-format instructions have an opcode of `0b0110011`.
- **rs:** Register source. Contains info about the registers being accessed.
- **rd:** Register destination. Where the result of the instruction should be stored.
- **funct:** Further describe what operation we need to perform (sometimes, the same opcode can correspond to multiple instructions).

![[/cs61c/img/RISC-V/Untitled 8.png]]

### I-Format Instructions

![[/cs61c/img/RISC-V/Untitled 9.png]]

Functions involving constant values generally use the I-format. Overall, this is very similar to the R-format, except `rs2` and `funct7` are replaced with the `imm[11:0]` 12-bit signed immediate.

The opcode for I-format is `0010011`.

This immediate size is large enough to accommodate the range `[-2048, +2047]` using the Two's Complement representation.

Immediates are always sign-extended to 32 bits before use in arithmetic operations.

![[/cs61c/img/RISC-V/Untitled 10.png]]

`shamt` is the shift amount: since shifts are limited to 32 bits max, the higher order bits are used for differentiating logical vs arithmetic shifts.

**Loads** are also I-format instructions:

![[/cs61c/img/RISC-V/Untitled 11.png]]

### S-Format Instructions

![[/cs61c/img/RISC-V/Untitled 12.png]]

S-format is used for **stores**: 

- `sb r2, offset(r1)`
- `rs2` is the source register, and `rs1` is the base register.
- There is no write to the register file (no rd).
- `imm[4:0]` and `imm[11:5` combine to represent the offset from `rs1` to store.
- The opcode is `0100011`.

![[/cs61c/img/RISC-V/Untitled 13.png]]

SB: store byte

SH: store half-word

SW: store word

### B-Format Instructions

B-format is used for branching: reading (but not writing) from two registers to do some logic. Branches are normally used for loops. 

![[/cs61c/img/RISC-V/Untitled 14.png]]

The destination of the branch uses **PC-Relative Addressing:** the immediate field stores the two's complement offset relative to the PC. The branch offset is scaled by 2 bytes (to accommodate the possibility of half-word, 16-bit instructions).

The opcode is `1100011`.

**If we don't take the branch:** PC increments by 4.

**If we do take the branch:** PC increments by the immediate (the number of bytes to jump, multiplied by 2). In other words, the immediate represents the values `-4096` to `4094` in 2-byte increments. There is an implicit 0 in the front of the immediate.

One limitation of B-format instructions is that the jump range is limited to `2^{10}`: if we need to jump a further amount, we must defer to a `j` instruction.

![[/cs61c/img/RISC-V/Untitled 15.png]]

![[/cs61c/img/RISC-V/Untitled 16.png]]

### U-Format Instructions

Upper Immediate instructions: contains a 20-bit immediate rather than the 12 that a normal I-format instruction has. The most useful opcode is `LUI` which loads the 20 bits into a specified destination register. We can then `ADDI` referencing the destination register in addition to a literal immediate.

In RISC-V, there is a `LI` pseudoinstruction that expands to these two instructions done in order. 

This can have some strange behaviors though: `ADDI` extends the 20 bits stored in the register with the 12 bits of the passed in immediate. However, sign-extension might mangle the end of the `LUI` value.

As an example, `li x10, 0xDEADBEEF` expands to `lui x10, 0xDEADC` then `addi x10, x10, 0xEEF`.

Some specifics:

LUI:  Load Upper Immediate: `lui rd, immediate`

- Sets `rd` to a 32-bit value, where the upper 20 bits are `immediate` and the lower 12 are `0`
- Absolute addressing
- First sub-instruction of `la`: `lui x1, <hi20bits>` then `jalr ra, x1, <lo12bits>`

AUIPC: add upper immediate to PC: `auipc rd, immediate`

- Sets `rd` to `PC` + {upper 20 bits of `immediate` with 12 lower 0's}
- Addresses relative to the PC
- Jump PC-relative with 32-bit offset: `auipc x1, <hi20bits>` then  `jalr x0, x1, <lo12bits>`

### J-Format Instructions

![[/cs61c/img/RISC-V/Untitled 17.png]]

J-Format instructions are used for jumps. 

For example: `JALR rd, rs, immediate`:

- writes PC + 4 to the destination rd
- sets PC to rs + immediate

Pseudoinstructions: `ret = jr ra = jalr x0, ra, 0`

## Multiplication and Division

In RISC-V, we multiply register values, but this will create a 64-bit value (since registers are 32-bit each). So, a product must be stored in two registers (one for upper, one for lower).

Additionally, multiplication is not in standard RISC-V, it is an extra.

**Syntax:** 

As convention, the following calls should be done in this order. This way, the hardware only carries out one multiplication or division and reuses the result for multiple calls.

```python
mul rd, rs1, rs2 # places lower 32 bits into rd
mulh rd, rs1, rs2 # places upper 32 bits into rd'

div rd, rs1, rs2 # divides rs1 by rs2 and saves quotient into rd
rem rd, rs1, rs2 # modulo function
```