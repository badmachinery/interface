from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QFileDialog, QGridLayout, QPushButton, QMainWindow, QLineEdit, QTextEdit)

# Application
WINDOW = {
'hres': 1024,
'vres': 700,
'title': 'Interface',
'stylesheet': 'background-color: black'
}

# Buttons
_button_hsize = 160
_button_vsize = 60

SSH_BUTTON = {
'type': QPushButton,
'name': 'ssh_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50,
'stylesheet': "background-image: url(\"interface/icons/ssh_off.png\")",
'stylesheet_pressed': "background-image: url(\"interface/icons/ssh_on.png\")",
}

SCRIPT_BUTTON = {
'type': QPushButton,
'name': 'script_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50 + _button_vsize + 30,
'stylesheet': "background-image: url(\"interface/icons/script_off.png\")",
'stylesheet_pressed': "background-image: url(\"interface/icons/script_on.png\")",
}

FILE_BUTTON = {
'type': QPushButton,
'name': 'file_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50 + _button_vsize * 2 + 30 * 2,
'stylesheet': "background-image: url(\"interface/icons/file_off.png\")",
'stylesheet_pressed': "background-image: url(\"interface/icons/file_on.png\")",
}

WLAN_BUTTON = {
'type': QPushButton,
'name': 'wlan_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50 + _button_vsize * 3 + 30 * 3,
'stylesheet': "background-image: url(\"interface/icons/wifi_off.png\")",
'stylesheet_pressed': "background-image: url(\"interface/icons/wifi_on.png\")",
}

# Labels
_label_hsize = 300
_label_vsize = 60

PIXEL = {
'type': QLabel,
'name': 'pixel',
'text': '',
'hsize': _label_hsize / 10,
'vsize': _label_vsize / 5,
'hpos': WINDOW['hres'] - _label_hsize / 10,
'vpos': 0,
'stylesheet': 'background-color: black',
'stylesheet_pressed': 'background-color: green',
}

IP_LABEL = {
'type': QLabel,
'name': 'ip_label',
'text': 'IP: Waiting',
'hsize': _label_hsize,
'vsize': _label_vsize,
'hpos': 50 + _button_hsize + 30,
'vpos': 50,
'stylesheet': 'color: white',
}

SSH_TEXT = {
'type': QTextEdit,
'name': 'ssh_text',
'text': '',
'hsize': WINDOW['hres'],
'vsize': WINDOW['vres'] // 3,
'hpos': 0,
'vpos': WINDOW['vres'] - 40 - WINDOW['vres'] // 3,
'stylesheet': 'border: 1px solid white; color: white'
}

CAR = {
'type': QLabel,
'name': 'car',
'text': '',
'hsize': 75,
'vsize': 142,
'hpos': WINDOW['hres'] // 1.6,
'vpos': WINDOW['vres'] / 3 - 142 // 2,
'stylesheet': "background-image: url(\"interface/icons/car_off.png\")",
'stylesheet_good': "background-image: url(\"interface/icons/car_good.png\")",
'stylesheet_bad': "background-image: url(\"interface/icons/car_bad.png\")"
}


_obs_label_hsize_h = 30
_obs_label_vsize_h = 50
_obs_label_hsize_v = 50
_obs_label_vsize_v = 30
_obs_label_text = ''

SENSOR_FRONT= {
'type': QLabel,
'name': 'sensor_front',
'text': _obs_label_text,
'hsize': _obs_label_hsize_v,
'vsize': _obs_label_vsize_v,
'hpos': CAR['hpos'] + (CAR['hsize'] - _obs_label_hsize_v) // 2 + 2,
'vpos': CAR['vpos'] - _obs_label_vsize_v - 20,
'stylesheet': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_none_f.png\")",
'stylesheet_far': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_far_f.png\")",
'stylesheet_close': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_close_f.png\")",
}

SENSOR_LEFT= {
'type': QLabel,
'name': 'sensor_left',
'text': _obs_label_text,
'hsize': _obs_label_hsize_h,
'vsize': _obs_label_vsize_h,
'hpos': CAR['hpos'] - 20 - _obs_label_hsize_h,
'vpos': CAR['vpos'] + (CAR['vsize'] - _obs_label_vsize_h) // 2,
'stylesheet': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_none_l.png\")",
'stylesheet_far': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_far_l.png\")",
'stylesheet_close': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_close_l.png\")",
}

SENSOR_RIGHT = {
'type': QLabel,
'name': 'sensor_right',
'text': _obs_label_text,
'hsize': _obs_label_hsize_h,
'vsize': _obs_label_vsize_h,
'hpos': CAR['hpos'] + 20 + CAR['hsize'],
'vpos': CAR['vpos'] + (CAR['vsize'] - _obs_label_vsize_h) // 2,
'stylesheet': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_none_r.png\")",
'stylesheet_far': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_far_r.png\")",
'stylesheet_close': "background-image: url(\"interface/icons/ultrasonic/ultrasonic_close_r.png\")",
}

SSH_IN = {
'type': QLineEdit,
'name': 'ssh_in',
'text': '',
'hsize': WINDOW['hres'],
'vsize': 40,
'hpos': 0,
'vpos': WINDOW['vres'] - 40,
'stylesheet': "color: white"
}

COMMUNICATION_TIMER = {
'type': QTimer,
'name': 'communication'
}

SYSTEM_TIMER = {
'type': QTimer,
'name': 'system'
}

CHECK_TIMER = {
'type': QTimer,
'name': 'check'
}
