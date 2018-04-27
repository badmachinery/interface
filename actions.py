from PyQt5.QtCore import Qt
import socket

import interface
import constants as c
import connection

KEY_MAP = {
    Qt.Key_W: False,
    Qt.Key_A: False,
    Qt.Key_S: False,
    Qt.Key_D: False
    }

BTN_TO_KEY = {
    interface.WASD_BUTTONS_TEXT[0]: Qt.Key_W,
    interface.WASD_BUTTONS_TEXT[1]: Qt.Key_A,
    interface.WASD_BUTTONS_TEXT[2]: Qt.Key_S,
    interface.WASD_BUTTONS_TEXT[3]: Qt.Key_D,
}

KEY_TO_BTN = {
    Qt.Key_W: interface.WASD_BUTTONS_TEXT[0],
    Qt.Key_A: interface.WASD_BUTTONS_TEXT[1],
    Qt.Key_S: interface.WASD_BUTTONS_TEXT[2],
    Qt.Key_D: interface.WASD_BUTTONS_TEXT[3]
}

#Initialized at main.py/Main/initUI
#Consists both of Qt.Key_x and 'str' keys
BTN_MAP = {}

#Actions
current_speed_forward = 1

def get_speed_and_rotation():
    speed = c.ENGINE_SPEED[0]
    rotation = c.SERVO_ANGLE[0]
    for i in KEY_MAP.keys():
        if KEY_MAP[i]:
            if (KEY_MAP[Qt.Key_A]):
                rotation = c.SERVO_ANGLE[-45]
            if (KEY_MAP[Qt.Key_D]):
                rotation = c.SERVO_ANGLE[45]
            if (KEY_MAP[Qt.Key_W]):
                speed = c.ENGINE_SPEED[current_speed_forward]
            if (KEY_MAP[Qt.Key_S]):
                speed = c.ENGINE_SPEED[-1]
    return speed, rotation

def manual_write():
    speed, rotation = get_speed_and_rotation()
    sock.send('s', str(speed))
    sock.send('r', str(rotation))

sock = connection.Socket_connection()
ssh = connection.SSH_connection()
