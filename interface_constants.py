# Application
APP_HRES = 1024
APP_VRES = 768

WINDOW_STYLE = 'background-color: black'

# Buttons
BTN_HSIZE = 160
BTN_VSIZE = 60

WASD_BUTTONS_TEXT = ['Forward', 'Left', 'Backward', 'Right']
WASD_BUTTONS_HPOS = [
    APP_HRES // 2 - BTN_HSIZE // 2,
    APP_HRES // 3 - BTN_HSIZE // 4,
    APP_HRES // 2 - BTN_HSIZE // 2,
    APP_HRES // 2 + BTN_HSIZE // 1.5
]
WASD_BUTTONS_VPOS = [
    APP_VRES // 4 * 2 + BTN_VSIZE // 2,
    APP_VRES // 4 * 3,
    APP_VRES // 4 * 3,
    APP_VRES // 4 * 3
]
WASD_BUTTONS_STYLE = "background-color: gray"
WASD_BUTTONS_STYLE_PRESSED = "background-color: red"

CONNECT_SSH_BUTTON_TEXT = ''
CONNECT_SSH_BUTTON_HPOS = 50
CONNECT_SSH_BUTTON_VPOS = 50
CONNECT_SSH_BUTTON_STYLE = "background-image: url(\"icons/ssh_connection_off\")"
CONNECT_SSH_BUTTON_STYLE_PRESSED = "background-image: url(\"icons/ssh_connection_on\")"

RUN_BUTTON_TEXT = 'Run script on Raspberry'
RUN_BUTTON_HPOS = 50
RUN_BUTTON_VPOS = 50 + BTN_VSIZE + 30
RUN_BUTTON_STYLE = "background-color: white"
RUN_BUTTON_STYLE_PRESSED = "background-color: #33cfff"

FILE_BUTTON_TEXT = 'Send file to /home/pi/Connector'
FILE_BUTTON_HPOS = 50
FILE_BUTTON_VPOS = 50 + BTN_VSIZE * 2 + 30 * 2
FILE_BUTTON_STYLE = "background-color: white"
FILE_BUTTON_STYLE_PRESSED = "background-color: #33cfff"

WLAN_BUTTON_TEXT = 'Create WLAN'
WLAN_BUTTON_HPOS = 50
WLAN_BUTTON_VPOS = 50 + BTN_VSIZE * 3 + 30 * 3
WLAN_BUTTON_STYLE = "background-color: white"
WLAN_BUTTON_STYLE_PRESSED = "background-color: #33cfff"

#Label
LABEL_HSIZE = 300
LABEL_VSIZE = 60

IP_LABEL_TEXT = 'IP: Waiting'
IP_LABEL_HPOS = 50 + BTN_HSIZE + 30
IP_LABEL_VPOS = 50
IP_LABEL_STYLE = "color: white"

SSH_TEXT_HSIZE = 1024
SSH_TEXT_VSIZE = APP_VRES // 3
SSH_TEXT_HPOS = 0
SSH_TEXT_VPOS = APP_VRES - 40 - SSH_TEXT_VSIZE
SSH_TEXT_STYLE = "border: 1px solid white; color: white"

#Line edit
SSH_IN_HSIZE = APP_HRES
SSH_IN_VSIZE = 40
SSH_IN_HPOS = 0
SSH_IN_VPOS = APP_VRES - SSH_IN_VSIZE
SSH_IN_STYLE = "color: white"
