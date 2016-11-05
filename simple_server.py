#!/usr/bin/env python3
# See https://docs.python.org/3.2/library/socket.html
# for a decscription of python socket and its parameters

import socket
from threading import Thread
from argparse import ArgumentParser
import os
# Use os.path.isfile, os.path.exists
import stat
# Check if a file has others permissions set, os.stat
import sys 
# Get the argument vector (argv) from command line and use

/** Definitions **/
BUFSIZE = 4096
CRLF = '\r\n'
OK = 'HTTP/1.0 200 OK{}{}'.format(CRLF,CRLF)
NOT_FOUND = 'HTTP/1.0 404 Not Found{}{}'.format(CRLF,CRLF)
FORBIDDEN = 'HTTP/1.0 403 Forbidden{}{}'.format(CRLF,CRLF)
MTHD_NOT_ALLOWED = 'HTTP/1.0 405 Method Not Allowed{}{}'.format(CRLF,CRLF)
MOVED = 'HTTP/1.1 301 Moved Permanently{}'.format(CRLF)
NOT_ACCEPTABLE = 'HTTP/1.0 406 Not Acceptable{}'.format(CRLF)


/** Server **/

def processreq(data):
    request_type = str(data).split('\r\n')[0].split(' ')[0] # Identify the request type GET or HEAD
    resource = str(data).split('\r\n')[0].split(' ')[1]
    resource_file = resource.rsplit('/',1)[-1]
    resource_extension = resource_file.rsplit('.',1)[-1]
    
    # Check if Accept header exists
    headers_list = str(data).split('\r\n')
    for header in headers_list:
      if header[:7] == 'Accept:':
        accept_header = header
        break
    # 406 Not applicable
    if len(accept_header):
      if resource_extension not in accept_header:
        response = NOT_ACCEPTABLE
        print response
        return response
      elif resource_extension != 'html' and os.path.exists(resource):
        response = OK + resource_file
        return response

    # Redirection Response
    if resource_file == 'csumn':
      location_header = 'Location: http://www.cs.umn.edu{}{}'.format(CRLF, CRLF)
      response = MOVED + location_header
      print response
      return response

    if request_type == 'GET':
      # Check if resource exists
      if os.path.exists(resource):
        # Check the permission
        if os.access(resource, os.R_OK):
          msg_body = open(resource, "r").read()
          response = OK + msg_body
        else:
          msg_body = open("./403.html", "r").read()
          response = FORBIDDEN + msg_body
      else:
        msg_body = open("./404.html", "r").read()
        response = NOT_FOUND + msg_body

    elif request_type == 'HEAD':
      if os.path.exists(resource):
        if os.access(resource, os.R_OK):
          response = OK
        else:
          response = FORBIDDEN 
      else:
        response = NOT_FOUND

    elif request_type == 'POST':
        response = MTHD_NOT_ALLOWED
    
    else:
        response = 'Error'
    print response
    return response

def client_talk(client_sock, client_addr):
    print('talking to {}\n'.format(client_addr)) # Logging requests
    data = client_sock.recv(BUFSIZE)
    print('Incoming requests:\n')
	  # decode the data and process the request
    req = data.decode('utf-8')
    print req # Server logs requests to STDOUT
	  # process the data, and formulate a response
    response = str(processreq(req))
    response = response.encode("UTF-8")
    client_sock.send(response)

    # clean up
    client_sock.shutdown(1)
    client_sock.close()
    print('connection closed.')

class EchoServer:
  def __init__(self, host, port):
    print('listening on port {}'.format(port))
    self.host = host
    self.port = port

    self.setup_socket()

    self.accept()

    self.sock.shutdown()
    self.sock.close()

  def setup_socket(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind((self.host, self.port))
    self.sock.listen(128)

  def accept(self):
    while True:
      (client, address) = self.sock.accept()
      client_talk(client, address)

if __name__ == '__main__':
  host = 'localhost'
  if len(sys.argv) > 1:
    port = int(sys.argv[1])
  else:
    port = 9001
  EchoServer(host, port)

