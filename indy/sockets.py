import socket

class Socket:
    def connect(self, _ip, _port):
        self.sock = socket.socket()
        self.sock.connect((_ip, _port))
        self.sock.settimeout(0)

    def close(self):
        self.sock.close()

    def reconnect(self):
        self.close()
        self.connect()

    def send(self, symbol, data=''):
        try:
            self.sock.send((symbol + data + '\n').encode('ascii'))
            return True
        except OSError:
            return False

    def receive(self, amount=32):
        return self.sock.recv(amount)
