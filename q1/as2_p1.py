from socket import *

serverName = 'ec2-52-65-60-139.ap-southeast-2.compute.amazonaws.com'
serverPort = 12010
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Please enter your student number:')
clientSocket.send(sentence)
responseMessage = clientSocket.recv(1024)
print 'From Server:', responseMessage
clientSocket.close()
