# Client Side
#RSA ENCRYPTION USED (1024 bits)
import random
import socket
from Crypto.PublicKey import RSA
key = RSA.generate(1024)
publickey2send = key.publickey()

s = socket.socket()

host = socket.gethostname()
port = 8888

# msg to be sent to the user 
#msg = "harsh pathak sending msg to server"

s.connect((host,port))

#Public key exchange 
ServersPubkey = RSA.importKey(s.recv(2048))  
print('Client :: Received the servers public key ')
s.send(publickey2send.exportKey());
print('Key exchange successful ! \n')


data = s.recv(1024)
decrypted = key.decrypt(eval(data))
print(decrypted)

#Authentication begins !
#nonce = random.randint(0,10000)

nonce = str(random.randint(0,10000))
print('Nonce sent = ' + nonce)
E_nonce = ServersPubkey.encrypt(nonce,int(len(nonce)))
s.sendall(str(E_nonce))

temp = s.recv(2017)
R_nonce = key.decrypt(eval(temp))

print('Nonce Received ='+ R_nonce)

if str(R_nonce) == str(nonce) :
	print('Authentication successful !!')

else :
	print('Authentication failed')
	s.close()


while True:
	msg = raw_input('\nEnter your message :: ')
	print('Client :: Sending msg')	
	#ENCRYPTING YOUR MSG
	Tencypted = ServersPubkey.encrypt(msg,int(len(msg)))
	s.sendall(str(Tencypted))
	print('Your message in encrypted form looks like this ->' + str(Tencypted))
    
	if msg == 'bye' :
		break
		

	received_msg = s.recv(1024)
	decrypted = key.decrypt(eval(received_msg))
	
	print('\nClient:: msg received !! decrypted msg -> ' + decrypted + '\n')
	
	if str(decrypted) == 'bye':
		break

	
	

print('closing socket')	
s.close()
