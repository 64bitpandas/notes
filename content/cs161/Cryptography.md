---
title: "Cryptography"
weight: 60
---

## What is Cryptography?

Cryptography is the study of secure communication over insecure channels, and often involves providing guarantees on the security of resources in the presence of an attacker.

**The Cast**

- Alice: sender
- Bob: recipient
- Eve: eavesdropper (cannot modify messages)
- Mallory: malicious attacker (can modify messages)

### **Three Goals of Cryptography**

1. **Confidentiality:** adversary cannot read messages
    1. Lock and unlock messages on local machine of sender and recipient, so all messages in the communication channel are encrypted
    2. If encrypted, the ciphertext should not give attackers any additional information about the plaintext, other than what the attacker already knew beforehand.
    3. Ideally, it should be impossible to distinguish between two encrypted messages of the same length.
    4. **IND-CPA:** Indistinguishability under chosen plaintext attack: If Eve sends a pair of plaintexts $M_0$ and $M_1$ to Alice to encrypt, Eve must only be able to guess which encrypted message was which plaintext with probability $0.5$. (This must also apply for two identical strings!)
        1. Edge cases: does not hide length, and only applies to polynomial time attacks (since exponential time brute forcing would be unfeasible). For example, probability $0.5 + 0.5^{128}$ is acceptable.
2. **Integrity:** adversary cannot change messages without being detected
    1. Attach a tag to messages. If the tag was changed, then the message was modified
3. **Authenticity:** can prove that a message came from its intended sender

### **Kerckhoff's Principle**

Security through obscurity: always assume attackers know the system. i.e. cryptosystems should be secure even if attackers know exactly how it works:

- Change keys automatically if leaked
- Key should be kept secret

### Summary

![[/cs161/img/Cryptography/Untitled.png]]

## Symmetric Key Encryption

Encryption schemes provide confidentiality.

All symmetric key algorithms have three parts: **keygen, encrypt, and decrypt.** Both encrypt and decrypt use the same key generated in keygen.

![[/cs161/img/Cryptography/Untitled 1.png]]

**Limitation:** encryption does not typically hide length (since padding a small text to a video size would be really inefficient).

### Key Generation: One-Time Pads

![[/cs161/img/Cryptography/Untitled 2.png]]

To encrypt, XOR each bit in the message with a bit in the key. To decrypt, XOR the ciphertext with the key in the other direction.

Keys are random $n$ bit objects, where $n$ is the length of the message. In One-Time Pad, a new key is generated for every message sent.

**Correctness Proof:**

![[/cs161/img/Cryptography/Untitled 3.png]]

# Block Ciphers

**Block Cipher** is an encryption/decryption algorithm that encrypts a fixed number of bits.

![[/cs161/img/Cryptography/Untitled 4.png]]

![[/cs161/img/Cryptography/Untitled 5.png]]

**Encryption:** uses k-bit key $K$, n-bit plaintext $M$ and outputs an n-bit ciphertext $C$ using the formula $\{0, 1\}^k \times \{0, 1\}^n \to \{0, 1\}^n$

