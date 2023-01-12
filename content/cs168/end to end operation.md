---
weight: 160
---

Suppose we have the following scenario:
 - Host H1 boots up
 - Fetches small file from H5
 - Goes idle
 - Fetches two small files from H2
![[/cs168/img/Pasted image 20221210190305.png]]


Here's what will happen:
1. DHCP to get configuration
	1. UDP Discover => broadcast 
	2. UDP Offer from H4 <- H1
	3. UDP Request => broadcast
	4. UDP ack <- H1
2. ARP for DNS server
	1. ARP request for H3 => broadcast
	2. H3 ARP response <- unicast to H1
3. Resolve H5
	1. UDP DNS request for H5.com => H3
	2. UDP DNS response <- H1
4. ARP for R1
	1. ARP request for R1 => broadcast
	2. ARP response from R1 <- H1
5. TCP connection to H5
	1. TCP SYN => H5
	2. TCP SYNACK <- H1
	3.  TCP ACK => H5
6. HTTP request to H5
	1. TCP HTTP GET => H5
	2. TCP ACK <- H1
	3. HTTP response <- H1
	4. ACK => H5
	5. (after download completes and connection becomes idle for a while) FIN => H5
7. TCP disconnect from H5
	1. ACK <- H1
	2. FIN <- H1
	3. ACK => H5
The rest of the steps are extremely similar to the above.
9. Resolve H2
10. ARP for H2
11. TCP to H2
12. HTTP to H2
13. HTTP to H2 (2)
14. TCP disconnect from H\2