import paramiko

import actions.consts as consts

class SSH:
    def __init__(self):
        self.invoked = False

    def connect(self, _hostname, _username, _password, _port):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=_hostname, username=_username, password=_password, port=_port)

    def send_file(self, filename, directory=consts.RASPBERRY_APP_DIRECTORY):
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
                return self.shell.recv(1024).decode('utf-8')
        return ''

    def close(self):
        self.client.close()
