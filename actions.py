from PyQt5.QtCore import Qt
import socket
import re
import time

import interface
import interface_constants as ic
import constants as c
import socket_connection
import ssh_connection
import wlan
import vars as v

sock = socket_connection.Socket_connection()
ssh = ssh_connection.SSH_connection()

KEY_MAP = { }

mode = c.MODE_MANUAL
script_running = False

direction_status = c.DIRECTION_STATUS_STANDING
forward_speed = 1
backward_speed = -1

rotation_angle = c.SERVO_ANGLE[0]

sending_speed = c.ENGINE_SPEED[0]
sending_options = []

def key_pressed(key):
    KEY_MAP[key] = True
def key_released(key):
    KEY_MAP[key] = False

def system_timer_actions():
    '''
    1) Checking wlan connection status (trying to get ip)
    2) Getting stdout from ssh connection
    '''

    ''' 1) '''
    ip = wlan.getIP(c.RASPBERRY_0_MAC)
    if ip:
        c.RASPBERRY_IP = ip
        interface.main.ip_label.setText('IP: ' + c.RASPBERRY_IP)
    else:
        interface.main.ip_label.setText(ic.IP_LABEL_TEXT)

    ''' 2) '''
    newtext = ssh.get_stdout()
    if newtext:
        interface.main.ssh_text.append(newtext)

def sending_timer_actions():
    '''
    1) Setting standart states
    2) Checking all the keys and making actions associated to them
    3) Flag checking and other actions. Preparing data before sending
    4) Sending data to Raspberry Pi
    '''

    global direction_status, rotation_angle, \
    script_running, mode, sending_options

    ''' 1) '''
    direction_status = c.DIRECTION_STATUS_STANDING
    rotation_angle = c.SERVO_ANGLE[0]
    sending_options.clear()


    ''' 2) '''

    for key in KEY_MAP.keys():
        if KEY_MAP[key] and key in KEY_HANDLER.keys():
            KEY_HANDLER[key]()

    ''' 3) '''

    '''There we choose which speed do we actually want from our car depending on direction_status'''
    sending_speed = {c.DIRECTION_STATUS_STANDING: c.ENGINE_SPEED[0],
                     c.DIRECTION_STATUS_FORWARD: c.ENGINE_SPEED[forward_speed],
                     c.DIRECTION_STATUS_BACKWARD: c.ENGINE_SPEED[backward_speed]
                     }[direction_status]

    ''' 4) '''
    if script_running:
        if mode == c.MODE_MANUAL:
            sock.send('s', str(sending_speed))
            sock.send('r', str(rotation_angle))
        for option in sending_options:
            sock.send(option[0], option[1])

def reading_timer_actions():
    '''
    1) Getting data from raspberry
    2) Updating interface for new data
    '''

    ''' 1) '''
    if script_running:
        #data = sock.receive(64)
        data = None
        if data:
            if data[0] == 'Q':
                data = re.search(r'Q(.+)\n', data).groups(0)
                v.obstacle_distance_front_left = int(data)
            elif data[0] == 'E':
                data = re.search(r'E(.+)\n', data).groups(0)
                v.obstacle_distance_front_right = int(data)
            elif data[0] == 'L':
                data = re.search(r'L(.+)\n', data).groups(0)
                v.obstacle_distance_left = int(data)
            elif data[0] == 'R':
                data = re.search(r'R(.+)\n', data).groups(0)
                v.obstacle_distance_right = int(data)

    ''' 2) '''
    interface.main.q_obstacle_label.setText(str(v.obstacle_distance_front_left))
    interface.main.e_obstacle_label.setText(str(v.obstacle_distance_front_right))
    interface.main.l_obstacle_label.setText(str(v.obstacle_distance_left))
    interface.main.r_obstacle_label.setText(str(v.obstacle_distance_right))


def key_handler_w():
    global direction_status
    direction_status = c.DIRECTION_STATUS_FORWARD
def key_handler_s():
    global direction_status
    direction_status = c.DIRECTION_STATUS_BACKWARD
def key_handler_a():
    global rotation_angle
    rotation_angle = c.SERVO_ANGLE[-45] #Default (and only) option for manual control
def key_handler_d():
    global rotation_angle
    rotation_angle = c.SERVO_ANGLE[45]  #Default (and only) option for manual control

def key_handler_shift():
    global forward_speed
    if forward_speed < 3:
        forward_speed += 1
    else:
        forward_speed = 3

def key_handler_control():
    global forward_speed
    if forward_speed > 1:
        forward_speed -= 1
    else:
        forward_speed = 1

def key_handler_c():
    '''
    1) Stops script execution on raspberry
    2) Stops command sending in interface
    3) Changes interface
    '''
    global script_running
    script_running = False
    sock.send('C', 'Stop')
    sock.close()
    interface.main.make_button_pressed('script_button', False)
    interface.main.make_edit_line_enabled(True)

def key_handler_p():
    '''
    1) Starts auto-script execution on raspberry
    2) Changes mode in interface
    '''
    global mode
    sending_options.append(['C', 'Auto'])
    mode = c.MODE_AUTO

def key_handler_k():
    sending_options.append(['C', 'Load'])

def key_handler_u():
    sending_options.append(['C', 'Way'])

def key_handler_r():
    sending_options.append(['C', 'Break'])

KEY_HANDLER = {
    Qt.Key_W: key_handler_w,
    Qt.Key_S: key_handler_s,
    Qt.Key_A: key_handler_a,
    Qt.Key_D: key_handler_d,
    Qt.Key_Shift: key_handler_shift,
    Qt.Key_Control: key_handler_control,
    Qt.Key_C: key_handler_c,
    Qt.Key_P: key_handler_p,
    Qt.Key_K: key_handler_k,
    Qt.Key_U: key_handler_u,
    Qt.Key_R: key_handler_r
}


'''
Interface buttons' handlers
'''

def connect_wlan():
    wlan.startWLAN(c.WLAN_NAME, c.WLAN_KEY)
    interface.main.make_button_pressed('wlan_button')

def connect_ssh():
    ssh.connect()
    interface.main.make_button_pressed('connect_ssh_button')
    interface.main.make_edit_line_enabled(True)
    ssh.invoke_shell()

def run_script():
    global script_running, mode
    ssh.send_command('python3 ' + c.RASPBERRY_APP_DIRECTORY + '/main.py')
    interface.main.make_button_pressed('script_button')
    sock.connect()
    interface.main.make_edit_line_enabled(False)
    script_running = True
    mode = c.MODE_MANUAL

def send_file_to_raspberry():
    filepath = interface.main.file_dialog()
    filename = re.sub('.*\/', '', filepath)
    if filename:
        ssh.send_file(filepath, c.RASPBERRY_APP_DIRECTORY + '/' + filename)

def send_command():
    '''
    TODO Remake
    '''
    ssh.send_command(interface.main.ssh_in.text())
    interface.main.ssh_in.setText('')
