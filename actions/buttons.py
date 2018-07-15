import re
import time

from interface.interface import interface
from interface.consts import *

import actions.vars as vars
import actions.consts as consts

import indy.wlan as wlan

def connect_wlan():
    wlan.startWLAN(consts.WLAN_NAME, consts.WLAN_KEY)
    interface._setStyleSheet(WLAN_BUTTON, WLAN_BUTTON['stylesheet_pressed'])

def connect_ssh():
    vars.ssh.connect(vars.raspberry_ip, consts.RASPBERRY['username'], consts.RASPBERRY['password'], consts.RASPBERRY['ssh_port'])
    interface._setStyleSheet(SSH_BUTTON, SSH_BUTTON['stylesheet_pressed'])
    interface._setEnabled(SSH_IN, True)
    vars.ssh.invoke_shell()

def run_script():
    vars.ssh.send_command('python3 ' + consts.RASPBERRY_APP_DIRECTORY + '/main.py')

    interface._setStyleSheet(SCRIPT_BUTTON, SCRIPT_BUTTON['stylesheet_pressed'])
    interface._setStyleSheet(CAR, CAR['stylesheet_good'])
    interface._setEnabled(SSH_IN, False)

    vars.socket.connect(vars.raspberry_ip, consts.RASPBERRY['socket_port'])
    vars.script_running = True


def send_file_to_raspberry():
    filepath = interface.file_dialog()
    filename = re.sub('.*\/', '', filepath)
    if filename:
        vars.ssh.send_file(filepath, consts.RASPBERRY_APP_DIRECTORY + '/' + filename)
