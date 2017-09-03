from socket import *
from threading import *

serverPort = 12010
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024)

    print sentence

    capitalizedSentence = sentence.upper()

    print capitalizedSentence

    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
