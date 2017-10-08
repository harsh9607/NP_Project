# Server side program
# Author : Harsh Pathak 
#Socket Programming 
import random
import socket
from Crypto.PublicKey import RSA
key = RSA.generate(1024)
publickey2send = key.publickey()



# Creating a Socket Object , Type : TCP 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# To acquire the local machines IP address and binding it. 
host = socket.gethostname()
s.bind((host,8888))

# server ready to listen 
s.listen(2)

# Accepting connections
print('Server :: waiting for Connections:')
c , clientaddr = s.accept()   
print('Server::Got a connection from client side')

#Public Key Exchanges  
print('Server :: Sending my Public key')
c.send(publickey2send.exportKey());
ClientsPubKey = RSA.importKey(c.recv(2048))
print('Server :: Received Cilents Public key as well !')
print('Key exchange successful ! \n')



dummy = 'Oh hello there..harsh here i had encypted this..but..perhaps you decrypted it...let me authenticate if you are Rizwan sir only !'
Tencypted = ClientsPubKey.encrypt(dummy,int(len(dummy)))
c.sendall(str(Tencypted))
print('Your msg in encypted form looks like this ->' + str(Tencypted))

# Authentication Begins !! 
temp = c.recv(2017)
d_nonce = key.decrypt(eval(temp))
print('nonce received ->' + d_nonce )
print('Authenticating !!!')

E_d_nonce = ClientsPubKey.encrypt(d_nonce,int(len(d_nonce)))
c.sendall(str(E_d_nonce))


while True:
     
    data = c.recv(2017)
    decrypted = key.decrypt(eval(data))
    print('Server :: msg  received !!decrypted message -> '+ decrypted)
    print('\n')
    if str(decrypted) == 'bye' :
    	break
    msg2send = raw_input('Enter message for Client :: ')
    Tencypted = ClientsPubKey.encrypt(msg2send,int(len(msg2send)))
    c.sendall(str(Tencypted))
    print('\nServer :: Sending msg in encrypted form')
    print('Your encrypted msg looks like this ->' + str(Tencypted))
    print('\n')

  

print('closing socket !')    
c.close()
