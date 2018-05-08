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
        self.initUI()
        self.initTimer()
        self.mode = c.MODE_MANUAL

    def initUI(self):
        self.resize(ic.APP_HRES, ic.APP_VRES)
        self.setWindowTitle('Connector')
        self.setStyleSheet(ic.WINDOW_STYLE)

        self.ip_label = QLabel(ic.IP_LABEL_TEXT, self)
        self.ip_label.setGeometry(
            ic.IP_LABEL_HPOS, ic.IP_LABEL_VPOS,
            ic.LABEL_HSIZE, ic.LABEL_VSIZE)
        self.ip_label.setStyleSheet(ic.IP_LABEL_STYLE)

        self.wlan_button = QPushButton(ic.WLAN_BUTTON_TEXT, self)
        self.wlan_button.setGeometry(
            ic.WLAN_BUTTON_HPOS, ic.WLAN_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.wlan_button.setStyleSheet(ic.WLAN_BUTTON_STYLE)
        self.wlan_button.pressed.connect(self.connect_wlan)

        self.connection_button = QPushButton(ic.CONNECT_SSH_BUTTON_TEXT, self)
        self.connection_button.setGeometry(
            ic.CONNECT_SSH_BUTTON_HPOS, ic.CONNECT_SSH_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.connection_button.setStyleSheet(ic.CONNECT_SSH_BUTTON_STYLE)
        self.connection_button.pressed.connect(self.connect_ssh)

        self.run_button = QPushButton(ic.RUN_BUTTON_TEXT, self)
        self.run_button.setGeometry(
            ic.RUN_BUTTON_HPOS, ic.RUN_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.run_button.setStyleSheet(ic.RUN_BUTTON_STYLE)
        self.run_button.pressed.connect(self.run_script)

        self.file_button = QPushButton(ic.FILE_BUTTON_TEXT, self)
        self.file_button.setGeometry(
            ic.FILE_BUTTON_HPOS, ic.FILE_BUTTON_VPOS,
            ic.BTN_HSIZE, ic.BTN_VSIZE)
        self.file_button.setStyleSheet(ic.FILE_BUTTON_STYLE)
        self.file_button.pressed.connect(self.send_file)

        self.ssh_in = QLineEdit(self)
        self.ssh_in.setGeometry(
            ic.SSH_IN_HPOS, ic.SSH_IN_VPOS,
            ic.SSH_IN_HSIZE, ic.SSH_IN_VSIZE)
        self.ssh_in.setStyleSheet(ic.SSH_IN_STYLE)
        self.ssh_in.editingFinished.connect(self.send_command)
        self.ssh_in.setEnabled(False)   #Here

        self.ssh_text = QTextEdit('', self)
        self.ssh_text.setGeometry(
            ic.SSH_TEXT_HPOS, ic.SSH_TEXT_VPOS,
            ic.SSH_TEXT_HSIZE, ic.SSH_TEXT_VSIZE)
        self.ssh_text.setStyleSheet(ic.SSH_TEXT_STYLE)
        self.ssh_text.setReadOnly(True)

        self.go = False

        self.show()

    def initTimer(self):
        self.write_timer = QTimer(self)
        self.write_timer.timeout.connect(self.write_cycle)
        self.write_timer.start(c.TIMER_INTERVAL)

        self.con_timer = QTimer(self)
        self.con_timer.timeout.connect(self.con_cycle)
        self.con_timer.start(c.TIMER_INTERVAL * 5)

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
                a.sock.send('R', 'stop')
                a.sock.close()
                self.run_button.setStyleSheet(ic.RUN_BUTTON_STYLE)
                self.ssh_in.setEnabled(True)    #Here
            if e.key() == Qt.Key_P:
                a.sock.send('R', 'script')
            if e.key() == Qt.Key_K:
                a.sock.send('R', 'reload')

    def keyReleaseEvent(self, e):
        if e.key() in a.KEY_MAP.keys():
            a.KEY_MAP[e.key()] = False

    def write_cycle(self):
        if self.go and self.mode == c.MODE_MANUAL:
            a.manual_write()

    def con_cycle(self):
        ip = wlan.getIP(c.RASPBERRY_0_MAC)
        if ip:
            c.RASPBERRY_IP = ip
            self.ip_label.setText('IP: ' + c.RASPBERRY_IP)
        else:
            self.ip_label.setText(ic.IP_LABEL_TEXT)
        newtext = a.ssh.get_stdout()
        if newtext:
            self.ssh_text.append(newtext)

    def connect_ssh(self):
        a.ssh.connect()
        self.connection_button.setStyleSheet(ic.CONNECT_SSH_BUTTON_STYLE_PRESSED)
        self.ip_label.setText('IP: ' + c.RASPBERRY_IP)
        self.ssh_in.setEnabled(True)   #Here
        a.ssh.invoke_shell()

    def connect_wlan(self):
        wlan.startWLAN(c.WLAN_NAME, c.WLAN_KEY)
        self.wlan_button.setStyleSheet(ic.WLAN_BUTTON_STYLE_PRESSED)

    def run_script(self):
        a.ssh.send_command('python3 ' + c.RASPBERRY_APP_DIRECTORY + '/main.py')
        self.run_button.setStyleSheet(ic.RUN_BUTTON_STYLE_PRESSED)
        a.sock.connect()
        self.ssh_in.setEnabled(False)   #HERE
        self.go = True

    def send_file(self):
        filepath = QFileDialog.getOpenFileName(self)[0]
        filename = re.sub('.*\/', '', filepath)

        if (filename):
            a.ssh.send_file(filepath, c.RASPBERRY_APP_DIRECTORY + '/' + filename)

    def send_command(self):
        a.ssh.send_command(self.ssh_in.text())
        self.ssh_text.append('>>> ' + self.ssh_in.text())
        self.ssh_in.setText('')


app = QApplication(sys.argv)
menu = Main()
