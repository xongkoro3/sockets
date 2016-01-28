import socket
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Socket created'
# define BUffer Size
buf = 256
# bind the socket to the port
address = (socket.gethostname(), int(sys.argv[1]))
print >>sys.stderr, 'IP address: %s port: %s' % address
s.bind(address)

file_name, address = s.recvfrom(1024)
print 'The file to be downloaded is:' + file_name
f=open(file_name,"rb")
data = f.read(buf)
message_number = 0

while (data):
    if(s.sendto(data,address)):
        data = f.read(buf)
	print str(buf) + ' bytes read and sent.'
	message_number = message_number + 1
print 'Number of messages:' + str(message_number)
s.close()
f.close()
