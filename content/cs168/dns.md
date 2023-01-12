---
weight: 130
---

DNS (domain name system) was created as a solution to make IP addresses human-readable for users. 

In the early days, DNS took the form of a standardized address book called hosts.txt maintained by Elizabeth Feinler at the Network Information Center. This included an IP address, user-friendly name, and properties such as supported protocols. Whenever someone wanted to look up a name, they would query for hosts.txt. However, this got troublesome due to increased burden on the NIC team, high bandwidth usage as the number of hosts increased, and having a single point of failure.


## Hierarchy
**Names are hierarchical:** Domains get more specific from right to left

**Authority is hierarchical:** Each level has a responsible party (.edu, berkeley.edu, etc)
 - The DNS root is controlled by ICANN
 - Top Level Domains (TLDs) are controlled by over 1500 authorities, such as Educause for edu domains and Verisign for .net/.com domains.
 - A **zone** corresponds to an administrative authority responsible for a contiguous portion of the authority. An example of a zone is `*.berkeley.edu` which controls all domains ending in berkeley.edu.

**Infrastructure is hierarchical:** the DNS system is composed of many name servers which each are responsible for one part of the hierarchy.


## Name Lookup
1. A client looks up a domain by querying their **resolving name server** (usually run by ISP)
2. The resolving name server runs a **recursive query** (actually iterative) by repeatedly doing the following:
	1. Get a request from the current server (starting at the root)
	2. If the server knows the answer, return the answer.
	3. Otherwise, move onto the next server and return the result of that query.

There are several main classes of name servers:
 - Root server knows all the TLD servers
 - TLD server knows about a particular TLD (such as .edu)
 - Authoritative servers know information about their zone (such as \*.berkeley.edu) and map domain names to IPs.
 - 


## The DNS Protocol

C / python socket API:
`result = gethostbyname("hostname.com")`: deprecated but still common, limited to IPv4
`error = getaddrinfo("hostname.com", NULL, NULL, &result)`: more modern, not limited to IPv4

Standard DNS server: BIND (berkeley internet name domain server)
 - basically a daemon/server process
 - listens on port 53 (UDP)

Messages may be either a query or response (QR bit in header 0 or 1 respectively). 

Data is stored in **resource records** (RRs) that are a tuple of (type, name, value, ttl, class).
 - type is A, NS, etc.
 - name is the domain name
 - value is the IP address
 - ttl is how long the record is valid for 
 - class is used for other network types (not really used in practice)

### Step by step
1. Client queries resolving name server
2. Resolving name server queries root server, requesting an A record
3. Response: list of NS records corresponding to TLD/authoritative servers, as well as an additional A record (IP for name server we should ask next)
4. Repeat until the desired authoritative server is contacted, and an A record is returned

### Registering a domain
 - Companies can purchase/request IP blocks from ISP
 - Register domain with a registrar
 - Run 2 authoritative name servers for the domain (often handled by registrar/external service)
 - Registrar will insert pairs of NS and A records into the TLD name servers

### Reverse lookups
Using the PTR record, we can convert an IP address to a hostname.
 - name = dot-quad IP address listed backwards (138.110.1.200 -> 200.1.110.138)
 - name is followed by `.in-addr.arpa`


### Record Types
**A:** "address record" - maps hostname to IP address
**AAAA:** Same as A, but for ipv6
**NS:** "nameserver" - maps domain to DNS server
**CNAME:** "canonical name" - way for aliasing from one hostname to another hostname
**DNAME:** maps an entire subtree to another subtree
**MX:** "mail exchanger": redirects to another mail server
**TXT:** human-readable information, often used to prove ownership of domain
**SRV:** used for arbitrary services (servicename.transportprotocol.hostname)

## Availability, Scalability, Performance
**DNS should be:**
 - Highly available: accessible at all times (otherwise the internet breaks down)
 - Highly scalable: most devices on the internet will use DNS
 - Highly performant: lookups should be fast and take little bandwidth

**How do we do this?** Just add more servers.
 - Domains have at least two name servers each
 - Have multiple servers per domain such that if one domain goes down, others are still available
 - Have multiple root servers (currently, there are 13), and make each of these root servers a network of physical servers around the world. (For example, the E root has over 300 servers with the same IP address using anycast)
 - Caching: Increases performance by reducing the number of requests/iterative queries being made. Caches can be introduced at any layer, including the host. 

## Example

Let's say our local host wants to access the domain `ischool.berkeley.edu`.
1. Our host will send a recursive query to the resolving name server (`cdns01.comcast.net`), asking for the A record for `ischool.b.e`.
2. The resolving nameserver will check the cache, and if present, return the result.
3. If cache entry not present, the resolving name server queries the root server requesting the A record for `ischool.b.e`.
4. The root server sends back the DNS tuples `(NS, edu, k.edu-servers.net)`, and `(A, k.edu-servers.net, aaa.aaa.aaa.aaa)`.
5. The resolving nameserver queries `k.edu-servers.net` requesting the A record for `ischool.b.e`.
6. The TLD server sends back NS and A records for `berkeley.edu`.
7. The resolving nameserver queries `adns1.berkeley.edu`.
8. Berkeley's DNS server sends back the desired A record, along with a TTL.