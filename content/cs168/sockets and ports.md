---
weight: 70
---

## Network Ports
Switches and routers have **physical ports** where links connect to switches.
The OS supports **logical ports** where applications connect to the operating system's network stack.

## Sockets
A **socket** is an OS mechanism that creates and manages logical ports. When an app wants access to the network, a socket is opened and associated with a **port number**. All incoming packets to that port number are then sent to the socket it's associated with.

Sockets are an abstraction layer that allow processes in the OS to communicate over the network.
 - Includes `connect`, `listen`, `accept`, `send`, `recv` API calls
 - Clients initiate new connections to servers; servers listen, accept, and dispatch connections to many clients at once
 - Connections pipe data bidirectionally between a process on a client and a process on a host
 - Sockets are uniquely identified by IP:port combination; client port is usually randomly assigned, whereas server port is fixed and already known by the client.

Logical ports are a part of the socket abstraction. Port numbers are included in the L3 packet header.