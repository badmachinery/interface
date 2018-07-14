from PyQt5.QtCore import Qt

import actions.consts as consts

import indy.sockets as socket_lib
import indy.ssh as ssh_lib

socket = socket_lib.Socket()
ssh = ssh_lib.SSH()

sensor_front_data = 300
sensor_left_data = 300
sensor_right_data = 300

raspberry_ip = 'localhost'

ticker = 0

key_map = {
    Qt.Key_W: False,
    Qt.Key_A: False,
    Qt.Key_S: False,
    Qt.Key_D: False
}

script_running = False

socket_send_status = True
interface_work_status = True
