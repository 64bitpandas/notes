---
weight: 40
---

## Some values
The **Bandwidth** of a link is the number of bits sent/received per unit time (measured in bps, bits per second).

The **Propagation delay** of a link is the time it takes a bit to travel along the link (measured in seconds). It is analogous to the 'length' of the link.

**Bandwidth-delay product (BDP)** is the product of bandwidth and propagation delay, measured in bits. It is analogous to the total capacity of a link (how many bits can be in the link at the same time).

**Transmission delay** is equal to Packet Size / Link Bandwidth. It describes how long it will take before the entire packet has entered the link.

**Queueing delay** describes the amount of time a packet exists in a router's queue when transient overload occurs.

**Packet Delay** is equal to the sum of transmission delay, propagation delay, and queueing delay.

**Router Capacity** is equal to the number of external ports multiplied by the speed of each port. 
 * Example: a router with 4 100Mbps ports and 1 1Gbps port will have a total capacity of 0.4 + 1 = 1.4Gbps.
![[/cs168/img/Pasted image 20220831185459.png]]