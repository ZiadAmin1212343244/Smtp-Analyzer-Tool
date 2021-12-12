
import socket
server_ip = socket.gethostbyname(socket.gethostname())

from socket import AF_INET, SOCK_STREAM, socket

print('Server started')
s = socket(AF_INET, SOCK_STREAM)
print('TCP Socket created')

print('Server Is bound to IP:', server_ip)

#s.bind(('127.0.0.1', 7779))
s.bind((server_ip, 7779))

backlog = 0
s.listen(backlog)
client_socket,client_addr = s.accept()
print('New client connected from %s:%d' % client_addr)

client_ip = client_addr[0]

recv_buffer_length = 1024
            #--------------------------------------------------------------------------------------------#
                                    
                                    ###### SMTP PROTOCOL #####
reply = client_socket.recv(1024)
if reply == 'HELO'.encode():
    print('CLIENT "{}": {}'.format(client_ip,reply))
    client_socket.sendall('250'.encode())

mail_from = client_socket.recv(1024)
print('MAIL FROM <{}>'.format(mail_from))
client_socket.sendall('250'.encode())

mail_to = client_socket.recv(1024)
print('RCPT <{}>'.format(mail_to))
client_socket.sendall('250'.encode())

data_command = client_socket.recv(1024)
if data_command == 'DATA'.encode():
    print('CLIENT "{}": {}'.format(client_ip,data_command))
    client_socket.sendall('354'.encode())

#Begin recieveing data

data_line = client_socket.recv(1024)
data_line = data_line.decode('UTF-8')
client_socket.sendall('250'.encode())
                #------------------------------------------------------------------------------------#


#Extracting Data
mail_from = mail_from.decode('UTF-8')
mail_to = mail_to.decode('UTF-8')

EMail = 'Email FROM <{}>: \nEmail TO <{}>: \nMessage: {}'.format(mail_from,mail_to,data_line)
Client_IP = client_ip
Client_Port = client_addr[1]
from scapy.all import *
Client_MAC = getmacbyip(client_ip)

print('\n\n')
print('EMail')
print('-'*70)
print(EMail)
print('-'*70)
print('Client Information')
print('Client_IP: ',Client_IP)
print('Client_Port: ',Client_Port)
print('Client_MAC: ',Client_MAC)
print('-'*70)



client_socket.sendall(EMail.encode())
client_socket.sendall(str(client_ip).encode())
client_socket.sendall(str(Client_Port).encode())
client_socket.sendall(str(Client_MAC).encode())

input('Press enter to terminate ... ')
s.close()
print('Terminating ...')


