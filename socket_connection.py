import socket

import constants as c

class Socket_connection:
    def __init__(self):
        #self.connect()
        pass

    def connect(self):
        self.sock = socket.socket()
        self.sock.connect((c.RASPBERRY_IP, c.RASPBERRY_SOCKET_PORT))
        self.sock.settimeout(0)

    def close(self):
        self.sock.close()

    def reconnect(self):
        self.close()
        self.connect()

    def send(self, symbol, data):
        self.sock.send((symbol + data + '\n').encode('ascii'))

    def receive(self, amount=32):
        return self.sock.recv(amount)
