import paramiko
import constants as c

class SSH_connection:
    def __init__(self):
        pass

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=c.RASPBERRY_IP, username=c.RASPBERRY_USER,
            password=c.RASPBERRY_PASSWORD, port=c.RASPBERRY_SSH_PORT)

    def send_file(self, filename, directory=c.RASPBERRY_APP_DIRECTORY):
        sftp = self.client.open_sftp()
        sftp.put(filename, directory)
        sftp.close()

    def execute_command(self, command='python3 ' + c.RASPBERRY_APP_DIRECTORY + '/main.py'):
        self.stdin, self.stdout, self.stderr = self.client.exec_command(command)
        return

    def stop_execution(self):
        self.stdin.write('\x03')

    def close(self):
        self.client.close()
