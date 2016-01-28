import socket
import sys
import os
import pickle

class msg_t:
	def __init__(self,msg_type,cur_seq,max_seq,payload_len,payload):
		self.msg_type = msg_type
		self.cur_seq = cur_seq
		self.max_seq = max_seq
		self.payload_len = payload_len
		self.payload = payload

# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (socket.gethostname()), int(sys.argv[1])) 
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# define BUffer Size
BUF_SZ = 1024

# Listen for incoming connections
sock.listen(1)

while True:

	print >>sys.stderr, 'Ready for a connection'
	connection, client_address = sock.accept()
	print 'connection established'
	print >>sys.stderr, 'connection from', client_address
	data = connection.recv(24)
	file_name = data
	print file_name
	current_sequence = 0
	file_size = os.stat(file_name).st_size
	max_sequence = file_size/BUF_SZ

	if file_name in os.listdir(os.getcwd()):
		f = open(file_name,'rb')
		l = f.read(BUF_SZ)

		while l:
			message = msg_t('MSG_TYPE_GET_RESP', current_sequence, max_sequence, len(l), l)
			m_list = [message.msg_type, message.cur_seq, message.max_seq, message.payload_len, message.payload]
			m_str = ""
			for i in range(len(m_list)):
				if i != len(m_list) - 1:
					m_str += str(m_list[i]) + "$$$"
				else:
					m_str += str(m_list[i])
			
			print m_str
 			
			connection.send(m_str)
			current_sequence = current_sequence + 1
			l = f.read(BUF_SZ)

	else:
		connection.sendall('MSG-TYPE-GET-ERR')
	f.close()
	connection.close()







