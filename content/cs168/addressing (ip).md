---
weight: 70
title: "Addressing"
---

How do we scale the ideas of routing and forwarding to the scale of the entire internet? 

This is mainly resolved with the domain of **addressing.**

## Early Addressing Schemes
In the early internet, each network had its own identifier, and each host within a network had its own identifier. Naturally, any host could be addressed using two numbers in the form `networkID.hostID`.

As a result of this hierarchical addressing scheme, each *internal router* only needs to store information about the hosts within the same network, as well as a gateway address to a *border router* connected to external networks.

## IPv4
In the modern internet, addresses are assigned using the IPv4 scheme, which is typically represented in the **dotted quad** format (XXX.XXX.XXX.XXX). 

IPv4 addresses are 32-bit, and 

### Classful Addressing
In the early internet, there were three main classes of networks:
![img](</cs168/img/Pasted image 20220918211936.png>)
However, this classful structure created several issues, the biggest of which was that the majority of organizations needed Class B networks, despite there only being ~16,000 of them.


### CIDR
As a solution to classful addressing, CIDR (**classless inter-domain routing**) was invented. CIDR introduces a new hierarchy for address assignment:
 - First, ICANN (Internet Corporation for Assigned Names and Numbers) acquired the remaining Class C networks.
 - Next, ICANN gives out a chunk to **RIRs** (Regional Internet Registries), like ARIN.
 - Then, larger organizations (mostly ISPs) acquire chunks from their responsible RIR.
 - Finally, smaller organizations and individuals acquire individual IP addresses from ISPs.

At each step, the assigner adds a certain number of bits to reduce the number of available addresses for the next step.


### IPv4 Header
![img](</cs168/img/Pasted image 20221003153110.png>)

* Version (4b): equal to 4 for IPv4 and 6 for IPv6
* Header Length (4b): typically set to 20 bytes if options are not used
* Type of Service (8b): used to specify how the packet should be treated
* Datagram length (16b): number of bytes in the packet (maximum $2^{16} - 1$, or 65535)
* Identifier (16b): used for uniquely identifying groups of fragments of a single IP datagram (all fragments in the same group will have the same ID)
* Flags (3b):
	* first bit is always 0
	* second bit is 1 if packet can be fragmented, 0 otherwise
	* third bit is 1 if packet isn't the last fragment, 0 otherwise
* Fragmentation Offset (13b): offset (divided by 8-bit units) from original payload
* TTL (8b): discard packet if TTL=0
* Upper-layer protocol: next layer protocol to use (6 for TCP, 17 for UDP)
* Header checksum: used to verify header integrity (recomputed at each hop)
* Source IP (32b): where packet came from
* Destination IP (32b): where packet is sent to


## Prefix Matching
Given a routing table, how do we actually match a requested destination IP with its host?

The naive solution would be to just iterate through all of the table entries until a match is found, but this is very slow. 
An improvement would be to create a **prefix tree** to take advantage of the binary tree structure enabled by bitstrings.
![img](</cs168/img/Pasted image 20221008151948.png>)


Realistically, due to the hierarchy of addressing multiple prefixes are often assigned to the same port (such as towards your ISP). Suppose in the illustration above that 0**, 101, and 11* all pointed towards Port 1. Then, the prefix tree can be compacted as such:

![img](</cs168/img/Pasted image 20221008152108.png>)





## IP Fragmentation

Maximum Transmission Unit (MTU)

### Example
Suppose we have an MTU of 500 bytes, and a 600-byte packet. Then, the packet will be split into two packets:
 - the first one will have 500 byte total length (480bytes data + 20 byte header). 
	 - Flag will be set to 001.
	 - Offset will be 0.
 - the second one will have 120 byte total length (100 bytes data + 20 byte header).
	 - Flag will be set to 000.
	 - Offset is 480/8 = 60.


## IPv6
The creation of IPv6 was motivated by the fact that one day we would run out of IPv4 addresses (32-bit, so 4,294,967,296 total). At this point we actually have already run out of IPv4 addresses, but you can buy some unused ones [here](https://auctions.ipv4.global/) for about $10,000-30,000 per /24 block. 

As of today (Oct 2022), about 40% of internet users support IPv6 (https://www.google.com/intl/en/ipv6/statistics.html), but it will take a very long time before we can completely deprecate IPv4.

### Philosophy
 - Don't make the network deal with problems: leave it to the end hosts
 - Simplify while still allowing extensibility

### Differences from IPv4
IPv6 is a more elegant, but unambitious protocol that mostly builds onto IPv4 with some minor improvements.

Here are the IPv4 and IPv6 headers side by side:
![img](</cs168/img/Pasted image 20221010105745.png>)

 - **More addresses:** $2^{128}$ addresses, which is far more than we will probably ever need. The source and destination address fields are now 4x larger (128 bits instead of 32).
 - **Removed checksum:** since the network is best-effort anyways, it's excessive to make each router compute the checksum. Instead, we can just verify it at the end host.
 - **Removed length field:** All IPv6 headers are the same length (40 bytes).
 - **Better options:** Rather than the ambiguous "options" field, IPv4 uses the "next header" field to point to the next layer's header.
	 - Each next header field has an ID corresponding to the protocol of the next header. For example, if Next Header = 6, the router will know to look for a TCP header.
	 - Next Headers can be chained/nested through multiple layers.
 - **Eliminated packet fragementation:** Instead of fragmentation, use **MTU Discovery**, where hosts can send small exploration packets to determine the MTU of routers in the path and decide how big to make the packets. If a packet larger than the MTU is sent to a router, an error message will be sent back to the host.
 - **Added flow label:** explicit mechanism to denote related packet streams: allow for multiple sessions and grouping of related packets


## Security

If an attacker can choose whatever they want to put in an IPv4 packet, they can exploit several vulnerabilities:
 - change source and destination addresses to whatever you want: can claim to be a source you're not
	 - choose different source address for every packet to avoid filtering
	 - cause destination to block a particular host
 - set Type of Service to cause hosts to treat attack traffic as high priority
	 - most ISPs mitigate this by not allowing end hosts to set TOS
 - send packets larger than MTU to create resource exhaustion
 - traceroute: discover topology via TTL