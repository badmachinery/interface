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

    def init_labels(self):
        self.ip_label = QLabel(ic.IP_LABEL_TEXT, self)
        self.ip_label.setGeometry(
            ic.IP_LABEL_HPOS, ic.IP_LABEL_VPOS,
            ic.LABEL_HSIZE, ic.LABEL_VSIZE)
        self.ip_label.setStyleSheet(ic.IP_LABEL_STYLE)

    def init_buttons(self):
        self.wlan_button = QPushButton(ic.WLAN_BUTTON_TEXT, self)
        self.wlan_button.setGeometry(
            ic.WLAN_BUTTON_HPOS, ic.WLAN_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.wlan_button.setStyleSheet(ic.WLAN_BUTTON_STYLE)

        self.connect_ssh_button = QPushButton(ic.CONNECT_SSH_BUTTON_TEXT, self)
        self.connect_ssh_button.setGeometry(
            ic.CONNECT_SSH_BUTTON_HPOS, ic.CONNECT_SSH_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.connect_ssh_button.setStyleSheet(ic.CONNECT_SSH_BUTTON_STYLE)

        self.script_button = QPushButton(ic.SCRIPT_BUTTON_TEXT, self)
        self.script_button.setGeometry(
            ic.SCRIPT_BUTTON_HPOS, ic.SCRIPT_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.script_button.setStyleSheet(ic.SCRIPT_BUTTON_STYLE)

        self.file_button = QPushButton(ic.FILE_BUTTON_TEXT, self)
        self.file_button.setGeometry(
            ic.FILE_BUTTON_HPOS, ic.FILE_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.file_button.setStyleSheet(ic.FILE_BUTTON_STYLE)

    def init_buttons_actions(self):
        self.wlan_button.pressed.connect(a.connect_wlan)
        self.connect_ssh_button.pressed.connect(a.connect_ssh)
        self.script_button.pressed.connect(a.run_script)
        self.file_button.pressed.connect(a.send_file_to_raspberry)

    def init_ssh_console(self):
        self.ssh_in = QLineEdit(self)
        self.ssh_in.setGeometry(
            ic.SSH_IN_HPOS, ic.SSH_IN_VPOS,
            ic.SSH_IN_HSIZE, ic.SSH_IN_VSIZE)
        self.ssh_in.setStyleSheet(ic.SSH_IN_STYLE)
        self.ssh_in.editingFinished.connect(a.send_command)
        self.ssh_in.setEnabled(False)

        self.ssh_text = QTextEdit('', self)
        self.ssh_text.setGeometry(
            ic.SSH_TEXT_HPOS, ic.SSH_TEXT_VPOS,
            ic.SSH_TEXT_HSIZE, ic.SSH_TEXT_VSIZE)
        self.ssh_text.setStyleSheet(ic.SSH_TEXT_STYLE)
        self.ssh_text.setReadOnly(True)

    def init_timers(self):
        self.sending_timer = QTimer(self)
        self.sending_timer.timeout.connect(a.sending_timer_actions)
        self.sending_timer.start(c.TIMER_INTERVAL)

        self.system_timer = QTimer(self)
        self.system_timer.timeout.connect(a.system_timer_actions)
        self.system_timer.start(c.TIMER_INTERVAL * 5)

    def keyPressEvent(self, e):
        a.key_pressed(e.key())

    def keyReleaseEvent(self, e):
        a.key_released(e.key())

    def write_cycle(self):
        a.sending_timer_actions()

    def make_button_pressed(self, button, status=True):
        if button == 'script_button':
            if status:
                self.script_button.setStyleSheet(ic.SCRIPT_BUTTON_STYLE_PRESSED)
            else:
                self.script_button.setStyleSheet(ic.SCRIPT_BUTTON_STYLE)
        elif button == 'wlan_button':
            self.wlan_button.setStyleSheet(ic.WLAN_BUTTON_STYLE_PRESSED)
        elif button == 'connect_ssh_button':
            self.connect_ssh_button.setStyleSheet(ic.CONNECT_SSH_BUTTON_STYLE_PRESSED)

    def make_edit_line_enabled(self, status):
        self.ssh_in.setEnabled(status)

    def file_dialog(self):
        return QFileDialog.getOpenFileName(self)[0]

    def set_label_text(self, label, text):
        if label == 'ip_label':
            self.ip_label.setText(text)


app = QApplication(sys.argv)
main = Main()
