---
title: "RISC-V Quick Reference"
---

![[/cs61c/img/RISC-V-Quick-Reference/Untitled.png]]

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 1.png]]

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 2.png]]

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 3.png]]

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 4.png]]

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 5.png]]

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 6.png]]

### opcodes

- R: `0110011`
- I: `0010011`
- S: `0100011`
- B: `1100011`

### registers

![[/cs61c/img/RISC-V/Untitled 5.png]]

Registers

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 7.png]]

Example instruction

### j vs jr vs jal vs jalr

`j label` is a pseudoinstruction for `jal x0, label`

`ret = jr ra = jalr x0, ra, 0`

`jal ra, label` calls function within $2^{18}$ instructions of PC

- is a J instruction
- saves PC + 4 in register `ra`
- Sets PC to PC + offset

`jalr rd, rs, immediate:`

- is an I instruction
- saves PC + 4 in register `rd`
- sets PC to `rs + immediate` (doesn't use PC itself in calculation)
- Absolute use: `lui x1, <hi20bits>` then `jalr ra, x1, <lo12bits>`
- Relative use: `auipc x1, <hi20bits>` then  `jalr x0, x1, <lo12bits>`

### Psuedoinstructions

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 8.png]]

### Memory allocation

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 9.png]]

![[/cs61c/img/RISC-V-Quick-Reference/Untitled 10.png]]