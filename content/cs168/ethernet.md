---
weight: 150
---

## Shared Media
In a radio network, nodes use a shared medium (the electromagnetic spectrum). As such, transmissions from different nodes might collide with one another, so we need a **multiple access protocol** to allocate the medium between users.

Some common approaches for doing this include:
 - Frequency Division Multiplexing: divide medium by frequency. This can be wasteful since frequencies are likely to be idle often.
 - Time Division Multiplexing: divide medium by time. Each sender gets a fixed time slot to send data. This has similar drawbacks to FDM.
 - Polling protocols: a turn-taking scheme where a coordinator gets to decide who gets to send data when (how Bluetooth works)
 - Token-passing: a turn-taking scheme where a virtual token is passed around, and only the holder can transmit
 - Random access: see [[#Pure ALOHA random access]]

## ALOHAnet
Additive Links Online Hawaii Area: a first attempt at wireless connections across the Hawaiian islands (1968, Norman Abramson)

In ALOHAnet, a hub node transmitted its own frequency, and all remote nodes transmitted on the same frequency using a random access scheme.

### Pure ALOHA random access
1. If a remote has a packet, just send it.
2. When the hub gets a packet, it sends an ack.
	- If two remote sites transmitted at the same time, a collision will occur and the hub will not send an ack
3. If the remote doesn't get the expected ack, wait a random amount of time and resend.

## Ethernet
In 1972, Bob Metcalfe was trying to connect hundreds of Xerox computers in the same building. It needed to be fast, maximially distributed, and cheap. 

The main idea was to connect all of the machines onto the same cable, and use it as a shared medium.

### Carrier Sense Multiple Access (CSMA)
CSMA is an improvement over ALOHA: instead of nodes sending data first, CSMA nodes listen to the network first and start transmitting when it's quieter.

By itself, this doesn't completely avoid collisions due to propagation delay.

### CSMA/CD
Main idea: listen while you talk. If a node detects another packet being sent at the same time, stop sending since the packet has already collided. This is **collision detection** (CD).

In addition, use a randomized **binary exponential backoff**: if retransmit after collision also collides, wait twice as long; continue doubling for every collision.

### Addresses and Service Types
On the ethernet shared medium, everyone will receive transmitted data. As such, ethernet has **flat addresses:** no routing or aggregation is required.

Addresses are 48 bits (6 bytes) shown as six 2-digit hex numbers with colons. The general structure is:
 - 2 bits of flags
 - 22 bits identifying manufacturer (company/org)
 - 24 bits identifying device
Addresses are typically permanently stored in network interface hardware, and are mostly unique (there are more devices than there are addresses). 

The **broadcast address** is all ones (FF:FF:FF:FF:FF:FF). Data sent to this address are received by everyone. This allows trivial implementation of broadcast.

Multicast (sending to all members within a group) is also trivially implemented by setting the first bit to 1.

However, classic ethernet does not support anycast (single address being shared by multiple devices).


### Switched Ethernet
In modern ethernet implementations, shared media is rarely used. Instead, switches exist between nodes that remove the possibility of collision. 

The main idea of switched ethernet is to flood all packets, such that everyone gets it just like in classic ethernet.


### Summary: MAC (L2) vs IP (L3)

MAC addresses:
 - hard coded by device manufacturers
 - not aggregation friendly ("flat" addresses with no hierarchy)
 - topology independent: same even when host moves
 - main purpose: packet transfer within the same L2 network
 - require no network configuration

IP addresses:
 - dynamically configured and assigned by network operators + DHCP
 - have hierarchical structure
 - topology dependent: depends on where host is attached
 - main purpose: packet transfer to destination subnet

The IP/MAC split solves the **bootstrap problem**, in which the fixed behavior of MAC makes a convenient first assignment that IP can build off of for assigning the first hop. 

## ARP
**Address Resolution Protocol:** converts IP addresses to corresponding ethernet addresses.

ARP runs directly on top of **L2** (between L2 and L3, which is IP). In general, the host broadcasts a query asking who has a particular IP address. The desired host then responds via unicast with its ethernet address. 

Hosts typically cache results in an ARP table (Neighbor table), which is refreshed occasionally.


### Example
Suppose we have the following network topology:
![[/cs168/img/Pasted image 20221213130109.png|300]]

If H1 wants to send a packet to the IP address `10.0.0.2`:
1. Check the prefix to see if it's on the same subnet. (it is)
2. H1 broadcasts an ARP request to all hosts on the subnet.
3. H2 answers H1's request with its MAC address (using unicast)
4. H1 receives the answer, sends the packet, and caches the entry in its ARP table.

If H1 wants to send a packet to `10.1.0.3`:
1. Check the prefix and see that the subnet is different. 
2. Since the subnet is different, broadcast an ARP request for the router (`10.0.0.254`) instead.
3. R1 answers H1's request with its MAC address.
4. H1 receives the answer, and sends the packet with destination IP `10.1.0.3`, but destination MAC of R1.



## DHCP
Although ethernet addresses are hard-coded into the hardware, IP addresses are adaptable depending on the context. Typically, the routers know what IP addresses to assign to hosts, but how do hosts know this?

One method is to manually assign static addresses to each host. However, portable devices like phones or laptops may move around multiple times a day, and needing to reassign them every time we move is very annoying!

The solution is **DHCP (Dynamic Host Configuration Protocol)**, which provides a way for hosts to query the network for local configuration information (IP address, netmask, default gateway, local DNS resolver).

DHCP servers are added to the network, either as standalone or as a part of a router, which listen to UDP port 67.

The DHCP server leases IP addresses to hosts. If the lease is not renewed, the IP address will be returned to the pool and can be assigned to another host.

### DHCP handshake
![[/cs168/img/Pasted image 20221210183624.png]]

Notes:
 - Discovery and request packets are **broadcast** by hosts, and have source IP 0.0.0.0, destination IP 255.255.255.255. This is because DHCP is built on IP, but no IP addresses are initially known.
- The source MAC is the address of the router, and the destination MAC is the address of the next hop's router.


