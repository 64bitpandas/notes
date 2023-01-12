---
weight: 60
title: "Internet Organization"
---


Currently, five internet layers exist:
 - Application (L7), where code interfaces with the internet as an abstraction,
 - Transport (L4), which can guarantee either reliable or unreliable data delivery,
 - Network (L3), which delivers best-effort global packet delivery,
 - Datalink (L2), which delivers best-effort local packet delivery,
 - Physical (L1), which physically moves bits between locations.

HIstorically, L5 (Session layer) and L6 (Presentation layer) existed, but have since been combined with L7 and L4.


### Local vs. Global Packet Delivery
There are many different types of links (ethernet, fiber, wifi...) that connect switches together. 
However, each type of link only knows how to manage its own network; ethernet packets can't get transferred into wifi on their own.

This is the main difference between local (single network) and global (multi network) delivery, which is managed between L2 and L3.


## What is a protocol?
Communication throughout the internet is standardized into **protocols**, which are agreements between parties on how to communicate.

Protocols include both the syntax (how the data is formatted) and the semantics (how the data corresponds to states). They exist at many levels:
![[/cs168/img/Pasted image 20220907173818.png]]

The primary benefit of having so many layers is abstraction- each layer only needs to deal with its specific assignment, and assume that all lower layers carry out their assignments.

All layers need to be implemented on the end-host, in order to convert bits into application data. 
![[/cs168/img/Pasted image 20220907174540.png|500]]

However, only L3 and below are supported by the network because the network does not support reliable delivery.
 - More specifically, switches implemented L1 and L2, and routers implemented L1, L2, and L3.

Below is an example of a protocol diagram:
![[/cs168/img/Pasted image 20220907182007.png]]
Notice that the datalink layers (ethernet, OTN) never communicate directly between each other; they send their information up to the IP network layer to be translated.

## End to End Principle
A guiding principle for modern internet architecture is the **end to end principle**, which states that the end-hosts should be responsible for guaranteeing security and reliability without needing to rely on anything within the network.

This is because the network cannot be guaranteed to be 100% reliable (equipment breaks down, etc), and end-to-end checks for reliability are required anyways so might as well make them robust.