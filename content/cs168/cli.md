---
weight: 20
linkTitle: "CLI Tools"
title: "Networking Command Line Tools"
---

## nslookup
Resolves a hostname to an IP address (or the reverse).

Basic usage: `nslookup <hostname> <DNS server>`
 - Example:
```
❯ nslookup cs168.io
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   cs168.io
Address: 185.199.109.153
Name:   cs168.io
Address: 185.199.110.153
Name:   cs168.io
Address: 185.199.111.153
Name:   cs168.io
Address: 185.199.108.153
```

Reverse lookup: `nslookup <ip>`
```
❯ nslookup 185.199.110.153
153.110.199.185.in-addr.arpa    name = cdn-185-199-110-153.github.com.
```



## host
Used for DNS lookup (converting between IP addresses and domain names).

`host -t ns <HOSTNAME>`

```
❯ host -t ns google.com
google.com name server ns2.google.com.
google.com name server ns4.google.com.
google.com name server ns3.google.com.
google.com name server ns1.google.com.
```


## ping
Measures RTT (round trip time) between host and remote server by sending ICMP (internet control message protocol) packets


## traceroute
Traces the route that packets take from computer to destination.
 - Shows router IP addresses and hop times
 - Asterisks = packet lost when being sent to router
 - Uses TTL (time to live) field in IP header; gets decremented by 1 at each router
 - packets are discarded when TTL=0 to avoid loops

```
❯ traceroute google.com
traceroute to google.com (142.251.214.142), 30 hops max, 60 byte packets
 1  Docsis-Gateway.hsd1.ca.comcast.net (10.0.0.1)  1.275 ms  1.326 ms  1.346 ms
 2  96.120.89.97 (96.120.89.97)  15.764 ms  18.875 ms  18.963 ms
 3  96.110.176.209 (96.110.176.209)  19.056 ms  19.095 ms  19.135 ms
 4  162.151.78.129 (162.151.78.129)  19.219 ms  19.160 ms  19.243 ms
 5  be-232-rar01.santaclara.ca.sfba.comcast.net (162.151.78.253)  15.767 ms  17.192 ms  18.799 ms
 6  96.108.99.249 (96.108.99.249)  26.164 ms  21.468 ms  19.513 ms
 7  be-299-ar01.santaclara.ca.sfba.comcast.net (68.86.143.93)  21.295 ms  16.004 ms  15.695 ms
 8  96.97.98.246 (96.97.98.246)  12.520 ms 69.241.75.46 (69.241.75.46)  22.875 ms 96.112.146.26 (96.112.146.26)  22.982 ms
 9  * * *
10  142.251.224.30 (142.251.224.30)  22.203 ms 209.85.252.250 (209.85.252.250)  23.538 ms sfo03s32-in-f14.1e100.net (142.251.214.142)  21.774 ms
```

