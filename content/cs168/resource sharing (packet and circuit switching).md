---
weight: 50
title: "Resource Sharing"
---

## Statistical Multiplexing

On the internet, millions of packets going to different destinations must share the same routers and paths. 

One way to handle this demand is **statistical multiplexing**- the concept of combining demands to share resources efficiently, rather than statically partitioning resources.

Some examples of statistical multiplexing:
 - processes sharing CPU cores (vs each process using 1 core)
 - Cloud computing (vs each user has their own datacenter)
 - public transit (vs each person drives a car)

**The peak of aggregate demand is far less than the aggregate of peak demands.**
 - Don't design for the absolute worst case, since not every user will have peak usage at exactly the same time.

## Two approaches to sharing
There are two main approaches to resource sharing, both of which enable statistical multiplexing.

**Reservations:** end-hosts explicitly reserve bandwidth when needed.
 - Implemented via **circuit switching**:
	 - 1. source sends reservation request to destination
	 - 2. switches establish a circuit
	 - 3. source sends data through circuit
	 - 4. source sends a teardown message
 
**Best effort:** just send packets and hope they reach the end destination
 - Implemented via **packet switching**
	 - Each packet makes an independent decision about how to handle the packet
	 - Switches add incoming packets to queue to handle **transient overload** (when incoming demand exceeds outgoing link bandwidth)
		 - Eventually if the link is saturated for a long time, **persistent overload** will occur as the queue overflows and drops packets

### Which method is better?
Circuit switching is better for:
 - workloads with predictable/understandable behaviors and smooth, constant-rate demand
 - providing an intuitive abstraction for business models

Packet switching is better for:
 - optimizing efficiency for amount of bandwidth used, especially for bursty workloads where peak load is reserved but rarely utilized fully
 - implementing a finer granularity of statistical multiplexing
 - Error recovery
 - Simpler implementation (no need for endhosts to manage each flow and keep track of requests)


### Handling failures
**Packet switching failure:**
 - Network must detect failure and recalculate routes on the routing control plane
 - Endhosts and individual flows may experience temporary loss of service, but no action is required on their part
**Circuit switching failure:**
 - In addition to all steps for handling packet switching failure, endhosts must tear down old reservations and send a new reservation request for every impacted flow
