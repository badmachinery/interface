import re
import time

from interface.interface import interface
from interface.consts import *

import actions.vars as vars
import actions.consts as consts
import actions.keys as keys

import indy.wlan as wlan


def handle_keys():
    if vars.script_running:
        for key in vars.key_map.keys():
            if vars.key_map[key] and key in keys.KEY_HANDLER.keys():
                keys.KEY_HANDLER[key]()

        if not vars.key_map[Qt.Key_W] and not vars.key_map[Qt.Key_S]:
            vars.socket_send_status = vars.socket.send('S')

        if not vars.key_map[Qt.Key_A] and not vars.key_map[Qt.Key_D]:
            vars.socket.send('M')


def get_sensors_data():
    if vars.script_running:
        data = vars.socket.receive()
        #data = None
        if data:
            if data[0] == 'F':
                data = re.search(r'Q(.+)\n', data).groups(0)
                vars.sensor_front_data = int(data)
            elif data[0] == 'L':
                data = re.search(r'L(.+)\n', data).groups(0)
                vars.sensor_left_data = int(data)
            elif data[0] == 'R':
                data = re.search(r'R(.+)\n', data).groups(0)
                vars.sensor_right_data = int(data)

        #interface.setText(F_OBSTACLE_LABEL['type'], F_OBSTACLE_LABEL['name'], str(vars.sensor_front_data))
        #interface.setText(L_OBSTACLE_LABEL['type'], L_OBSTACLE_LABEL['name'], str(vars.sensor_left_data))
        #interface.setText(R_OBSTACLE_LABEL['type'], R_OBSTACLE_LABEL['name'], str(vars.sensor_right_data))

def send_command():
    vars.ssh.send_command(interface.getText(SSH_IN['type'], SSH_IN['name']))
    interface._setText(SSH_IN['type'], SSH_IN['name'], '')

def handle_script_fall():
    vars.script_running = False
    vars.socket.close()

    interface._setStyleSheet(SCRIPT_BUTTON['type'], SCRIPT_BUTTON['name'], SCRIPT_BUTTON['stylesheet'])
    interface._setStyleSheet(CAR['type'], CAR['name'], CAR['stylesheet_bad'])
    interface._setEnabled(SSH_IN['type'], SSH_IN['name'], True)
