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

        self.initWASDButtons()

        self.lbl = QLabel('Pressed: ', self)
        self.lbl.setGeometry(g.APP_HRES // 3 - 125, g.APP_VRES // 3 - 20, 250, 40)

        self.plbl = QLabel('Received: ', self)
        self.plbl.setGeometry(g.APP_HRES // 3 - 125, g.APP_VRES // 4 - 20, 250, 40)

        self.connection_status = QLabel('Connection: Waiting', self)
        self.connection_status.setGeometry(g.APP_HRES // 3 - 125, g.APP_VRES // 5 - 20, 250, 40)

        self.show()

    def initWASDButtons(self):
        self.buttons = [QPushButton(i, self) for i in interface.WASD_BUTTONS_TEXT]

        for i, btn in enumerate(self.buttons):
            btn.setGeometry(
                interface.WASD_BUTTONS_HPOS[i], interface.WASD_BUTTONS_VPOS[i],
                g.BTN_HSIZE, g.BTN_VSIZE)
            btn.setStyleSheet(interface.WASD_BUTTONS_STYLE)

        [btn.pressed.connect(self.btn_pressed) for btn in self.buttons]
        [btn.released.connect(self.btn_released) for btn in self.buttons]

        for i, key in enumerate(a.KEY_MAP.keys()):
            a.BTN_MAP[key] = self.buttons[i]
        for i, s in enumerate(interface.WASD_BUTTONS_TEXT):
            a.BTN_MAP[s] = self.buttons[i]

    def initTimer(self):
        self.write_timer = QTimer(self)
        self.write_timer.timeout.connect(self.write_cycle)
        self.write_timer.start(a.TIMER_INTERVAL)

        #self.read_timer = QTimer(self)
        #self.read_timer.timeout.connect(self.read_cycle)
        #self.read_timer.start(a.TIMER_INTERVAL)

    def keyPressEvent(self, e):
        if e.key() in a.KEY_MAP.keys():
            a.KEY_MAP[e.key()] = True
            a.BTN_MAP[e.key()].setStyleSheet(interface.WASD_BUTTONS_STYLE_PRESSED)
        else:
            if e.key() == Qt.Key_Shift:
                a.current_speed += 1
                if (a.current_speed > 3):
                    a.current_speed = 3
            if e.key() == Qt.Key_Control:
                a.current_speed -= 1
                if (a.current_speed < 1):
                    a.current_speed = 1

    def keyReleaseEvent(self, e):
        if e.key() in a.KEY_MAP.keys():
            a.KEY_MAP[e.key()] = False
            a.BTN_MAP[e.key()].setStyleSheet(interface.WASD_BUTTONS_STYLE)

    def btn_pressed(self):
        a.KEY_MAP[a.BTN_TO_KEY[self.sender().text()]] = True
        a.BTN_MAP[self.sender().text()].setStyleSheet(interface.WASD_BUTTONS_STYLE_PRESSED)

    def btn_released(self):
        a.KEY_MAP[a.BTN_TO_KEY[self.sender().text()]] = False
        a.BTN_MAP[self.sender().text()].setStyleSheet(interface.WASD_BUTTONS_STYLE)

    def write_cycle(self):
        if self.mode == c.MODE_MANUAL:
            a.manual_write(self)

    def read_cycle(self):
        if a.arduino.is_connected:
            res = a.arduino.receive_data()
            if res:
                self.plbl.setText('Received: ' + res)
            self.connection_status.setText('Connection: Established')
        else:
            self.connection_status.setText('Connection: Lost')


def main():
    app = QApplication(sys.argv)
    menu = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
