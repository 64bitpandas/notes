---
title: "Introduction to Routing"
weight: 30
---

## Addressing and Naming

In the real world, people have names and are located at addresses. When we move around, our name stays the same, but our address changes.

The internet works in a very similar manner. Hosts have a **network name** (which describes which host it is) and a **network address** (where the host is currently located).

## Conceptual Intro to Routing
 - First, we'll run a distributed routing algorithm between switches and routers. This algorithm will help us gather information about the network, and compute paths between its topology.
- Within each router, the algorithm will store forwarding information to send packets to different links based on their destination. This is known as the **forwarding table**.

The distinction between *creating* the forwarding table and *using* the forwarding table is captured in the **control plane** and **data plane**.
* There is also a third plane, the **management plane**, which allows the router to interact with humans and external systems to configure and monitor the device.

The control plane is the mechanism using to compute the forwarding table.
 - Inherently global (must know topology)
 - Contains routing algorithm
 - Relatively infrequent time scale (per network event)
 - Primary challenge: compute routes at scale while accounting for network failure and the autonomy of ISPs

The data plane uses the table to forward packets.
 - Inherently local (only depends on arriving packet and local table)
 - Contains forwarding algorithm
 - Relatively frequent time scale (per packet arrival)
 - Primary challenge: perform routing operations at a nanosecond time scale


### Forwarding vs Routing: Summary
**Forwarding** is the process of looking up a packet's destination in a routing table and sending the packet to the correct neighbor. Forwarding is inherently *local* and operates on the *data plane*.

**Routing** is the process of routers communicating with other routers to determine how to populate forwarding tables. Routing is inherently *global* and operates on the *control plane*.


# Destination-Based Forwarding

## Forwarding Tables

For the data plane work, each router needs to store information about how to reach a destination.

A simple way of doing this is **destination-based forwarding:** the decision of where to route packets to depends only on its destination.

## Routing Graph Representation
We can graph paths that a packet will take to one particular destination within the network.
 - Each routing table contributes directed connections from its host router to the next hop in the table.
 - Each node/router should have exactly one arrow to another node.
 - Once two paths join at a router, they will never split again.
 - The set of all paths creates a **directed delivery tree** that covers every node that is able to reach the destination. This is a type of oriented spanning tree where the root is the destination node.

## Routing State Validity
The minimum requirement for a "good" routing state should be that the destination is reachable.

A global routing state is *valid* if it produces forwarding decision that always deliver packets to their destinations. 

**Validity is achieved if and only if for each destination, there are no dead ends or cycles.** 

The goal of routing procols is to compute a valid state. 

### Validation
Now that we have a condition for validity, how do we actually check that it's true?
 - First, select a single destination.
 - For each router, mark the outgoing edge with an arrow. There should only be one per router if using destination-based routing.
 - Eliminate all links that were not marked.
 - The state is now valid if and only if the remaining graph is a directed delivery tree (acyclic, with every arrow pointing towards the destination).
 - Repeat this process for every destination.


## Types of Routers
The internet is a network of networks, and not all of these networks may use the same protocol. This is primarily because each network has a different use case, which have different requirements (size, number of hosts, bandwidth, cost...)

**Intradomain Routing::** also known as Autonomous System: routing within a single network
 - Usually use IGPs (Interior Gateway Protocols)
 - Each network can choose their own protocol
 
**Interdomain Routing:** routing between different networks (autonomous systems)
 - EGPs (Exterior Gateway Protocols)
 - All AS's agree on a protocol
 - Internet has used BGP for a long time

# Intradomain Routing (L2/L3)
## Least-Cost Routing
How do we quantify how "good" a route is exactly?

1. Route needs to work: destination needs to be reachable (no loops or dead ends)
2. Minimize cost: number of hops, price, progagation delay, distance, reliability
	1. Cost can be abstracted into some general value/weight for each edge

Costs are usually configured/determined based on routers and their links. 

Least-costs:
 - avoid loops (since loop = infinite cost)
 - are destination-based (all costs depend on destination only)
 - form a spanning tree

### Trivial Routes
Routes that are unimportant and can be ignored:
 - Route from router to itself (loopback)
 - Route away from router with only one neighbor (default route)
	 - Default routes sometimes exist when there's multiple routes, but one is always preferred (wifi vs cellular)

