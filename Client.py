# Client Side

import socket

s = socket.socket()

host = socket.gethostname()
port = 8888


s.connect((host,port))

while True:
	msg = raw_input('Enter your message :: ')
	print('Client side running ! Sending msg')	
	#print(s.recv(2017))
	s.send(msg.encode())
	if msg == 'bye' :
		break
		
	received_msg = s.recv(2017)
	print(str(received_msg))
	if str(received_msg) == 'bye':
		break

	
	

print('closing socket')	
s.close()
