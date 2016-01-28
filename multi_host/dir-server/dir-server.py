import socket
import sys
import os
import time

# create a socket object
dir_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "apollo.cselabs.umn.edu"
port = int(sys.argv[1])                                           
dir_server_address = (host, port)
# bind to the port
dir_server_socket.bind(dir_server_address)                                 

# queue up to 5 requests
dir_server_socket.listen(5)                                           

list_servers = []
# establish a connection
while True:
    s, addr = dir_server_socket.accept()
    msg = s.recv(1064)
    print msg    
    if "register" in msg:
        # from app-server
        s.send("success\r\n")    
        msg = msg.split()
        list_servers.append((msg[1],msg[2]))
        s.close()
    else:
        # from app-client
	msg = "success "
	for i in range(len(list_servers)):
		for j in range(len(list_servers[i])):
			msg += str(list_servers[i][j]) + " "
	s.send(msg)
        s.close()

