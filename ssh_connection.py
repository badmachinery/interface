import paramiko
import constants as c

class SSH_connection:
    def __init__(self):
        self.invoked = False

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=c.RASPBERRY_IP, username=c.RASPBERRY_USER,
            password=c.RASPBERRY_PASSWORD, port=c.RASPBERRY_SSH_PORT)

    def send_file(self, filename, directory=c.RASPBERRY_APP_DIRECTORY):
        sftp = self.client.open_sftp()
        sftp.put(filename, directory)
        sftp.close()

    def invoke_shell(self):
        self.shell = self.client.invoke_shell()
        self.invoked = True

    def send_command(self, command):
        if self.invoked:
            self.shell.send(command + '\n')

    def get_stdout(self):
        if self.invoked:
            if self.shell.recv_ready():
                return self.shell.recv(1024).decode('ascii')
            else:
                return ''
        else:
            return ''

    def close(self):
        self.client.close()
