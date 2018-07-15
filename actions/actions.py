import re
import time

from interface.interface import interface
from interface.consts import *

import actions.vars as vars
import actions.consts as consts
import actions.keys as keys
import actions.utility as utility

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
        vars.socket_data + vars.socket.receive()
        if vars.socket_data:
            print(vars.socket_data)
            while vars.socket_data[0] in ['F', 'L', 'R']:
                vars.socket_data, symbol, data = utility.get_subdata(vars.socket_data)
                if symbol == 'F':
                    vars.sensor_front_data = data
                    print('F', data)
                if symbol == 'R':
                    vars.sensor_right_data = data
                    print('R', data)
                if symbol == 'L':
                    vars.sensor_left_data = data
                    print('L', data)
                if symbol == None:
                    break

def _update_sensor_icon(sensor, data):
    if data > 50 or data == -1:
        interface._setStyleSheet(sensor, sensor['stylesheet'])
    elif 20 < data <= 50:
        interface._setStyleSheet(sensor, sensor['stylesheet_far'])
    elif data <= 20:
        interface._setStyleSheet(sensor, sensor['stylesheet_close'])

def update_sensors_icons():
    _update_sensor_icon(SENSOR_FRONT, vars.sensor_front_data)
    _update_sensor_icon(SENSOR_LEFT, vars.sensor_left_data)
    _update_sensor_icon(SENSOR_RIGHT, vars.sensor_right_data)


def send_command():
    vars.ssh.send_command(interface.getText(SSH_IN))
    interface._setText(SSH_IN, '')

def handle_script_fall():
    vars.script_running = False
    vars.socket.close()

    interface._setStyleSheet(SCRIPT_BUTTON, SCRIPT_BUTTON['stylesheet'])
    interface._setStyleSheet(CAR, CAR['stylesheet_bad'])
    interface._setEnabled(SSH_IN, True)
