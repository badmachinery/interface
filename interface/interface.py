import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QFileDialog, QGridLayout, QPushButton, QMainWindow, QLineEdit, QTextEdit)

from interface.consts import *
from actions.vars import key_map

class Interface(QWidget):
    def __init__(self):
        super().__init__()


    def resizeWindow(self, horizontal, vertical):
        self.resize(horizontal, vertical)


    def showWindow(self):
        self.show()


    def hideWindow(self):
        self.hide()


    def resizeElement(self, element_type, element_name, horizontal, vertical):
        '''element must be resizable'''
        self.findChild(element_type, name=element_name).resize(horizontal, vertical)


    def _setWindowTitle(self, title):
        self.setWindowTitle(title)


    def setWindowStylesheet(self, stylesheet):
        self.setStyleSheet(stylesheet)


    def _setStyleSheet(self, element_type, element_name, stylesheet):
        '''element must have stylesheet field'''
        self.findChild(element_type, name=element_name).setStyleSheet(stylesheet)


    def _setEnabled(self, element_type, element_name, status):
        self.findChild(element_type, name=element_name).setEnabled(status)


    def _setReadOnly(self, element_type, element_name, status):
        '''Object must have "readonly" property'''
        self.findChild(element_type, name=element_name).setReadOnly(status)


    def _setText(self, element_type, element_name, text):
        '''element should have text field'''
        self.findChild(element_type, name=element_name).setText(text)


    def getText(self, element_type, element_name):
        '''element should have text field'''
        return self.findChild(element_type, name=element_name).text()

    def _append(self, element_type, element_name, text):
        '''element should have text field'''
        self.findChild(element_type, name=element_name).append(text)


    def __setStandartObjectProperties(self, object, params):
        '''Required: name, hpos, vpos, hsize, vsize'''
        object.setObjectName(params['name'])
        object.setGeometry(params['hpos'], params['vpos'], params['hsize'], params['vsize'])
        object.setStyleSheet(params['stylesheet'])


    def createLabel(self, params):
        '''Required: text, name, hpos, vpos, hsize, vsize, stylesheet'''
        label = QLabel(params['text'], self)
        self.__setStandartObjectProperties(label, params)
        return label


    def createButton(self, params):
        '''Required: text, name, hpos, vpos, hsize, vsize, stylesheet'''
        button = QPushButton(params['text'], self)
        self.__setStandartObjectProperties(button, params)
        return button


    def createLineEdit(self, params):
        '''Required: name, hpos, vpos, hsize, vsize, stylesheet'''
        line_edit = QLineEdit(self)
        self.__setStandartObjectProperties(line_edit, params)
        return line_edit


    def createTextEdit(self, params):
        '''Required: text, name, hpos, vpos, hsize, vsize, stylesheet'''
        text_edit = QTextEdit(params['text'], self)
        self.__setStandartObjectProperties(text_edit, params)
        return text_edit


    def createTimer(self, name):
        '''Name: str'''
        timer = QTimer(self)
        timer.setObjectName(name)
        return timer


    def connectSignal(self, element_type, element_name, signal, function):
        '''Object must have that signal'''
        element = self.findChild(element_type, name=element_name)
        eval('element.{}.connect({})'.format(signal, function))


    def startTimer(self, element_name, time_amount):
        '''time_amount: in milliseconds'''
        self.findChild(QTimer, name=element_name).start(time_amount)


    def keyPressEvent(self, e):
        key_map[e.key()] = True


    def keyReleaseEvent(self, e):
        key_map[e.key()] = False


    def file_dialog(self):
        return QFileDialog.getOpenFileName(self)[0]


app = QApplication(sys.argv)
interface = Interface()
