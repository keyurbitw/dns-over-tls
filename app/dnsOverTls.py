import os, socket, ssl, sys, struct
import dns.message
import dns.rdatatype
    
def queryDnsOverTls(domain=os.getenv('DOMAIN_NAME'), dns_server='1.1.1.1', port=853):
    # Create a DNS query
    query = dns.message.make_query(domain, dns.rdatatype.A)
    query_data = query.to_wire()

    # Set up the TLS context
    context = ssl.create_default_context()

    # Connect to the DNS server over TLS v1.3
    with socket.create_connection((dns_server, port)) as sock:
        with context.wrap_socket(sock, server_hostname=dns_server) as ssock:
            print(ssock.version())
            # Send the DNS query
            ssock.sendall(struct.pack("!H", len(query_data)) + query_data)

            # Receive the response length (first two bytes)
            response_len = ssock.recv(2)
            response_len = struct.unpack("!H", response_len)[0]

            # Receive the full DNS response
            response = ssock.recv(response_len)

    # Parse the DNS response
    answer = dns.message.from_wire(response)
    
    if answer:
        for rrset in answer.answer:
            for rr in rrset:
                response = rr
    else:
        response = "No Valid DNS Response Received."
    
    return str(response)