from socket import *

serverName = 'ec2-52-65-60-139.ap-southeast-2.compute.amazonaws.com'
serverPort = 12010
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence1 = '1111111111'
clientSocket.send(sentence1)
responseMessage = clientSocket.recv(1024)
print 'From Server, response 1:', responseMessage

sentence2 = '11111111111111111111'
clientSocket.send(sentence2)
responseMessage = clientSocket.recv(1024)
print 'From Server, response 2:', responseMessage

# sentence3 = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
# clientSocket.send(sentence3)
# responseMessage = clientSocket.recv(1024)
# print 'From Server, response 3:', responseMessage

clientSocket.close()
