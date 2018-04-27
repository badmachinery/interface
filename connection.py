import paramiko
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

    def receive(self):
        return self.sock.recv(32)

class SSH_connection:
    def __init__(self):
        pass

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=c.RASPBERRY_IP, username=c.RASPBERRY_USER,
            password=c.RASPBERRY_PASSWORD, port=c.RASPBERRY_SSH_PORT)

    def send_file(self, filename=c.RASPBERRY_APP_SCRIPT_MAIN, directory=c.RASPBERRY_APP_DIRECTORY):
        sftp = self.client.open_sftp()
        sftp.get(filename, directory)
        sftp.close()

    def execute_command(self, command='python3 ' + c.RASPBERRY_APP_DIRECTORY + '/main.py'):
        transport = self.client.get_transport()
        self.session = transport.open_session()
        self.session.setblocking(0)
        self.session.get_pty()
        self.session.invoke_shell()
        self.session.send(command)

    def stop_execution(self):
        self.session.send('\x03')

    def close(self):
        self.client.close()
