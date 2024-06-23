# DNS-Over-TLS (DoT)
A python code that implements DoT.

## Overview
DNS queries are sent over a plaintext connection. DNS over TLS (DoT) is a way to send DNS queries over an encrypted connection. With DoT, the encryption happens at the transport layer, where it adds TLS encryption on top of a TCP connection.

## Implementation
1. *Start an instance of Flask listening on 0.0.0.0:8080 with /DoT endpoint*
2. *Construct a DNS query from the provided domain in the query and record type (A record).*
3. *Creates a default SSL context for establishing a secure connection.*
4. *Connect to the CloudFlare DNS Server over TLS.*
    - *Opens a TCP connection to the DNS server on the specified port (853 for DoT).*
    - *Wrap the socket with SSL/TLS.*
5. *Send and Receive the DNS Query.*
6. *Parse the DNS Response.*
7. *Send the parsed response to the Flask instance*

## Getting Started

### Prerequisites
- Docker
- Python3

### Running Docker Instance
`docker run -p 8080:8080 -it keyurbitw/dns-over-tls`

## Verification

### Commands
Run the below commands from another terminal on your local.


`$ curl -XGET "localhost:8080/DoT?domain=example.com"`

`$ curl -XGET "localhost:8080/DoT?domain=gmail.com"`

`$ curl -XPOST 'localhost:8080/DoT?domain=google.com'`

### Sample Logs
We can see the below logs in the container.

`
TLSv1.3
172.17.0.1 - - [23/Jun/2024 15:49:24] "POST /DoT?domain=example.com HTTP/1.1" 200
`

`
TLSv1.3
172.17.0.1 - - [23/Jun/2024 15:49:24] "POST /DoT?domain=gmail.com HTTP/1.1" 200
`

`
TLSv1.3
172.17.0.1 - - [23/Jun/2024 15:49:37] "POST /DoT?domain=google.com HTTP/1.1" 200
`
