import socket
import sys
import os
import time
import re

# Command line arguments
ds_port = int(sys.argv[1])
db_port = int(sys.argv[2])

# ***** File Parameter ***** #
file_name = "10K.txt" # Please change this when grading

# Get list of available servers from dir-server
app_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
app_client_socket.connect(("apollo.cselabs.umn.edu",ds_port))
lm = "list-servers\r\n"
app_client_socket.sendall(lm)
received = app_client_socket.recv(1064)
received = received.split()
print "### list-servers response from dir-server ###"
print received[0] + '\n' + received[1] + ' ' + received[2] + '\n' + received[3] + ' ' + received[4] + '\r\n'
app_client_socket.close()

# Servers
server_a = (received[1], int(received[2]))
server_b = (received[3], int(received[4]))
client_ip = socket.gethostbyname(socket.gethostname())

# Connect to app-server a
socket_a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_a.connect(server_a)
f = open(file_name, 'rb')
l = f.read(1024)
t1 = 0
while (l):
    start = time.time()	# Measuring performance & data measurement
    socket_a.sendall(l)
    end = time.time()
    l = f.read(1024)
    t = end - start
    t1 += t
f.close()
re = socket_a.recv(1064)
socket_a.close()

# Connect to app-server b
socket_b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_b.connect(server_b)
f = open(file_name, 'rb')
l = f.read(1024)
t2 = 0
while (l):
    start = time.time()	# Measuring performance & data measurement
    socket_b.sendall(l)
    end = time.time()
    l = f.read(1024)
    t = end - start
    t2 += t
f.close()
re = socket_b.recv(1064)
print re
socket_b.close()

# Send set-record to db-server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("atlas.cselabs.umn.edu",db_port))
server1_ip = server_a[0]
port = str(server_a[1])
sr_msg = "set-record " + client_ip + " " + server1_ip + " " + port + " 10 " + str(t1) + "\r\n"
s.sendall(sr_msg)
re = s.recv(1064)
print "### Response of set-record from db-server ###"
print re
s.close()

# Send second set-record to db-server
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(("atlas.cselabs.umn.edu",db_port))
server2_ip = server_b[0]
port2 = str(server_b[1])
sr_msg = "set-record " + client_ip + " " + server2_ip + " " + port2 + " 10 " + str(t2) + "\r\n"
s2.sendall(sr_msg)
re = s2.recv(1064)
print "### Response of set-record from db-server ###"
print re + "\n"
s2.close()

# Send get-record to db-server
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect(("atlas.cselabs.umn.edu",db_port))
gr_msg = "get-records\r\n"
sock1.sendall(gr_msg)
re = sock1.recv(1064)
re = re.replace('\r','\n')
print "### Response of get-record from db-server ###"
print re + "\n"
sock1.close()


