import socket

class Socket:
    def connect(self, _ip, _port):
        self.sock = socket.socket()
        self.sock.connect((_ip, _port))
        self.sock.settimeout(0.01)

    def close(self):
        self.sock.close()

    def reconnect(self):
        self.close()
        self.connect()

    def send(self, symbol, data=''):
        try:
            self.sock.send((symbol + str(data) + '\n').encode('ascii'))
            return True
        except OSError:
            return False

    def receive(self, amount=32):
        try:
            return self.sock.recv(amount).decode('ascii')
        except socket.timeout:
            return ''
