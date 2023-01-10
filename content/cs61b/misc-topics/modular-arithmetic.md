# Modular Arithmetic and Bit Manipulation

> [!warning] Content Note
>
> Make sure you're comfortable working with binary numbers (adding, subtracting, converting to decimal) before continuing.

## Integer Types

This is an excerpt from the chart in [Java Objects](/cs61b/oop/objects.md). Go there to review primitive types first!

| Type  | Bits | Signed | Literals                      |
| ----- | ---- | ------ | ----------------------------- |
| byte  | 8    | yes    | 3, (int)17                    |
| short | 16   | yes    | None - must cast from int     |
| char  | 16   | no     | 'a', '\n'                     |
| int   | 32   | yes    | 123, 0100 (octal), 0xff (hex) |
| long  | 64   | yes    | 123L, 0100L, 0xffL            |

## Signed Numbers

A type is **signed** if it can be **positive** **or** **negative.** Unsigned types can _only_ be positive.

In signed types, the **first bit** is reserved for determining the sign of the number (0 is positive, 1 is negative). This means that there is one fewer bit for the actual number. For example, ints only have **31** bits for the number.

### Reading negative numbers

Let's say you are given a number like `10100`and want to convert it to decimal. We know that the 1 in the front means it's a negative number! However, we can't just discard that 1 and read the rest like a positive number. Instead, we have to **flip all the bits** and then **add one** to the result. So, `10100` flipped will become `01011`. Adding one will result in `01100`, which is the correct answer (12).

**Why do we have to do this?** Read on to the next section to find out!

## Two's Complement

**Two's Complement** is a a method of storing negative numbers in a way that supports proper arithmetic. Here's how it works:

1. Start with a binary number we want to negate, like `0101`, which is 5.
2. Flip all the bits to make `1010`.
3. Add one to make `1011`.

Although it makes negative numbers harder to read, the benefits are much more significant- it allows addition and subtraction to work between positive and negative numbers.

If you want to see firsthand why simply flipping the signed bit doesn't work, try out some problems in [this worksheet](https://d1b10bmlvqabco.cloudfront.net/attach/k5eevxebzpj25b/jcaul3qcivh6kh/k8g51ayfl9ui/GuerillaSection2.pdf) ([solutions](https://d1b10bmlvqabco.cloudfront.net/attach/k5eevxebzpj25b/jcaul3qcivh6kh/k8g53zthgevk/GuerillaSection2Sols.pdf)).

## Modular Arithmetic

Since primitive types have a fixed number of bits, it is possible to **overflow** them if we add numbers that are too large. For example, if we add `01000000`(a byte) with itself, we'd need 9 bits to store the result!

This will cause lots of issues, so we use **modular arithmetic** to **wrap around to the largest negative version** and keep the number in bounds. For example, `(byte)128 == (byte)(127+1) == (byte)(-128)`**.**

## Bit Operations

**Mask: &**

* `A & B` will only keep the bits that are 1 in A **AND** B
* Example: `00101100 & 10100111 == 00100100`

**Set: |**

* `A | B` will keep the bits that are 1 in A **OR** B
* Example: `00101100 | 10100111 == 10101111`

**Flip: ^**

* `A ^ B` will keep the bits that are 1 in A **XOR** B
* In other words, 1 if bits are unequal in A and B, 0 otherwise
* Example: `00101100 ^ 10100111 == 10001011`

**Flip all: \~**

* `~A` will flip all the bits from 1 to 0 or 0 to 1 in A
* Example: `~10100111 == 01011000`

**Shift Left: <<**

* `A << n` will shift all bits left n places
* All newly introduced bits are 0
* Example: `10101101 << 3 == 01001000`
* `x << n` is equal to x \* 2^n

**Arithmetic Right: >>**

* `A >> n` will shift all bits **except for the signed bit** right n times
* Newly introduced bits are the same as the signed bit
* Example: `10101101 >> 3 == 11110101`

**Logical Right: >>>**

* `A >>> n` will shift ALL bits right n times
* Newly introduced bits are 0
* Example: `10101101 >>> 3 == 00010101`
* Another example: `(-1) >>> 29 == 7` because it leaves 3 1-bits- ints are 32 bits

## Why is this useful?

Just looking at these obscure operations, it may be unclear as to why we need to use these at all.

Well, [here's a massive list of bit twiddling hacks](https://graphics.stanford.edu/\~seander/bithacks.html) that should demonstrate plenty of ways to use these simple operations to do some things really efficiently.

These operations are also the **building blocks for almost all operations done by a computer.** You'll see firsthand how these are used to construct CPU's in [61C](https://cs61c.org/).
