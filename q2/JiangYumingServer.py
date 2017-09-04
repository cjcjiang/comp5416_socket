from socket import *
import thread


def handler(connectionSocket, addr):
    while 1:
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)

if __name__ == '__main__':
    serverPort = 12010
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print 'The server is ready to receive'
    while 1:
        print 'New thread waiting for connection, listening on port', serverPort
        connectionSocket, addr = serverSocket.accept()
        print 'Connected from:', addr
        thread.start_new_thread(handler, (connectionSocket, addr))
