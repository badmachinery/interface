from interface.interface import interface
from interface.consts import *

import actions.consts as consts
import actions.vars as vars
import actions.actions as actions

import indy.wlan as wlan


def start():
    interface.startTimer(COMMUNICATION_TIMER, consts.timer_interval)
    interface.startTimer(SYSTEM_TIMER, consts.timer_interval)
    interface.startTimer(CHECK_TIMER, consts.timer_interval * 10)


def communication():
    actions.handle_keys()
    actions.get_sensors_data()
    actions.update_sensors_icons()

def system():
    ip = wlan.getIP(consts.RASPBERRY['MAC'])

    if ip:
        vars.raspberry_ip = ip
        interface._setText(IP_LABEL, 'IP: {}'.format(ip))
    else:
        interface._setText(IP_LABEL, IP_LABEL['text'])

    text = vars.ssh.get_stdout()
    if text:
        interface._append(SSH_TEXT, text)

def check():
    if vars.interface_work_status:
        interface._setStyleSheet(PIXEL, PIXEL['stylesheet_pressed'])
        vars.interface_work_status = False
    else:
        interface._setStyleSheet(PIXEL, PIXEL['stylesheet'])
        vars.interface_work_status = True

    if vars.script_running and not vars.socket_send_status:
        actions.handle_script_fall()
