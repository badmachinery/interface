import sys
import re
import time
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QFileDialog, QGridLayout, QPushButton, QMainWindow, QLineEdit, QTextEdit)

import interface_constants as ic
import actions as a
import constants as c
import wlan

# bla bla

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.init_timers()

    def init_UI(self):
        self.init_window()
        self.init_labels()
        self.init_buttons()
        self.init_buttons_actions()
        self.init_ssh_console()

        self.show()

    def init_window(self):
        self.resize(ic.APP_HRES, ic.APP_VRES)
        self.setWindowTitle(ic.WINDOW_TITLE)
        self.setStyleSheet(ic.WINDOW_STYLE)

    def create_label(self, params):
        label = QLabel(params['text'], self)
        label.setObjectName(params['name'])
        label.setGeometry(params['hpos'], params['vpos'], params['hsize'], params['vsize'])
        label.setStyleSheet(params['stylesheet'])
        return label

    def init_labels(self):
        self.ip_label = self.create_label(ic.IP_LABEL)
        self.f_obstacle_label = self.create_label(ic.F_OBSTACLE_LABEL)
        self.l_obstacle_label = self.create_label(ic.L_OBSTACLE_LABEL)
        self.r_obstacle_label = self.create_label(ic.R_OBSTACLE_LABEL)
        self.car = self.create_label(ic.CAR)

    def create_button(self, params):
        button = QPushButton(params['text'], self)
        button.setObjectName(params['name'])
        button.setGeometry(params['hpos'], params['vpos'], params['hsize'], params['vsize'])
        button.setStyleSheet(params['stylesheet'])
        return button

    def init_buttons(self):
        self.wlan_button = self.create_button(ic.WLAN_BUTTON)
        self.connect_ssh_button = self.create_button(ic.CONNECT_SSH_BUTTON)
        self.script_button = self.create_button(ic.SCRIPT_BUTTON)
        self.file_button = self.create_button(ic.FILE_BUTTON)

    def init_buttons_actions(self):
        self.wlan_button.pressed.connect(a.connect_wlan)
        self.connect_ssh_button.pressed.connect(a.connect_ssh)
        self.script_button.pressed.connect(a.run_script)
        self.file_button.pressed.connect(a.send_file_to_raspberry)

    def init_ssh_console(self):
        self.ssh_in = QLineEdit(self)
        self.ssh_in.setObjectName(ic.SSH_IN['name'])
        self.ssh_in.setGeometry(
            ic.SSH_IN['hpos'], ic.SSH_IN['vpos'],
            ic.SSH_IN['hsize'], ic.SSH_IN['vsize'])
        self.ssh_in.setStyleSheet(ic.SSH_IN['stylesheet'])
        self.ssh_in.editingFinished.connect(a.send_command)
        self.ssh_in.setEnabled(False)

        self.ssh_text = QTextEdit(ic.SSH_TEXT['text'], self)
        self.ssh_text.setObjectName(ic.SSH_TEXT['text'])
        self.ssh_text.setGeometry(
            ic.SSH_TEXT['hpos'], ic.SSH_TEXT['vpos'],
            ic.SSH_TEXT['hsize'], ic.SSH_TEXT['vsize'])
        self.ssh_text.setStyleSheet(ic.SSH_TEXT['stylesheet'])
        self.ssh_text.setReadOnly(True)

    def init_timers(self):
        self.communication_timer = QTimer(self)
        self.communication_timer.timeout.connect(a.communication_timer_actions)
        self.communication_timer.start(c.TIMER_INTERVAL)

        self.system_timer = QTimer(self)
        self.system_timer.timeout.connect(a.system_timer_actions)
        self.system_timer.start(c.TIMER_INTERVAL * 5)

    def keyPressEvent(self, e):
        a.key_pressed(e.key())

    def keyReleaseEvent(self, e):
        a.key_released(e.key())

    def write_cycle(self):
        a.sending_timer_actions()

    def make_button_pressed(self, name, status=True):
        button = self.findChild(QPushButton, name=name)
        if status:
            button.setStyleSheet(ic.BUTTONS[name]['stylesheet_pressed'])
        else:
            button.setStyleSheet(ic.BUTTONS[name]['stylesheet'])

    def set_text(self, type, name, text):
        self.findChild(type, name=name).setText(text)

    def make_object_enabled(self, type, name, status):
        self.findChild(type, name=name).setEnabled(status)

    def file_dialog(self):
        return QFileDialog.getOpenFileName(self)[0]


app = QApplication(sys.argv)
main = Main()