### Static Routes
 - Manually entered in by an operator
 - Typically used when operator has specific need (hosts don't usually participate in routing procols) 


## Distance-Vector Routing Protocols

D-V routing protocols are very similar to the Bellman-Ford shortest path algorithm.
[[/cs70/discrete-math/graphs#Bellman Ford Shortest Paths with Negative Edge Lengths|CS70 Notes on Graphs]]

However, Distance-Vector routing is asynchronous and has incomplete state, since each router can collect information simultaneously but only knows about its own local state. This differs from the traditional version of Bellman-Ford, which is serial (only one calculation at one time, and the entire state is known).

The basic table update algorithm for D-V is as follows:
 - Neighbors advertise a route with a particular distance/cost to a particular destination
	 - *do not* advertise to neighbor whos entry is in the nextHop table (avoid split horizon problem)
 - Router adds 1 to advertised distance and saves it in the nextHop table, along with the address of the neighbor that advertised it
 - If a neighbor gives a lower number than the current nextHop, it replaces the previous entry
	 - Exception: any cost given by current best neighbor will overwrite the entry, even if it's larger
	 - Exception to exception: stop counting at some maximum value to avoid counting to infinity when a loop exists
 - Direct routes need to be manually populated to initialize cost


### Failures in D-V

**What happens when the network is unreliable?** 
Sometimes, packets get dropped. An easy solution is to continuously advertise to all neighbors at a certain interval. (This differs from triggered updates- only sending on change. Choosing between the two is a tradeoff of reliability vs efficiency.)
 - Can also combine this with triggers to be most responsive: when table changes, when link becomes available, when link fails

The order in which packets arrive can also be nondeterministic.

**What happens when a link between two routers fail completely?**
We can add a new field to the routing table, **Time To Live (TTL).** Table entries will only be valid until that TTL expires. Then, when a link goes down, the time will run out and the entry will be deleted, so it can then be  replaced by the next best neighbor.
 - Most effective: set TTL to some multiple of the advertisement interval to guarantee that routes have at least a few tries before timing out
 - If a route does go down and the TTL expires, we can **poison** that route by setting its cost to $\infty$. So instead of not advertising a route, we actively advertise that the router doesn't have a route. This makes the information propagate faster than waiting for timeouts.

**How can we deal with the split horizon problem?**
 - Recall that the split horizon problem occurs when the optimal route expires/dies, and an unrelated route advertises a path away from the actual destination 
 - Solution: **Poison reverse**: if a router advertises a loop, set that value to $\infty$ so the next advertisement is immediately accepted  


## Link-State Routing
 - Very common IGP
 - Major examples include IS-IS (intermediate system to intermediate system) and OSPF (open shortest path first)
 - Main principle: if a router had a global view of the network, it could easily compute the path to any destination.
	 - Every router builds a full graph of the network and finds paths from itself to every destination on the graph 
		 - Can use traditional shortest paths algorithms like Dijkstras
	 - Populate forwarding table with next hop: only works if all other routers agree on what the best path is


### How does this compare to distance-vector?
D-V is distributed globally (all nodes do it), but using local data.
Link-State is computed **locally using global data**.
 - Global data includes the state of every link in the network (if it exists, if it's up, and how much it costs)

### Sharing info globally
The hardest part of link-state is getting the global state itself. 
To do this, every router needs to:
 - find out who its neighbors are (exchanges hello messages)
 - tell everyone about neighbors (use **flooding**: when local information changes upon receiving info from a neighbor, send to all other neighbors)
 - Tell everyone about adjacent destinations



### Link State Flooding
Some issues with the brute-force flooding idea:
 - Doesn't scale well with huge networks
 - Since packets are duplicated, the number of packets sent grows exponentially if the branching factor is greater than 1
  - Packets can be dropped on unreliable networks
  - Can't guarantee that individual routers will agree on best paths (see convergence section)

Some solutions:
 - Each router stores a sequence number, and puts it into their packets. If the info packet has a lower sequence number than the current revision, it's already been seen and is ignored. If it's greater, remember the sequence number and send the flood update to neighbors. 
 - Periodically resend floods to guarantee reliability


### Link State Convergence
Some calculations in link-state management take time, and in that time the state can change, causing divergence between routers.

Failure not detected: packets are sent to a dead link
Failure detected but not recomputed: can create dead ends
Failure detected but not globally notified: can create loops
State changes: packets in transit can get stuck if their destination link goes down


## Spanning Tree Protocol

### Learning Switches
  - Unlike Distance-Vector and Link-State protocols, which have static local table states, tables are filled in opportunistically using data packets.
	  - This means that instead of dropping packets to unknown destinations, send the packet to all possible destinations (i.e. flood it). 
		  - Also flood when the recorded nextHop is the same as the message's sender (avoid loops).
	  - Static routes also need to be learned, so on the initial send typically all of the routers will need to be pinged.
	  - Eventually, one of the packets will reach the destination, and information can then be sent backwards so that all routers in the path can learn about the host.
 - Doesn't work when network has loops

### From Learning Switches to Spanning Tree
In order to address the issue that learning switches don't work when the network has cycles, we can use the **spanning tree protocol:** the main idea being that we disable routes until we create a spanning tree of the entire network.

STP is only used in local (layer 2) networks, where bandwidth is generally not a concern and the number of nodes is relatively small, allowing for packet flooding.

Since flooding can find hosts, no static routes are needed anymore.

**Step 1: find least cost paths from every switch to the root**

Introduction:
 - This is basically the Distance-Vector protocol with a single table entry where that entry is the destination, or the switch at the root of the tree.
 - Every switch has a unique orderable ID.
 - Our goal is to first find the root (lowest ID), then find the best path to the root (lowest cost).
Algorithm:
 - All switches begin by thinking they are the root.
 - On receiving a route message from a neighbor:
	 - If the the advertised root is smaller, use it instead.
	 - If it's larger, ignore it.
	 - If it is the same as stored, use normal D-V update rules to minimize the distance, breaking ties by preferring the next hop with the smallest ID.
 - Only the root and switches that think they are the root will generate periodic advertisements. All other switches will forward advertisements when received.

**Step 2: disable data delivery on every link not on a shortest path to root**
 - Each switch:
	 - Enables the link along the best path to root
	 - Enable all links to hosts (anything that is not a switch, i.e. have not sent any advertisements)
	 - Disables every other link

**Step 3:** when a link on the tree fails, start over
 - If a route expires, routers think they are the root again