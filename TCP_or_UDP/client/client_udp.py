from socket import *
import sys
import select
import time

### Command Line Parameters ###
server_address = (str(sys.argv[1]), int(sys.argv[2]))
filename = str(sys.argv[3])
# Buffer 
buf = 256
# Create socket
s = socket(AF_INET, SOCK_DGRAM)
# Send the filename to server
s.sendto(filename, server_address)

# Open the file to write
f = open(filename,'wb')
# Receive file data from server
data,addr = s.recvfrom(buf)
total_time = 0
try:
    while(data):
        f.write(data)
        s.settimeout(2)
	start_time = time.time()
        data,addr = s.recvfrom(buf)
	end_time = time.time()
	t =  end_time - start_time
	total_time += t
except timeout:	
    print str(total_time)
    f.close()
    s.close()
    print "File Downloaded"


