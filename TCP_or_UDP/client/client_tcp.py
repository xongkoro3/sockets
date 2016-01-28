import socket
import sys
import os
import time
import pickle


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening

server_address = (str(sys.argv[1]), int(sys.argv[2]))
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

file_name = str(sys.argv[3])
print file_name
f = open(file_name,"wb")
message_number = 0

try:
	sock.sendall(file_name)
	
	data = sock.recv(1063)

	if data == '-MSG-TYPE-GET-ERR':
		print '-MSG-TYPE-GET-ERR'
		f.close()
		os.remove(file_name)
		sock.close()
	else:
		start_time = time.time()
		print_string = " RX "
		while data:
			print "Data:" + str(len(data))
			print data
			data_list = data.split("$$$")
			#print "Data List:" + str(data_list)
			f.write(data_list[4])
			data = sock.recv(1063)
			message_number = message_number + 1

finally:
	print "Message number: " + str(message_number)
	f.close()
	sock.close()
	end_time = time.time()
	total_time = end_time - start_time
	print total_time

