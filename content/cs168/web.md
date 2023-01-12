---
weight: 140
---

## Origins
In 1989, Tim Berners-Lee set out to solve a problem: there was a lot of information being stored digitally, and no way to find or access much of it. He created "Information Management: A Proposal" in which the concept of the "web" was first established.

This proposal had several key parts:
 - not based on a hierarchy
 - allows remote access across networks
 - heterogeneity: different systems can access the same data
 - non-centralization: ability for existing systems to be linked together without a central control
 - access to existing data: ability to get data from existing databases to reduce overhead of adapting new system

**Why was this so successful?**
 - Very flexible; didn't force any changes on existing data, systems, or networks
 - Many systems were built for networks in the first place
 - Integrated interface for scattered information
 - Practical solution to a specific problem
 - Early form of open-source software (free for anyone to use)
 - No over-specification: websites can be structured in many ways
 - No central authority or single underlying system: anyone can add their own systems easily
 - Ability to quickly navigate between different sources

## Basics

**What do we need to create the Web?**
 - A way to represent content with links: HTML
 - A client program to access content: web browsers
 - A way to reference content: URLs
 - A way to host content: servers
 - A protocol to transfer content between servers and clients: HTTP

### URL Syntax

**scheme://host:port/path/resource?query#fragment**
 - Scheme: protocol (https, ftp, smtp...)
 - Host: DNS hostname or IP address
 - Port: 80 for http, 443 for https
 - Path: traditional filesystem hierarchy
 - Resource: desired resource
 - Query: search terms
 - Fragment: subpart of a resource

## HTTP
*Note:* The following information refers to the HTTP 1.0 standard. HTTP 2 is also commonly supported(about 44% adoption), and HTTP 3 is upcoming (5%, mostly Google/Facebook), but they are significant departures in terms of implementation.

**Main idea:**
 - Client-server architecture
 - Client connects to server via TCP on port 80
 - Stateless protocol

### HTTP Request
 - Plaintext, separated with CRLF (CR = Carriage Return, ASCII 13, LF = Line Feed, ASCII 10)
 - Request Line: **Method Resource Protocol**
	 - Method: GET, HEAD, POST...
	 - Resource: what needs to be fetched
	 - Protocol version: HTTP/1.1 or HTTP/1.0
 - Request Headers: provide additional information
 - Body: separated with a blank line; used for submitting data


### HTTP Status
 - Status Line: **Protocol Status Reason**
	 - Protocol: HTTP/1.1 or HTTP/1.0
	 - Status: status code (200, etc)
	 - Reason: human-readable message

### HTTP Methods
 - GET: request to download (body on response only)
 - POST: send data from client to server (body often present in both request and response)
 - HEAD: same as GET except no body is needed in the response (used to check for existence)

### Status Codes
 - 1xx: informational (not defined)
 - 2xx: successful
	 - 200: OK
 - 3xx: redirection
	 - 301: moved permanently
	 - 304: not modified
- 4xx: client error
	- 400: bad request
	- 401: unauthorized
	- 404: not found
- 5xx: server error
	- 500: internal server error


### Caching
Web caching takes advantage of temporal locality: if something is accessed, it'll probably be accessed soon. This is true because the most popular content is accessed far more frequently than non-popular content.

Caching is implemented via two headers:
 - Cache-Control: max-age=(seconds) - 1.1
 - Expires: (absolute time of expiry) - 1.0

We can also specify the following to force skip caches:
 - Cache-Control: no-cache - 1.1
 - Pragma: no-cache - 1.0

Additional settings:
 - If-Modified-Since: (date)
	 - If a resource has changed since date, respond with latest version. Otherwise, respond with 304 (not modified)

![[/cs168/img/Pasted image 20221108140614.png]]


**Proxy servers** make requests on behalf of clients. This creates an extra layer of caching that can server multiple clients more quickly.
 - Reverse proxies are caches close to the servers.
 - Forward proxies are caches close to the clients. (typically done by ISPs)

### CDNs
Content Delivery Networks provide caching and replication as a service.
CDNs are large-scale distributed storage infrastructure that create new domain names for customers. The content provider then rewrites content to reference the new domains instead of the original ones.
 - typically aliased using CNAMEs to make domain names still human-readable
**Pull:**
 - CDN acts like a cache
 - content provider gives CDN an origin URL
 - when a client requests it from CDN:
	 - if cached, serve
	 - if not cached, pull from origin
 - easier to implement (less work for content provider)

**Push:**
 - Content provider uploads content to CDN, who serves it like a normal server
 - provides more control over content

### HTTP Performance
The primary bottleneck is RTT, not transmission delay. Using standard TCP, downloading many small objects takes 2 RTTs per object, which adds up to a lot of time.

Some optimizations can be made:
 - **Concurrent requests:** make many requests in parallel
	 - need to share bandwidth between all concurrent requests
 - **Persistent connections:** maintain TCP connection across multiple requests
	 - can be combined with concurrent requests
	 - default for HTTP 1.1
 - **Pipelined connections:** send multiple requests all at once
	 - can combine small requests into one large request
	 - not used in practice, due to bugs and head-of-line blocking (remaining connections all need to wait for a slow connection in the middle)