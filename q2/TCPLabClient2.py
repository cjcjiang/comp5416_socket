from socket import *
import time
serverName = '127.0.0.1'
serverPort = 12010
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')



for i in range(20):
    clientSocket.send(sentence) ## Do not specify serverName,serverPort
    modifiedSentence = clientSocket.recv(1024)
    print 'From Server:', modifiedSentence
    time.sleep(1)
    
clientSocket.close()