A secure block cipher is like a randomly chosen permutation from the set of all permutations on $n$-bit strings (since attackers can't get any information from a block cipher)

Block ciphers are impossible to brute force in polynomial time.

**caveats:** Block ciphers are **not IND-CPA secure** because it is deterministic- sending the same message multiple times will always give the same encryption. They can also only encrypt messages of a constant size (need to be chained).

### AES: Advanced Encryption Standard

An industry standard for block cipher encryption that hasn't been broken so far.

Key size: 128 bits (or 256, for AES-256)

Block size: 128 bits

14 cycles of repetitions, where the current ciphertext is represented as a state matrix, and every cell is mapped to a sub-byte. Then the algorithm shifts the bytes in each row by a certain offset.

## Modes of Operation

### ECB

**ECB Mode (Electronic Codebook):** Splits a message into blocks of 128 bits, and feeds each of them through block cipher/AES individually

![[/cs161/img/Cryptography/Untitled 6.png]]

- **not IND-CPA secure,** same issues as AES that are not addressed.

### CBC

**CBC Mode (Cipher Block Chaining):** uses an Initialization Vector to introduce randomness into each step.

![[/cs161/img/Cryptography/Untitled 7.png]]

- **Initialization Vector (IV):** Randomized data vector for every message that is XORed in at the first step. In future steps, the previous step's output becomes the IV for that block.
- Formula: $C_i = E_K (M_i \oplus C_{i-1})$, $C_0 = IV$
- IV can be included in the message since the key is still secret
- Decryption: Parse ciphertext as (IV, $C_1$, ... $C_m$) - XOR with IV or previous ciphertext

![[/cs161/img/Cryptography/Untitled 8.png]]

- Encryption is not parallelizable (requires computation of previous block), while decryption is parallelizable (every step only requires ciphertext)
- CBC is IND-CPA secure since the IV makes the encrypted ciphertext random. However, reusing IV makes it not IND-CPA secure because attackers can determine if two ciphertexts are the same, up to the first different block

### Padding

Sometimes, the message is not exactly a multiple of block size, so we must add padding.

- Can't add a constant value (like 0) because it is impossible to tell if this was part of the original message, or just padding
- Example padding scheme: append a 1, then all 0's (might need to append an extra block if already a multiple of 128)

### CTR

**Counter Mode:** introduces a counter value and a random nonce to ensure that two identical plaintext blocks cannot be distinguished after being converted to ciphertext.

- CTR is parallelizable, both in encryption and decryption (better than CBC).
- No padding is necessary (after getting the random nonce/counter value, only take the first x bits needed to pass into XOR)
- AES-CTR is IND-CPA secure assuming that nonce is randomly generated and never reused

![[/cs161/img/Cryptography/Untitled 9.png]]

![[/cs161/img/Cryptography/Untitled 10.png]]

# Cryptographic Hashes

A **hash function** $H(M)$ takes in an arbitrary length message $M$ and outputs a **fixed-length,** $n$-bit hash.

## Properties

- $\{0, 1\}^* \to \{0, 1\}^n$
- Deterministic in nature
- Provides integrity with the assumption that a known hash is not compromised
    - Example: when downloading, match hash of downloaded file with public hash to ensure file was not tampered with
- **One-way**: infeasible to find the original message given the hash
    - Formally, for all polynomial time attacks `Adv(k)`, the probability of `Adv(y) = x` given that `y = H(x)` is negligible (exponentially small)
    - $H(x) = 1$ is **not** a one-way function because it is trivial to solve for an $x$ that works (even if it may not be the original x, it doesn't matter)
- **Second Preimage Resistance:** given an input, it is infeasible to find a different input with the same hash.
- **Resistant to collision:** Unfeasible to find a pair of inputs $x' \ne x$ such that $H(x') = H(x)$
    - By the Birthday Problem, finding a collision on an $n$ bit output only requires $2^{\frac{n}{2}}$ on average
    - Implies second preimage resistance (weaker condition)
- **Unpredictability:** Attackers should not be able to predict the input given a single output (i.e. appears random)

## Examples

- MD5 (128 bits, broken)
- SHA-1 (160 bits, broken)
- SHA-2 (256, 384, or 512 bits, current standard)
- SHA-3 (256, 384, or 512 bits, current standard, not vulnerable to length extension attacks but slower)

## Length Extension Attacks

If an attacker knows $H(x)$ and the length of $x$, they can create $H(x || m)$ for any $m$ ($||$ is concatenation)

# MAC

**Goal:** provide integrity to messages (tell recipient who sent it)

**Idea:** send a tag $T$ with the message

![[/cs161/img/Cryptography/Untitled 11.png]]

Two parts:

- Keygen: Create key $K$
- MAC(K, M): Create tag $T$ for message $M$ using key $K$

**Properties:**

- Correctness: MAC is deterministic
- Efficiency
- Security: **EU-CPA: existentially unforgeable under chosen plaintext attack** (see below)

### EU-CPA

1. Mallory sends multiple messages to Alice and receives their tags
2. Mallory tries to create a message-tag pair $(M', T')$ where $M'$ is a new message that has not been sent
3. If $T'$ is a valid tag for $M'$, then Mallory wins
4. A scheme is EU-CPA if the probability of winning is essentially 0

### NMAC

**Idea:** use cryptographic hashes to build a MAC

**KeyGen:** Create two $n$ bit keys $K_1$ and $K_2$, where $n$ is the length of hash

**NMAC:** $H(K_1 || H (K_2 || M))$

**EU-CPA secure:** yes, assuming $K_1 \ne K_2$

### HMAC

$H((K \oplus opad) || H((K \oplus ipad) || M))$

- opad (outer pad): `0x5c` repeated until same length as $K$
- ipad (inner pad): `0x36` repeated until same length as $K$

- HMAC is both a hash function and a MAC
- Attackers cannot brute force HMAC because it requires the key $K$

# Authenticated Encryption

**Idea:** combines confidentiality and integrity on a message, e.g. combining MAC with encryption

One method of Authenticated Encryption: combine existing schemes that individually provide confidentiality or integrity. **Do not reuse keys between steps.** 

- Example: $MAC(K_2, Enc(K_1, M))$ or $Enc(K_1, M || MAC(K_2, M))$
- Typically, use **encrypt-then-MAC** since it's more robust to mistakes and doesn't have to be decrypted before checking MAC.

**Authenticated Encryption with additional data (AEAD):**  provides all 3 of confidentiality, integrity, and authenticity by guarantees the integrity of additional data (such as memory addresses).

- If used correctly, great; if incorrect, then it loses multiple requirements.
- Example: **Galois Counter Mode (GCM)** where authentication tags are attached to each block, and calculated based on the previous blocks.

![[/cs161/img/Cryptography/Untitled 12.png]]

# Pseudorandom Number Generators

In order to make IND-CPA schemes, randomness is required. How do we get this randomness?

- More specifically, randomness = both random and unpredictable with high entropy (0 entropy = uniform)
- True randomness can be generated from a physical source, such as a wall of lava lamps
    - Usually expensive and slow
    - Can be biased towards certain values

To compromise with cost and speed, pseudorandom number generators use a small amount of true randomness to generate random-looking output.

- Can be deterministic, but attackers who do not know the internal state should not be able to distinguish it from true randomness.
- It is impossible to make a truly random PRNG. This is because there are only $2^s$ possible output sequences generated from an initial seed $s$ bits long

PRNG's have two functions:

- **Seed(randomness):** initialize the PRNG internal state with true random entropy
- **Generate(n):** generates $n$ pseudorandom bits

Properties:

- **Correctness:** deterministic if the same seed is received
- **Efficiency:** can quickly generate new bits
- **Security:** indistinguishable from true randomness

One possible PRNG is to use a block cipher in CTR mode, and OR the outputs of the block cipher encryptions together.

## Stream Ciphers

Stream ciphers are another way of making symmetric key encryption using PRNG's.

**Idea:**  Set the seed to $K|IV$, XOR PRG.Generate($M$) with $M$ itself, where $M$ is the message that should be sent.

# Key Exchange

**Problem:** how do you share private keys if you need them to unlock the message in the first place?

## Diffie-Hellman Key Exchange

**Idea:** Alice sends a locked key to Bob. Bob locks it as well using his private key and sends it back to Alice. Alice then unlocks her key, and Bob is left with Alice's message but locked only with his own lock.

**Math (Diffie-Hellman Problem):** Given $g,p,g^a \mod p, g^b \mod p$, where $p$ is a large prime and $g$ is a generator, it is computationally unfeasible to find $g^{ab} \mod p$ if you don't have $a$ or $b$.

The **shared symmetric key** is $g^{ab}$.

![[/cs161/img/Cryptography/Untitled 13.png]]

### Properties of DHE

- **Ephemeral:** can be used for temporary/short-term calculations: once a single $a, b$ are used for some exchange, they never need to be used again
- **Forward Secrecy:** If $a, b, K$ are discarded after a certain amount of time, it is impossible for an attacker to decrypt any recorded messages received via insecure communication

### Issues with DHE

![[/cs161/img/Cryptography/Untitled 14.png]]

**Man in the middle (MITM) attack:** If Mallory encrypts the received messages with her own private key $m$, and send this over to Alice or Bob, they will both think they got valid keys from each other but in reality Mallory has all of the information necessary to decrypt their messages. This can be mitigated with certificates or digital signatures.

**Active protocol:** Bob and Alice must both be online at the same time to exchange keys.

**No authentication:** Impossible to tell with the current scheme who a message came from

# Public Key Cryptography

**Idea:** Each person has two keys: a **public key** which is known to everybody, and a **private key** which is only known by that person. 

- Typically, each public key corresponds to one private key.
- Uses number theory, and messages are represented as numbers rather than bitstrings.

### Three parts

1. KeyGen(): generates a public/private keypair $PK, SK$
2. Enc(PK, M): encrypts plaintext using public key
3. Dec(SK, C): decrypts ciphertext using secret key

### Semantic Security

Semantic security is the standard notion of security for public key schemes. This is similar to IND-CPA, but simplified because Eve now possesses the public key of Alice and Bob and can encrypt messages herself.

![[/cs161/img/Cryptography/Untitled 15.png]]

## El Gamal Encryption

**Idea:** modify Diffie-Hellman so it can be used to directly encrypt and decrypt messages.

El Gamal uses the Diffie-Hellman assumption ($g^{ab}$ appears random) as well as the **discrete logarithm problem:** given $g, p, g^a \mod p$ for a random $a$, it is difficult to find $a$.

**Steps:**

- **KeyGen:** Bob generates private key $b$ and public key $B = g^b \mod p$. $p$ is a large publicly known prime number.
- **Enc(**$g^b$, $M$): Alice generates random number $r$ and computs $g^r \mod p$. Alice then sends $C_1 = g^r \mod p, C_2 = M \cdot (g^b)^r \mod p$ to Bob.
    - Constraints: $0 < M < p-1$. Note that $M$ cannot be zero because it would be very easy for an attacker to see that the encrypted value is also zero.
- **Dec(**$b, g^r, M \cdot g^{br}$**):** Bob computes $M \cdot g^{br} \cdot (g^r)^{-b} \mod p$.

**Malleability:**

An adversary can easily tamper with the message by multiplying the ciphertext by some value. El Gamal encryption does not provide integrity.

- Can be used as a feature (transform ciphertext without needing to decrypt)

## Hybrid Encryption

Public key encryption is slow (since there is a lot of math involved) and can only encrypt small messages (due to the modulo operator).

The solution is to use public-key encryption for initial key exchange with a random temporary key $K$,  then use symmetric key encryption to encrypt large messages using $K$.

# Digital Signatures

Digital signatures ensure authenticity and integrity without needing to share a secret key beforehand.

Digital signatures consist of three parts:

- KeyGen(): generate a public and private keypair.
- Sign(SK, M): sign the message $M$ using the signing/secret key $SK$ to produce a signature.
- Verify(PK, M, sig): check if the signature is valid using a verify/public key.

Secure digital signature schemes should be secure under EU-CPA.

## RSA

KeyGen:

- Random pick two large primes $p$ and $q$
- Compute $N = pq$
- Choose $e$ relatively prime to $(p-1)(q-1)$
- Compute $d = e^{-1} \mod (p-1)(q-1)$
- Use $N$ and $e$ as the public key, use $d$ as the private key

Sign:

- Compute a cryptographic hash $H(M)^d \mod N$

Verify:

- Verify that $H(M) \equiv sig^e \mod N$

## Distributing Public Keys

If public keys are verified over an insecure communication channel, Mallory can replace it with her key and intercept all incoming messages.

**Idea:** Sign public keys to prevent tampering. Store these signatures in some **trust anchor** (a source you can implicitly trust).

- **Trust on first use:** the first time you communicate with someone, trust the public key that is used and warn if it changes in the future.
- **Certificate Authority:** another trusted entity gives a signed endorsement of someone's public key
    - To address scalability and ensure there isn't a single point of failure, we can establish **hierarchical trust:** root certificate authorities can delegate signing power to other trusted authorities (intermediate certificate authorities).
    - The public keys of the ~150 root CAs are hard-coded into most devices.

### Revocation

If a certificate authority issues a bad certificate, it can be revoked.

One common strategy is to have expiration dates for certificates. After the certificate expires, it gets revoked and no longer trusted.

- Renewing certificates more frequently makes it more secure, but it becomes more difficult to use.

Another strategy is to release a Certificate Revocation List (CRL) that users can download. However, the lists can get very large and users may not be able to download it right away. Attackers can also force the CA to go offline, in which they cannot publish an updated CRL.

# Password Hashing

In order to securely store passwords, hash each user's password and check the hash of incoming passwords against the stored hash. This is secure because hashes are one-way so even if an attacker has the hash function they can't look it up.

However, attackers can use brute-force attackers to pre-compute common password hashes. To solve this, you can **salt** the hashes (a random, public value appended to the end of passwords before being hashed) so that every entry is unique.

Another mitigation is to use slow hashes and attempt timeouts to further slow down attackers. Normal users won't be able to detect the slowdown.

# Bitcoin

Bitcoin is a cryptocurrency composed of two components: a ledger, and cryptographic transactions.

Every user in the ledger has a public key and a signing (private) key. Whenever a transaction is made (for example, Alice transfers 10 bitcoin to Bob), then Alice will sign the message " $PK_A$ transfers 10 bitcoin to $PK_B$ " using her signing key.

Now, the problem arises that Alice can request transactions whenever she wants, even if she doesn't actually have the money! We will need to keep a public ledger to keep track of transactions.

The ledger ($L$) owner checks a transaction ($TX$) with the following steps:

1. Verify that the signature on TX (the transaction) matches with the public key of the sender.
2. Verify that the sender has bitcoins sent to them from somewhere in $L$ (i.e. they actually have money to spend)
3. Verify that the sum of amounts received by the sender in $L$ total to the amount being sent

If any of these verifications fail, the transaction will not be posted to the ledger and it will be as if it never happened in the first place.

### Properties of the Ledger

The ledger is:

1. publicly visible,
2. append only,
3. immutable.

Bitcoin uses a hash chain (also known as a blockchain). Each transaction has a collision-resistant hash, and each block's hash includes the hash of the previous block.

Given $H(i)$ and all of the blocks $1...i$, Alice can verify that the previous blocks are not compromised.

### Decentralized Blockchain

In Bitcoin, every participant stores a copy of the blockchain (so there is no central party). When a new transaction is made, it is broadcast to everyone.

Every node checks the transaction and creates a new block if valid. To reach **consensus,** the majority of participants must agree on the blockchain.

- Not everyone is allowed to add blocks; only miners. Only the miner that solves the **proof of work puzzle** can add a block.
    - This puzzle is typically finding a random number when, appended to the block data and hashed, creates a hash starting with $N$ number of zero bits. (H(block || random number) = 00000...000423ba5c...)
    - **The longest correct chain is always preferred.** Even if some malicious miners fork the chain and remove transactions, they should eventually lose to the honest miners.
    - Miners are rewarded when they successfully append a block.
    - Mining frequency is about 10 minutes; if more or fewer miners are active, then the difficulty of the problem can be adjusted to keep the time consistent.
- Due to forks, it is not guaranteed that all transactions will be persisted. To be sure, most people wait 6 transactions before confirming, since the chance of this being forked is very low.