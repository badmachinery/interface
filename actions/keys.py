import re
import time

from interface.interface import interface
from interface.consts import *

import actions.vars as vars
import actions.consts as consts

import indy.wlan as wlan


def key_handler_w():
    vars.socket.send('F')

def key_handler_s():
    vars.socket.send('B')

def key_handler_a():
    vars.socket.send('L')

def key_handler_d():
    vars.socket.send('R')

def key_handler_shift():
    vars.socket.send('+')

def key_handler_control():
    vars.socket.send('-')

def key_handler_i():
    vars.socket.send('I')

def key_handler_c():
    vars.script_running = False
    vars.socket.send('E')
    vars.socket.close()

    interface._setStyleSheet(SCRIPT_BUTTON, SCRIPT_BUTTON['stylesheet'])
    interface._setStyleSheet(CAR, CAR['stylesheet'])
    interface._setEnabled(SSH_IN, True)

def key_handler_k():
    vars.socket.send('R', '')

def key_handler_u():
    vars.socket.send('W', '')


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
    Qt.Key_I: key_handler_i,
}
