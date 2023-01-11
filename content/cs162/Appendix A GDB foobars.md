---
title: "GDB Reference"
---

Run with args: `r <args>`

Breakpoint: `b <n>`

Conditional breakpoint: `b <n> if <condition>` or `condition <n> <condition>` on existing

Step into: `step` or `s` (`si` for assembly)

Step over: `next` or `n` (for assembly, `ni`)

See all registers: `info registers` (can also do `info frame`, `info args`, `info locals`)

View split mode: `ctrl+x ctrl+a`

Switch between code and assembly: `layout asm`, `layout src`. `Ctrl+X A` to exit split

View hex memory: `x <name>` or `x/Nx <name>` to view `N` bytes after name

Enable logging: `set logging on` , to change directory `set logging file`