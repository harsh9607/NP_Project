# Client Side

import socket

s = socket.socket()

host = socket.gethostname()
port = 8888

# msg to be sent to the user 
#msg = "harsh pathak sending msg to server"

s.connect((host,port))

while True:
	msg = raw_input('Enter your message :: ')
	print('Client side running ! Sending msg')	
	print(s.recv(2017))
	s.send(msg.encode())
	
s.close()
