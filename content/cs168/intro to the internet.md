---
weight: 1
---

## About this Class

There are two meanings of internet:
 - the infrastructure that connects computing devices,
 - or the ecosystem of applications built on that infrastructure.

When the average person says "internet" they usually refer to the second definition. This class, on the other hand, explores the first.

**Why study the internet?** It's one of the most impactful and life-changing inventions in human history. In addition, it's too large and complex for theoretical models and requires an **entirely new design paradigm** of:
 - Decentralized control
 - best-effort service model (no guarantee or notification of data delivery)
 - route around trouble
 - dumb infrastructure, smart endpoints
 - end-to-end design
 - layering


## About the Internet: a high-level overview
At a very high level, the Internet is composed of three main types of components:
 - **End hosts**, like phones, computers, and IoT devices, send and receive packets as a first or last destination.
 - **Switches**, which are often routers, manage the connections between end hosts and forward packets arriving on one link to another link.
 - **Links** connect switches and end hosts together. These could be one of many technologies like fiber cables, WiFi, or phone lines.


### Some more definitions
**ISPs** (internet service providers) operate independently from one another and each manage a small portion of the available internet. Oftentimes, the infrastructure within an ISP is abstracted away from the public, and can be treated as a singular component.

Since ISPs are often competing and may not cooperate to create the optimal route for end users, network engineers must account for real-world and business considerations for any design.

**Autonomous Systems** (AS) are groups of routers under the same control. ISPs consist of one or more AS.

**Packets** are segments of bytes. Packets typically include:
 - A header (info for network to make decisions). Packet headers *must* contain the destination address.
 - A body (payload, and/or headers for other layers)
 - The header is meaningful to both the network and endpoint, whereas the body is only useful to the endpoint.

**Flow** refers to a stream of packets exchanged between two endpoints.

**Hostnames** are human-readable identifiers (like a domain, google.com).
 - Hostnames don't provide information about the location of a host. However, they can correspond to IP addresses that do.
![[/cs168/img/Pasted image 20220826114154.png]]


**The main job of the Internet is to transfer data between end hosts.** This is more difficult than it seems because there are many considerations:
 - What path do we take between hosts and switches?
 - Do the available paths have adequate bandwidth?
 - What protocols do we use? Can it handle every possible communication case?


## Internet Problems to Solve
In order to keep the internet running, we need to answer the following questions:
 - How do we create a robust naming scheme for billions of end-hosts? (IP)
 - How do we address endhosts? (DNS)
 - How do we map names to addresses?
 - How do we compute forwarding tables? (routing control plane)
 - How do we forward packets? (routing data plane)

