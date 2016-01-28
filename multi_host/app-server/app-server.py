import socket
import sys
import os
from random import randint

# dir-server port number
ds_port = int(sys.argv[1])

# app-server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
app_server_host = socket.gethostbyname(socket.gethostname())
app_server_port = randint(9000,10000)	#Randomly select an integer within the 9000 to 10000 range
app_server_address = (app_server_host, app_server_port)
print "### app-server address ###"
print >>sys.stderr, '"<%s>, <%s>"\n' % app_server_address

# Register on dir-server
sock.connect(("apollo.cselabs.umn.edu",ds_port))
rm = "register " + app_server_host + " " + str(app_server_port) + "\r\n" 
sock.sendall(rm)
confirm = sock.recv(1064)
print "### Confirmation from dir-server for register-message ###"
print confirm + "\n"

sock.close()

# Get data from app-client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(app_server_address)
s.listen(5)
while True:
    client, addr = s.accept()
    msg = client.recv(1064)
    client.send("10K Data received at app-server")
    print msg

