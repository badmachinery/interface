# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QGridLayout, QPushButton, QMainWindow)

import interface
import geometry as g
import actions as a
import constants as c

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initTimer()
        self.mode = c.MODE_MANUAL

    def initUI(self):
        self.resize(g.APP_HRES, g.APP_VRES)
        self.setWindowTitle('Connector')

        self.connection_button = QPushButton(interface.CONNECT_SSH_BUTTON_TEXT, self)
        self.connection_button.setGeometry(
            interface.CONNECT_SSH_BUTTON_HPOS, interface.CONNECT_SSH_BUTTON_VPOS,
            g.BTN_HSIZE, g.BTN_VSIZE)
        self.connection_button.setStyleSheet(interface.CONNECT_SSH_BUTTON_STYLE)
        self.connection_button.pressed.connect(self.connect_ssh)

        self.socket_button = QPushButton(interface.CONNECT_SOCKET_BUTTON_TEXT, self)
        self.socket_button.setGeometry(
            interface.CONNECT_SOCKET_BUTTON_HPOS, interface.CONNECT_SOCKET_BUTTON_VPOS,
            g.BTN_HSIZE, g.BTN_VSIZE)
        self.socket_button.setStyleSheet(interface.CONNECT_SOCKET_BUTTON_STYLE)
        self.socket_button.pressed.connect(self.connect_socket)

        self.run_button = QPushButton(interface.RUN_BUTTON_TEXT, self)
        self.run_button.setGeometry(
            interface.RUN_BUTTON_HPOS, interface.RUN_BUTTON_VPOS,
            g.BTN_HSIZE, g.BTN_VSIZE)
        self.run_button.setStyleSheet(interface.RUN_BUTTON_STYLE)
        self.run_button.pressed.connect(self.run_script)

        self.go = False

        self.show()

    def initTimer(self):
        self.write_timer = QTimer(self)
        self.write_timer.timeout.connect(self.write_cycle)
        self.write_timer.start(c.TIMER_INTERVAL)

    def keyPressEvent(self, e):
        if e.key() in a.KEY_MAP.keys():
            a.KEY_MAP[e.key()] = True
        else:
            if e.key() == Qt.Key_Shift:
                a.current_speed_forward += 1
                if (a.current_speed_forward > 3):
                    a.current_speed_forward = 3
            if e.key() == Qt.Key_Control:
                a.current_speed_forward -= 1
                if (a.current_speed_forward < 1):
                    a.current_speed_forward = 1
            if e.key() == Qt.Key_C:
                self.go = False
                a.sock.close()
                a.ssh.stop_execution()

    def keyReleaseEvent(self, e):
        if e.key() in a.KEY_MAP.keys():
            a.KEY_MAP[e.key()] = False

    def write_cycle(self):
        if self.go and self.mode == c.MODE_MANUAL:
            a.manual_write()

    def connect_ssh(self):
        a.ssh.connect()
        self.connection_button.setStyleSheet(interface.CONNECT_SSH_BUTTON_STYLE_PRESSED)

    def connect_socket(self):
        a.sock.connect()
        self.socket_button.setStyleSheet(interface.CONNECT_SOCKET_BUTTON_STYLE_PRESSED)
        self.go = True

    def run_script(self):
        a.ssh.execute_command()
        self.run_button.setStyleSheet(interface.RUN_BUTTON_STYLE_PRESSED)

def main():
    app = QApplication(sys.argv)
    menu = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
