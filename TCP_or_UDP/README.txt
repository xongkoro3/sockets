1. Introduction
A TCP based server&client, and a UDP based server&client is developed in Python. The client downloads a file from the server. The mechanism I use to transfer the message protocol is by processing it into string. I use delimiter "$$$" to separate. For example <msg_type>$$$<cur_seq>$$$<max_seq>$$$<payload_len>. Wireshark is used to measure the performance difference for same files between TCP connection and UDP connection.

2. Execution
On the terminal
#TCP:
$./server_tcp.py <port>
$./client_tcp.py <server-ip> <port> <filename>

#UDP:
$./server_udp.py <port>
$./client_udp.py <server-ip> <port> <filename>

3. File hierarchy
TCP_or_UDP/  
    server/
        server_tcp.c
  	server_udp.c
    client/
        client_tcp.c
      	client_udp.c

4. Instruction
1) Please make sure the file to be downloaded is in the folder or specified path.
2) The running time depends on the machine and network environment.

