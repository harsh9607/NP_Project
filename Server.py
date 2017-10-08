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
 
c , clientaddr = s.accept()   
while True:
    print('Server:: waiting for Connections:')
  
  #c , clientaddr = s.accept()    #tuple
    #(client,(ip,port))=sock.accept()
    print('Server::Got a connection from client side')
    c.send('You are Connected to Harsh101 server services')
    data = c.recv(2017)
    print(str(data))
    c.send('Got your msg , Thanks for connecting ')
    print('Served out client !')
    
c.close()

