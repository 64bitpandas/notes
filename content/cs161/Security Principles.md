---
title: "Security Principles"
weight: 10
---

## What is security?

Security is enforcing a desired property (confidentiality, privacy, integrity, authentication, availability) in the presence of attackers.

Some things that security helps protect:

- Physical safety (prevent disruption of cars, planes, etc)
- Personal information (health records...)
- National security

**Everything is hackable,** especially if it's connected to the internet. 

## Threat Model

It is important to understand the motives and methods behind attacks, and make general assumptions about them to be safe. A **threat model** is a model of the attacker and the resources they have.

### Assumptions

- The attacker can interact with systems without notice.
- The attacker knows information about your systems (OS, vulnerabilities, patterns of use...)
- The attacker is able to get lucky (1 in a million = vulnerable).
- The attacker has all resources and computing power needed to mount the attack.

## Basic Security Principles

### Trusted Computing Base

The trusted computing base (TCB) is the core components of a system that it relies on. A good TCB has **correctness** (does what you want it to), **completeness** (can't be bypassed), and **security** (can't be compromised).

- The TCB should be made as small and simple as possible.
- Typically, the TCB is the OS or some component of the OS (e.g. kernel mode).

### Human Factors

- A security system should be **easy to use,** otherwise users will not actually use it and/or find ways to get around it! It should also be foolproof to prevent incorrect usage from causing issues.
- Security systems should be robust to bugs and programming errors of the developers who create around it.
- Also need to protect against social engineering attacks (gain users' trust, get access that way)

> 💡 Case study: memory dialogs. The following dialog
> will appear to users as this:
>
> ![[/cs161/img/Security-Principles/Untitled.png]]
>
> ![[/cs161/img/Security-Principles/Untitled 1.png]]

### Security is Economics

- The cost of defense should be less than the cost of attacks.
- If attack costs more than the reward, it does not make sense to attack.
- Example: we wouldn't put a $10 lock for a $1 item

### Detect if you can't prevent

- **Deterrence:** stopping attacks before they happen
- **Prevention:** stopping attacks when they happen
- **Detection:** learn about an attack after it happened
- **Response:** doing something about an attack after it happened
    - Example: having emergency supplies after earthquake, keep backups in case of ransomware
    

### Defense in Depth

- More defenses = better
- Diminishing returns: 2 walls is better than 1, but 101 walls is not that much better than 100 walls

### Separation of Responsibility

(Distributed Trust): privilege should be shared between multiple parties, to prevent one from making poor decisions on their own

- Example: nuclear weapons require two people to simultaneously activate to launch

### Ensure Complete Mediation

Every access point should be protected. Otherwise, security measures will just be bypassed

- **Reference monitor:** a single point that all access must occur through (firewall, airport security...)
- Reference monitors should be correct, complete, and secure (just like a TCB)

### Least Privilege

Grant as little privilege as possible to as few people as needed, otherwise attackers may already have access they were unnecessarily granted.

### Security through obscurity

(Don't do it!) Also known as Shannon's Maxim / Kerckhoff's Principle

### Design in security from the start

Include security as part of the initial design, rather than adding it afterwards

![[/cs161/img/Security-Principles/Untitled 2.png]]