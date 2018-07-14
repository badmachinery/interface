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
    interface.createLabel(F_OBSTACLE_LABEL)
    interface.createLabel(L_OBSTACLE_LABEL)
    interface.createLabel(R_OBSTACLE_LABEL)
    interface.createLabel(CAR)
    interface.createLabel(PIXEL)

def buildButtons():
    interface.createButton(WLAN_BUTTON)
    interface.findChild(WLAN_BUTTON['type'], name=WLAN_BUTTON['name']).pressed.connect(buttons.connect_wlan)

    interface.createButton(SSH_BUTTON)
    interface.findChild(SSH_BUTTON['type'], name=SSH_BUTTON['name']).pressed.connect(buttons.connect_ssh)

    interface.createButton(SCRIPT_BUTTON)
    interface.findChild(SCRIPT_BUTTON['type'], name=SCRIPT_BUTTON['name']).pressed.connect(buttons.run_script)

    interface.createButton(FILE_BUTTON)
    interface.findChild(FILE_BUTTON['type'], name=FILE_BUTTON['name']).pressed.connect(buttons.send_file_to_raspberry)

def buildLineEdits():
    interface.createLineEdit(SSH_IN)
    interface.findChild(SSH_IN['type'], name=SSH_IN['name']).editingFinished.connect(actions.send_command)
    interface._setEnabled(SSH_IN['type'], SSH_IN['name'], False)

def buildTextEdits():
    interface.createTextEdit(SSH_TEXT)
    interface._setReadOnly(SSH_TEXT['type'], SSH_TEXT['name'], True)

def buildTimers():
    interface.createTimer(COMMUNICATION_TIMER['name'])
    interface.findChild(COMMUNICATION_TIMER['type'], name=COMMUNICATION_TIMER['name']).timeout.connect(timers.communication)

    interface.createTimer(SYSTEM_TIMER['name'])
    interface.findChild(SYSTEM_TIMER['type'], name=SYSTEM_TIMER['name']).timeout.connect(timers.system)

    interface.createTimer(CHECK_TIMER['name'])
    interface.findChild(CHECK_TIMER['type'], name=CHECK_TIMER['name']).timeout.connect(timers.check)
