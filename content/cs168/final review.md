---
weight: 170
---

## Part 1

Original questions: [final review part 1](https://notes.bencuan.me/cs168/cs168_final_review_fa22.pdf)

### 1.1
**less aggressive** than normal TCP. 

Aggressiveness is determined by the throughput. Higher throughput = more aggressive.

Throughput can be calcuated by dividing the number of bytes over time (or, packets per RTT).

In a normal TCP implementation, the multiplier $M$ is $0.5$.

At full throughput (highest possible window size $W$ before loss occurs), the throughput is $W/RTT$. At minimum throughput during congestion avoidance (right after loss is detected), the throughput is $1/2 \times W/RTT$Q. Therefore, the average throughput for typical TCP is $3/4 \times W/RTT$.

In the modified case, $M=0.25$ so the average is $(0.25+1)/2 \times W/RTT = 5/8\times W/RTT$. Since the throughput is less than TCP, it's less aggressive.

Note that the increase to the additive constant $A=2$ doesn't change average throughput, it only makes the frequency of the AIMD sawtooth cycle twice as fast.


### 1.2
Sending an ACK once every two packets is **both reliable and TCP-compatible**, because of the in-order property of TCP. If the ACK sequence number is greater than that of the two previous packets, it will provide enough information to the recipient to consider both those packets as sent.

### 2
Here's the sketch of a TCP connection between your computer (H) and the Gradescope server (S):
1. SYN from H -> S
2. SYN+ACK <-
3. ACK + HTTP request ->
4.  ACK + HTTP response <-
5. ACK + FIN ->
6. FIN + ACK <-
7. ACK ->


### 3
Start with CWND=1 and SSTHRESH=50. All constants are in terms of numbers of MSS.
![[/cs168/img/Pasted image 20221213144250.png]]

1. 9 ACKs are receieved: CWND += 9, so it becomes 10. (slow start)
2. 8 ACKs are received: CWND += 8, so it becomes 18. (slow start)
3. A timeout occurs: SSTHRESH = CWND/2 = 9, and CWND gets reset to 1.
4. 45 ACKS are received:
	1. Fast recovery until CWND = 10. (first 9 ACKs)
	2. Congestion avoidance:
		1. Next 10 ACKs increase CWND to 11
		2. Next 11 ACKs increase CWND to 12
		3. Next 12 ACKs increase CWND to 13
		4. Final 3 ACKs increase CWND to 13 3/13
5. 10 ACKs are received: CWND = 14 (congestion avoidance)
6. 9 dupACKs are recieved:
	1. Fast recovery after 3 dupACKs --> CWND = $\lfloor 14/2 \rfloor + 3 = 10$, SSTHRESH = $\lfloor$CWND$/2 \rfloor = 7$ 
	2. Remaining 6 dupACKs during fast recovery: CWND += 6 = 16
7. 35 ACKs are received:
	1. Congestion avoidance begins at CWND=7
	2. Next 7 ACKS increase CWND to 8
	3. Next 8 ACKs increase CWND to 9
	4. Next 9 ACKs increase CWND to 10
	5. Final 10 ACKs increase CWND to 11
8. Timeout occurs:
	1. CWND is reset to 1, SSTHRESH = floor(11/2) = 5
9. 8 ACKs received:
	1. First 5 = fast recovery, increase CWND to 6
	2. Next 3 increase to 3/6 => CWND = 6 1/2
10. 2 dupACKs received:
	1. nothing happens (3 required)
11. 4 ACKs are received: 
	1. Congestion avoidance: First 3 increase CWND to 7
	2. Final ACK increases CWND to 7 1/7


### 4
Recall that if the total available bandwidth is $C$ and each flow $i$ has a bandwidth demand $r_i$, then the fair allocation of bandwidth $a_i$ to each flow is calculated as$$a_i = min(f, r_i)$$ where $f$ is the flow's fair share, calculated by the following:
 - Get the average $C/N$ (where $N$ is the number of flows).
 - Subtract all of the $r_i$ from $C$ where $r_i < N$. For each flow that this is done for, subtract one from $N$.
 - For all of the remaining flows, set $f = C/N$.

#### 4.1
1. Find $C/N = 15/4$.
2. See that $r_A = 3$, which is less than $C/N$. So $a_A = 3$ and the new average is $12/3 = 4$.
3. See that $r_B = 4 = C/N$, so $a_B = 4$ and the new average is $8/2 = 4$.
4. See that $r_C = 5 > C/N$, so give it $a_C = C/N = 4$ and the new average is $4/1 = 1$.
5. Give the remaining 4Mbps to the last flow, so $a_D = 4$.

#### 4.2
The process is equivalent to the one above. If the initial $C=17$, then $C/N = 5$ for flows C and D, so they each get 5Mbps instead of 4.

#### 4.3
Basically, we want to simulate fair queuing by dropping packets to match the desired bandwidth from 4.2.

Since $a_i = r_i$ for A, B, and C, we want to use the same bandwidth so $p_i = 0$. 

For flow D, we want $a_D \times (1-p_D) = r_D$. Solve for $p_D$:
$6 \times (1-p_D) = 5$
$1 - p_D = 5/6$ so $p_D = 1/6$ 

### 5
![[/cs168/img/Pasted image 20221213145743.png]]

#### 5.1
If $A_1$ wants to message $A_3$, it will need to broadcast an ARP request to all hosts in A-Net. So $A_2, A_3, R_A$ will all see the request.

#### 5.2
When $A_3$ responds, it is a unicast so only $A_1$ will know its MAC address.

#### 5.3
If $B_1$ wants to message $A_3$, it will need to go through $R_B$ so it first needs to request $R_B$'s MAC address.

#### 5.4
$R_A$ will need to make an ARP request for $A_3$, since it doesn't know $A_3$'s MAC address yet.

#### 5.5
If $A_3$ wants to message $B_2$, it will need $R_A$'s MAC address. However, since an ARP request was made from $R_A$ to $A_3$ already, the MAC is cached and does not need to be re-requested.

#### 5.6
After $B_2$ receives the packet, $R_B$ will have the MACs of $B_1$ and $B_2$ from the requests made in 5.3 and 5.5.

#### 5.7
$R_A$ will have $A_1$ cached from its broadcast from 5.1, and $A_3$ cached from the request made in 5.3.

### 6
Recall that DHCP has 4 parts:
![[/cs168/img/Pasted image 20221210183624.png|300]]
1. Discovery is broadcast (source 0.0.0.0 since no IP is known yet, and destination is 255.255.255.255 since DHCP server also is unknown)
	1. Client MAC is sent as source, with destination as FF:FF:FF:FF
2. Offer is broadcast with source IP of the DHCP server, and destination IP 255.255.255.255 (since server doesn't know who requested it)
3. Request is broadcast with source 0.0.0.0 and 255.255.255.255 to accept the offer
	1. Client MAC is sent as source, with destination of FF:FF:FF:FF (need to broadcast to all DHCP servers, to tell those not selected to reclaim the offered address)
4. Acknowledge message is sent with DHCP server as source, and destination 255.255.255.255
	1. Contains IP address, subnet mask, default gateway IP, dns server IP, and lease time
	2. 


#### 6.1
Discovery and request packets have source 0.0.0.0 and destination 255.255.255.255, so the number of packets is $2H$.

#### 6.2 and 6.3
All DHCP packets are broadcast, so none are unicast.

#### 6.4
Offers and Acks have a defined source IP, and destination 255.255.255.255.

Assuming we have $D$ DHCP servers and $H$ hosts, each server will give an offer to each host (making $D \times H$ offer packets), and each host will receive one ACK (making $H$ acks). So $DH + H$ total.

#### 6.5
All discover and request packets contain their own source MAC, and have a destination of FF:FF:FF:FF. So $2H$ total.

#### 6.6
DHCP makes all broadcasts on the IP layer, so no ARP requests need to be sent.

#### 6.7
All servers on the same L2 network will all receive the same number of DHCP packets, since all packets are broadcast. The numbers are as follows:
 - $H$ hosts each make 1 discovery packet
 - Each of $D$ servers responds to the hosts, making $HD$ offers
 - Each host sends a request, making $H$ requests total
 - Each host receives an ack, making $H$ acks total

### 7
![[/cs168/img/Pasted image 20221213151815.png]]
Alice and Bob both want to access "www.tumblr.com".

#### 7.1
The end goal is to receive an A or AAAA record that translates the domain name into an IP address.

#### 7.2
Root servers will return both an NS record and A record, corresponding to the TLD server for .com.

#### 7.3
The iterative process is as follows: (with edge weights for Alice)
1. DNS client queries DNS server (1)
2. Server queries root (3)
3. Root returns records (3)
4. Server queries TLD (2)
5. TLD returns records (2)
6. Server queries nameserver (1)
7. Nameserver returns an A record (1)
8. Server returns A record to client (1)
So 1+3+3+2+2+1+1+1 = 14 total.

Bob follows exactly the same process, but with different edge weights.

#### 7.4
If Alice is in the US and Bob is in China, the Tumblr server is probably in the US because Bob's latency is higher than Alice's.

#### 7.5
Authoritative DNS servers can use IP geolocation to redirect users to closer content servers, decreasing latency.



## Part 2

[final review part 2](https://notes.bencuan.me/cs168/cs168_final_review2_fa22.pdf)

### True False
1. F, telephone networks use circuit switching and the modern internet uses packet switching.
2. F, transport layer is layer 4.
3. F, the outermost header is the application headers (HTTP etc).
4. T, the only increase/decrease mode that is fair is AIMD.
5. F, UDP does provide checksums.
6. F, HTTP runs over TCP, not UDP.
7. T, DNS runs over UDP since it needs to be responsive.
8. T, DHCP runs over UDP since it's broadcast.
9. F, ARP runs on L2 so no UDP is used.
10. T, ARP requests are broadcast.
11. F, ARP responses are unicast.
12. F, ACK packets can be combined with HTTP requests (which are payloads).
13. F, MX is a mail record that redirects a domain to another domain's mail server.
14. F, removing timers means TCP wouldn't be reliable in the case of timeouts.
15. T, SDN allows additional control of networking within cloud providers; traditional networking relies on vendor code within hardware devices.
16. T, OpenFlow gives access to the forwarding plane.
17.  F, cellular networks store user state on the data plane to route packets to the correct carrier.
18. F, Google's global WAN consists of many different interconnected regions and zones.


### Short Answer
1. Sending 1TB over a 1Gbps link would take 8000 seconds, or about 133 minutes. Driving 45 miles at 25mph would take 108 minutes, so it would be faster.
2. Only TCP provides points 1, 2, and 4. Both provide multiplexing/demux capabilities.
3. ECN is a protocol where routers notify hosts of congestion.
4. HTTP is stateless so it uses cookies to store information across TCP sessions.
5. OpenFlow, see the [[#SDN]] section.
6. Initial DNS requests from hosts are sent to the local DNS server, which begins the iterative query process.
7. DHCP is used to request the laptop's IP address. In the process, the laptop also learns the router's IP address. DNS is used to convert the domain to an IP. ARP is used to find the MAC address of the first router.
8. Throughput for TCP is proportional to $\frac{MSS}{RTT \sqrt{p}}$. This proportion for Connection A is $\frac{1000}{100 \times 0.1} = 100$, and for B it is $\frac{2000}{500 \times .2} = 20$. So Connection A's throughput is 5 times that of Connection B.
   

### HTTP and TCP

#### 3a.
1. SYN sent
2. SYN+ACK received, CWND=2
3. ACK sent with HTTP GET
4. HTTP response received

2 RTT.


#### 3b.
Nonpersistent connections require a new connection for every request, so one is needed for each of the 3 images.

Persistent connections don't need any new connections.

#### 3c.
From 3a, it takes 2 RTT to download the index page.
After the index page is downloaded:

We have three concurrent connections, one for each image. So we only need to consider the time to download one image.
-   The first RTT will correspond to the SYN and SYN-ACK exchange
-   In the second RTT, the client sends the request for the image to the server. The image size is 2 MSS but the server's congestion window is 1. So the server can only send one MSS over.
-   In the third RTT, the client sends an ACK (for the first MSS) back to the server and only now can the server send the second MSS in the image. (Note that receiving the ACK also increases the server's CWND to 2 MSS -- which doesn't matter for this scenario but will if there was more data to send as in the case with the persistent connection)

The pipelined case is the same, but minus the first RTT for the exchange. 

### Detailed Sequence of Packets
1.    ⇉ DHCP discover
2.  ⇇ DHCP offer
3.  ⇉ DHCP request
4.  ⇇ DHCP ack
5.  ⇉ ARP request for DNS IP (to ask about B and C IPs)
6.  **← ARP response from DNS (3rd received)**
7.  → DNS request for B IP
8.  ← DNS response with B IP
9.  ⇉ ARP request for B (in the same subnet, doesn't need to go to router)
10.  ← ARP response from B
11.  → TCP SYN to B
12.  ← TCP SYN+ACK from B
13.  → TCP ACK to B
14.  **→ HTTP request to B (8th sent)**
15.  ← ACK from B (to the request from A)
16.  ← HTTP response from B
17.  → ACK to B (for the HTTP response)
18.  → TCP FIN to B
19.  ← TCP ACK from B (to the FIN)
20.  ← TCP FIN from B
21.  → TCP ACK to B (to the FIN)
22.  → DNS request for C IP
23.  **← DNS response for C IP (11th received)**
24.  ⇉ ARP for Router (since C is in another subnet, need routers MAC)
25.  ← ARP response from Router
26.  → TCP SYN to C
27.  ← TCP SYN+ACK from C
28.  **→ TCP ACK to C (15th sent)**
29.  → HTTP request to C
30.  ← TCP ACK from C (to the request from A)
31.  ← HTTP response from C
32.  → TCP ACK to C
33.  → TCP FIN to C
34.  ← TCP ACK from C
35.  ← TCP FIN from C
36.  → TCP ACK to C

### SDN
In a Software-Defined Network, the **control program** expresses the operator’s intentions for network control by configuring the switches in the **abstract network view** , which is part of the API provided by the **virtualization layer** that is based on the **global network view** it receives from the **network operating system** , which in turn uses the **switch interface (OpenFlow)** to control the physical switches.

![[/cs168/img/Pasted image 20221213172913.png|300]]