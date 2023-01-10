

## Google's Network


## Software Defined Networking


## Datacenters
Datacenters refer to computing infrastructure that is in the same physical location, but is shared by many users and applications.

Datacenters require specialized networks that are different from typical networks in the following ways:
 - Administered by a single organization: high degree of control over the network, end hosts, and the placement of sources
 - High density of scale in a single location
 - Much less heterogeneity: servers may have 1-2 orders of magnitude of performance range rather than 5-6 in general cases
 - Extreme emphasis on performance

**The primary goal** of a datacenter network is to allow servers to communicate with any other server in the datacenter at full link capacity.

### Datacenter Traffic
**North-south traffic:** between datacenter and outside world
**East-west traffic:** between different servers inside the datacenter
 - several orders of magnitude larger than North-South traffic
**Wide Area Network (WAN):** private network connecting multiple datacenters owned by the same authority

### Properties
**Diameter:** max number of hops between any two server nodes (lower = less latency)
**Bisection width:** minimum number of links cut to partition the network into two equal halves (higher = better, harder to split datacenter + more resilience)
**Bisection bandwidth:** minimum bandwidth between any two equal network halves
 - **Full bisection bandwidth**: when a datacenter has a bisection bandwidth of $N/2 \times R$ ($N$ servers, $R$ link capacity per server), such that servers can communicate at the full capacity $R$ 

### Implementations
**Big Switch Approach:** have one central switch controlling all servers. Very impractical for large scales

**Tree Approach:** main switch has several subswitches, each controlling some servers. Impractical due to single point of failure, lack of scalability

**Fat Tree Network:** like a tree, but each layer has a similar number of switches
![[Pasted image 20221213000816.png]]
 - Provides full bisection bandwidth, and is scalable
 - All switches have the same number of ports, which is low
 - All link speeds are the same and low
 - Many equal length, mostly independent paths between any two nodes
 - Creates some challenges with routing
	 - Solution: use hierarchical addressing for clusters of servers; SDN controller programs forwarding tables at each switch
	 - **Equal Cost Multi Path (ECMP)** protocol: load balance flows across equal cost paths. All packets from a flow follow the same path 

### Problems

**Queuing delay:** compounds with the number of hops, and greater than propagation delay for datacenter-scale short hops

**TCP congestion control:** TCP fills queues which makes the first problem worse. Solutions:
 - React to explicit feedback from routers (ECN)
 - React to delay instead of loss (Google BBR)

## Cellular
Cellular networks originate over 50% of web traffic, connecting over 5 billion users with mobile devices. 

Over the generations, rate (bits per second) and density (devices per unit area) have increased 10x, whereas latency has decreased by 10x.

### Participants
**Mobile Network Operator (MNO):** operates infrastructure, and offers connectivity as a service

**User Equipment (UE):** devices that users connect to network with
 - International Mobile Subscriber Identity (IMSI) uniquely identifies users, and is stored in a SIM card


### MNO Infrastructure
![[Pasted image 20221213002438.png]]

### Wireless Communication
 - Data is transmitted over assigned carrier frequencies
	 - Challenges: noise, attenuation, interference, fading, distortion
 - Shared medium: cellular networks use reservation-based sharing


### End to End Operation

1. Registration
	1. UE signs up with a home MNO
	2. MNO learns IMSI and associated user information
	3. UE and MNO exchange secret keys
2. Attachment
	1. UE sends a request to a nearby tower
	2. MNO control plane authenticates IMSI and assigns IP address
	3. Control plane programs path to gateway, and enforces service plan rate limits
3. Data Transfer
	1. Cell tower schedules flows based on carrier
4. Mobility
	1. If UE signal quality decreases (e.g. user moved), tower redirects UE to a better one
	2. Handover protocol reprograms path seamlessly (IP address unchanged)
5. Roaming
	1. If UE moves out of home MNO's coverage area, they may be able to use another MNO's towers under a roaming agreement
	2. Home MNO shares keys with roaming MNO, and pays for the service