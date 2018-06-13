from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QFileDialog, QGridLayout, QPushButton, QMainWindow, QLineEdit, QTextEdit)
import socket
import re
import time

import interface
import interface_constants as ic
import constants as c
import socket_connection
import ssh_connection
import wlan
import vars as v

sock = socket_connection.Socket_connection()
ssh = ssh_connection.SSH_connection()

KEY_MAP = {
Qt.Key_W: False,
Qt.Key_S: False,
Qt.Key_A: False,
Qt.Key_D: False,
 }

mode = c.MODE_MANUAL
script_running = False


def key_pressed(key):
    KEY_MAP[key] = True
def key_released(key):
    KEY_MAP[key] = False

def system_timer_actions():
    # Check connection status
    ip = wlan.getIP(c.RASPBERRY_0_MAC)
    if ip:
        c.RASPBERRY_IP = ip
        interface.main.set_text(QLabel, 'ip_label', 'IP: ' + c.RASPBERRY_IP)
    else:
        interface.main.set_text(QLabel, 'ip_label', ic.IP_LABEL['text'])

    # Get stdout
    newtext = ssh.get_stdout()
    if newtext:
        interface.main.ssh_text.append(newtext)

def communication_timer_actions():

    for key in KEY_MAP.keys():
        if KEY_MAP[key] and key in KEY_HANDLER.keys() and script_running:
            KEY_HANDLER[key]()

    if script_running:
        if not KEY_MAP[Qt.Key_W] and not KEY_MAP[Qt.Key_S]:
            sock.send('S', '')

        if not KEY_MAP[Qt.Key_A] and not KEY_MAP[Qt.Key_D]:
            sock.send('M', '')

    # Get data from raspberry
    if script_running:
        #data = sock.receive(64)
        data = None
        if data:
            if data[0] == 'Q':
                data = re.search(r'Q(.+)\n', data).groups(0)
                v.obstacle_distance_front_left = int(data)
            elif data[0] == 'L':
                data = re.search(r'L(.+)\n', data).groups(0)
                v.obstacle_distance_left = int(data)
            elif data[0] == 'R':
                data = re.search(r'R(.+)\n', data).groups(0)
                v.obstacle_distance_right = int(data)

    # Update interface with new data
    interface.main.set_text(QLabel, 'f_obstacle_label', str(v.obstacle_distance_front))
    interface.main.set_text(QLabel, 'l_obstacle_label', str(v.obstacle_distance_left))
    interface.main.set_text(QLabel, 'r_obstacle_label', str(v.obstacle_distance_right))

def key_handler_w():
    sock.send('F', '')

def key_handler_s():
    sock.send('B', '')

def key_handler_a():
    sock.send('L', '')

def key_handler_d():
    sock.send('R', '')

def key_handler_shift():
    sock.send('+', '')

def key_handler_control():
    sock.send('-', '')

# Stops script execution on raspberry
def key_handler_c():
    global script_running
    script_running = False
    sock.send('E', '')
    sock.close()
    interface.main.make_button_pressed('script_button', False)
    interface.main.make_object_enabled(QLineEdit, 'ssh_in', True)
    interface.main.car.setStyleSheet(ic.CAR['stylesheet'])

def key_handler_k():
    sock.send('R', '')

def key_handler_u():
    sock.send('W', '')


KEY_HANDLER = {
    Qt.Key_W: key_handler_w,
    Qt.Key_S: key_handler_s,
    Qt.Key_A: key_handler_a,
    Qt.Key_D: key_handler_d,
    Qt.Key_Shift: key_handler_shift,
    Qt.Key_Control: key_handler_control,
    Qt.Key_C: key_handler_c,
    Qt.Key_K: key_handler_k,
    Qt.Key_U: key_handler_u,
}

#   @@@@
# Interface button handlers
#   @@@@

def connect_wlan():
    wlan.startWLAN(c.WLAN_NAME, c.WLAN_KEY)
    interface.main.make_button_pressed('wlan_button')

def connect_ssh():
    ssh.connect()
    interface.main.make_button_pressed('connect_ssh_button')
    interface.main.make_object_enabled(QLineEdit, 'ssh_in', True)
    ssh.invoke_shell()

def run_script():
    global script_running, mode
    ssh.send_command('python3 ' + c.RASPBERRY_APP_DIRECTORY + '/main.py')
    interface.main.make_button_pressed('script_button')
    sock.connect()
    interface.main.make_object_enabled(QLineEdit, 'ssh_in', False)
    interface.main.car.setStyleSheet(ic.CAR['stylesheet_good'])
    script_running = True
    mode = c.MODE_MANUAL

def send_file_to_raspberry():
    filepath = interface.main.file_dialog()
    filename = re.sub('.*\/', '', filepath)
    if filename:
        ssh.send_file(filepath, c.RASPBERRY_APP_DIRECTORY + '/' + filename)

def send_command():
    '''
    TODO Remake
    '''
    ssh.send_command(interface.main.ssh_in.text())
    interface.main.ssh_in.setText('')
