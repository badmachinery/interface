from interface.interface import interface
from interface.consts import *

import actions.consts as consts
import actions.vars as vars
import actions.actions as actions

import indy.wlan as wlan


def start():
    interface.startTimer('communication', consts.timer_interval)
    interface.startTimer('system', consts.timer_interval * 5)
    interface.startTimer('check', consts.timer_interval * 10)


def communication():
    actions.handle_keys()
    actions.get_sensors_data()

def system():
    ip = wlan.getIP(consts.RASPBERRY['MAC'])

    if ip:
        vars.raspberry_ip = ip
        interface._setText(IP_LABEL['type'], IP_LABEL['name'], 'IP: {}'.format(ip))
    else:
        interface._setText(IP_LABEL['type'], IP_LABEL['name'], IP_LABEL['text'])

    text = vars.ssh.get_stdout()
    if text:
        interface._append(SSH_TEXT['type'], SSH_TEXT['name'], text)

def check():
    if vars.interface_work_status:
        interface._setStyleSheet(PIXEL['type'], PIXEL['name'], PIXEL['stylesheet_pressed'])
        vars.interface_work_status = False
    else:
        interface._setStyleSheet(PIXEL['type'], PIXEL['name'], PIXEL['stylesheet'])
        vars.interface_work_status = True

    if vars.script_running and not vars.socket_send_status:
        actions.handle_script_fall()
