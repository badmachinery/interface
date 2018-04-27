from PyQt5.QtCore import Qt
import socket

import interface
import constants as c

TIMER_INTERVAL = 50    #In milliseconds

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

current_speed = 1

#Initialized at main.py/Main/initUI
#Consists both of Qt.Key_x and 'str' keys
BTN_MAP = {}

#Actions

class Connection:
    def __init__(self):
        self.sock = socket.socket()
        try:
            #self.sock.connect(('192.168.1.45', 9090))
            #self.sock.connect(('192.168.137.243', 9090))
            self.sock.connect(('192.168.137.153', 9090))
        except Exception:
            self.sock.connect(('192.168.137.223', 9090))
        self.sock.settimeout(0)

    def send(self, *data):
        try:
            data_block = b''
            for s in data:
                data_block += str(s).encode('ascii') + '/'.encode('ascii')
            self.sock.sendall(data_block)
        except Exception:
            print('Exception')

con = Connection()

def manual_write(interface):
    res = []
    speed = c.ENGINE_SPEED[0]
    #speed = '0'
    rotation = c.SERVO_ANGLE[0]
    for i in KEY_MAP.keys():
        if KEY_MAP[i]:
            if (KEY_MAP[Qt.Key_A]):
                rotation = c.SERVO_ANGLE[-45]
            if (KEY_MAP[Qt.Key_D]):
                rotation = c.SERVO_ANGLE[45]
            if (KEY_MAP[Qt.Key_W]):
                speed = c.ENGINE_SPEED[current_speed]
                #speed = '1'
            if (KEY_MAP[Qt.Key_S]):
                speed = c.ENGINE_SPEED[-1]

    #con.send(speed, rotation)

    #con.sock.send(speed.encode('ascii'))

    con.sock.send(('s' + str(speed) + '\n').encode('ascii'))
    con.sock.send(('r' + str(rotation) + '\n').encode('ascii'))

    #con.sock.send('s'.encode('ascii') + str(speed).encode('ascii') + '/'.encode('ascii') + 'r'.encode('ascii') + str(rotation).encode('ascii') + '/'.encode('ascii'))
    #arduino.send_data(speed, rotation)
