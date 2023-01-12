---
weight: 80
title: "Interdomain Routing (BGP)"
---

In [[intradomain routing]], we primarily focused on processes for intradomain routing- where switches discover paths within their own networks.

Now, we'll discuss **interdomain routing** between many autonomous systems.

## Autonomous Systems (AS)
As a review, an autonomous system is a domain that represents a network under a single administrative control. Every AS is assigned a unique ASN by ICANN.

A **stub AS** only sends and receives packets on behalf of its directly connected hosts. Some examples include companies and universities.

On the other hand, a **Transit AS** carries packets on behalf of other ASes. These can vary greatly in scale from global to regional, and may be organized hierarchically.

There are three basic kinds of relationships between ASes: customer (pays for usage), provider (is paid by others for usage), and peers (don't pay each other and are assumed to exchange roughly equal traffic).

![[/cs168/img/Pasted image 20220928162353.png|300]]

Tier 1 ASes are at the top of the hierarchy:
 - typically span multiple continents
 - do not have providers
 - are peered with most other tier 1 ASes
 - examples: AT&T, Verizon...

## Goals for Interdomain Routing
Similarly to intradomain routing, we still want to be able to find valid routes (with no loops or dead ends), and optimize for least cost paths.

In addition, there are two main goals:
 - Scalability: must be feasible for use in the entire internet
 - Policy compliance: routes must reflect business goals of ASes


### Scaling
The key to scaling is host [[addressing (ip)]]. Since IP addresses have hierarchical subnet support, instead of enumerating every single IP address, we can simply say something like "all x.y.00/16 addresses are owned by Comcast" and redirect all traffic within that subnet to Comcast.

Additionally, the hierarchical addressing structure allows for a further optimization of pointing to higher tier ASes, since each of them will know how to reach lower tier ASes.

One possible downside to hierarchical addressing is that we are not able to aggregate 'multi-homed' networks with more than one provider. 

### Policy
Some ASes will have preferences on where to route their traffic, even if they may not be objectively optimal in terms of least cost.

There are two main principles for typical policies:
1. ASes don't accept traffic unless they're getting paid: only carry traffic to customers, and only use peering links to send traffic between customers.
2. Either make money or send money when sending traffc: only send to provider if no peers or customers are available. 

Also, ASes want autonomy and privacy: the ability to choose their own policies, and to not explicitly announce their policy choices to others.

Policy controls how routes are imported and exported.
 - **Import (selection)**: choosing which path to use
	 - controls how traffic leaves the network
 - **Export:** which path to advertise
	 - controls how traffic enters the network (what traffic this AS carries)




# BGP
![[07 Networking#BGP]]

Essentially, BGP is very similar to Distance-Vector with some key differences:
 - BGP aggregates destinations using hierarchical addressing.
 - BGP does not pick the shortest path routes. Instead, it chooses the route based on policy.
 - Rather than doing distance-vector routing, BGP is **path-routing**: rather than advertising distance, advertise the entire path.
	 - This allows for easier loop detection: if an advertised path includes the current AS, it will discard it.
 - Sometimes, for policy reasons, an AS may choose not to advertise a route to a destination.


### BGP Sessions
There are several gateway protocol session types:
 - **eBGP** (external) sessions are between border routers in **different ASes**. Routers learn about external routes, and exchange routes to different destination prefixes.
	 - Only border routers need to speak eBGP.
 - **iBGP** (internal) sessions are within the **same AS**. Routers learn which border routers to use, and distribute externally learned routes internally.
	 - Commonly in practice, route reflectors are run for iBGP: essentially they are dedicated machines for each domain that handle all iBGP connections between them. So rather than having all routers map to each other, they just point to the route reflector.
 - IGP for intradomain routing (see [[intradomain routing]])

Each router has two routing tables: nextHops for internal destinations (IGP), and egress routers for external destinations (iBGP).


### BGP Messages
**Basic BGP messages:**
 - Open: establish BGP session
 - Notification: report unusual conditions
 - Update: informs neighbors of new routes (announcements) or inactive routes (withdrawal)
	 - Basic format: maps IP to route attributes (parameters used during route selection)
	 - Local attributes: kept private
	 - Public attributes: shared with other routers

**Attributes:**
 - ASPATH: path vector that lists all ASes a route advertisement has traversed in reverse order. Carried in route advertisements
 - LOCAL_PREF: used to choose between different AS paths
	 - only carried in iBGP messages since ASes don't want to publicize their preferences
 - MED: Multi-Exit Discriminator
	 - used when ASes have multiple links between one another
	 - lower MED = better
	 - set by announcing AS
 - IGP Cost: "hot potato" routing- minimize cost of traversing internal network to border router
	 - may conflict with MED

Route selection in priority order
1. Pick highest LOCAL_PREF
2. Pick shortest ASPATH
3. Pick lowest IGP cost to next hop
4. Pick lowest MED (other router preferences)
5. Tie break by router ID



### Issues with BGP
 - Security: no guarantee that AS owns advertised prefixes, or that it will follow the advertised path (prefix hijacking)
 - Performance: policy-based, not cost-based (so advertised path length can be misleading)
 - Configuration: BGP misconfiguration is a major source of internet outages
 - Reachability and convergence not guaranteed if Gao-Rexford not followed

## Gao-Rexford Rules
Gao-Rexford rules describe common practice in import/export policies:
 - When importing (selecting) a route to a destination, customer > peer > provider.
	 - ASes may use additional rules for tiebreaking
 - When exporting routes:
	 - if route advertised by customer, export route to everyone.
		 - paths go in any direction in tree
	 - if route advertised by peers or providers, only export route to customers.
		 - paths point downward in tree

If all ASes follow G-R rules, the following guarantees are made in the steady state:
 - routes are "valley free": TODO
 - reachability: any two ASes can communicate
 - convergence: all routers agree on paths

Assume that:
 - customer-provider relationships are acyclic
 - tier 1 ASes are at the top and all peer with one another

### Policy Oscillation
If we don't follow Gao-Rexford rules, 