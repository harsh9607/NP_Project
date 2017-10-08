# Server side program
# Author : Harsh Pathak 
#Socket Programming 
import socket

# Creating a Socket Object , Type : TCP 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# To acquire the local machines IP address and binding it. 
host = socket.gethostname()
s.bind((host,8888))

# server ready to listen to 2 connections at max 
s.listen(3)
print('Server:: waiting for Connections:') 
c , clientaddr = s.accept()   
print('Server::Got a connection from client side')
while True:
 
    data = c.recv(2017)
    print(str(data))
    
    if str(data) == 'bye' :
    	break
    msg2send = raw_input('Enter message for Client :: ')
    c.send(msg2send.encode())
    if str(msg2send) == 'bye' :
    	break
  

print('closing socket !')    
c.close()
