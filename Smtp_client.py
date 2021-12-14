from socket import AF_INET, SOCK_STREAM, socket

#first, we are going to create the socket
print('Client started')
s = socket(AF_INET, SOCK_STREAM)

# we are going to identify the ip address and the port address to connect with the server address  
server_address = (('192.168.189.1',7779))
s.connect(server_address)


#------------------------------------------------------------------------------------#
# here is the messages that we want to send and receive between the server and the client 
message = 'HELO'
s.sendall(message.encode())

reply = s.recv(1024)
if reply == '250'.encode():
    print('SERVER :',reply)
    email_from = input('Your Email: ') #here is the mail that the user enter
    s.sendall(email_from.encode())

    mail_from_acceptance = s.recv(1024)
    if mail_from_acceptance == '250'.encode():
        print('SERVER :',mail_from_acceptance)

        mail_to = input('Reciever Email: ') #the user enter here the receiver mail
        s.sendall(mail_to.encode())
        mail_to_acceptance = s.recv(1024)
        if mail_to_acceptance == '250'.encode():
            print('SERVER :',mail_to_acceptance)

            #Start sending data
            s.sendall('DATA'.encode())
            reply = s.recv(1024)
            if reply == '354'.encode():
                print('SERVER: {}'.format(reply))
                print('SERVER IS READY FOR DATA')

                #Sending data line by line until you send (.)
                
data_line = input('Enter line of data to send: ') # the message that the user want to send to the server 
s.sendall(data_line.encode())


reply = s.recv(1024)
if reply == '250'.encode():
    print('SERVER:', reply)
    
                    
# recieving the extracted data from the server     
          
client_mail = s.recv(1024)
client_ip = s.recv(1024)
clie_port = s.recv(1024)
client_mac = s.recv(1024)







input('Press enter to terminate ... ')
s.close()
print('Terminating ...')




 
