from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QFileDialog, QGridLayout, QPushButton, QMainWindow, QLineEdit, QTextEdit)

from interface.interface import interface
from interface.consts import *

import actions.actions as actions
import actions.buttons as buttons
import actions.timers as timers

def buildAll():
    buildWindow()
    buildLabels()
    buildButtons()
    buildLineEdits()
    buildTextEdits()
    buildTimers()
    interface.showWindow()
    timers.start()

def buildWindow():
    interface.resizeWindow(WINDOW['hres'], WINDOW['vres'])
    interface._setWindowTitle(WINDOW['title'])
    interface.setWindowStylesheet(WINDOW['stylesheet'])

def buildLabels():
    interface.createLabel(IP_LABEL)
    interface.createLabel(SENSOR_FRONT)
    interface.createLabel(SENSOR_LEFT)
    interface.createLabel(SENSOR_RIGHT)
    interface.createLabel(CAR)
    interface.createLabel(PIXEL)

def buildButtons():
    interface.createButton(WLAN_BUTTON)
    interface._getElement(WLAN_BUTTON).pressed.connect(buttons.connect_wlan)

    interface.createButton(SSH_BUTTON)
    interface._getElement(SSH_BUTTON).pressed.connect(buttons.connect_ssh)

    interface.createButton(SCRIPT_BUTTON)
    interface._getElement(SCRIPT_BUTTON).pressed.connect(buttons.run_script)

    interface.createButton(FILE_BUTTON)
    interface._getElement(FILE_BUTTON).pressed.connect(buttons.send_file_to_raspberry)

def buildLineEdits():
    interface.createLineEdit(SSH_IN)
    interface._getElement(SSH_IN).editingFinished.connect(actions.send_command)
    interface._setEnabled(SSH_IN, False)

def buildTextEdits():
    interface.createTextEdit(SSH_TEXT)
    interface._setReadOnly(SSH_TEXT, True)

def buildTimers():
    interface.createTimer(COMMUNICATION_TIMER['name'])
    interface._getElement(COMMUNICATION_TIMER).timeout.connect(timers.communication)

    interface.createTimer(SYSTEM_TIMER['name'])
    interface._getElement(SYSTEM_TIMER).timeout.connect(timers.system)

    interface.createTimer(CHECK_TIMER['name'])
    interface._getElement(CHECK_TIMER).timeout.connect(timers.check)
