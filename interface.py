import geometry as g

WINDOW_STYLE = 'background-color: black'

# Buttons
WASD_BUTTONS_TEXT = ['Forward', 'Left', 'Backward', 'Right']
WASD_BUTTONS_HPOS = [
    g.APP_HRES // 2 - g.BTN_HSIZE // 2,
    g.APP_HRES // 3 - g.BTN_HSIZE // 4,
    g.APP_HRES // 2 - g.BTN_HSIZE // 2,
    g.APP_HRES // 2 + g.BTN_HSIZE // 1.5
]
WASD_BUTTONS_VPOS = [
    g.APP_VRES // 4 * 2 + g.BTN_VSIZE // 2,
    g.APP_VRES // 4 * 3,
    g.APP_VRES // 4 * 3,
    g.APP_VRES // 4 * 3
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
RUN_BUTTON_VPOS = 50 + g.BTN_VSIZE + 30
RUN_BUTTON_STYLE = "background-color: white"
RUN_BUTTON_STYLE_PRESSED = "background-color: green"

FILE_BUTTON_TEXT = 'Send file to /home/pi/Connector'
FILE_BUTTON_HPOS = 50
FILE_BUTTON_VPOS = 50 + g.BTN_VSIZE * 2 + 30 * 2
FILE_BUTTON_STYLE = "background-color: white"
FILE_BUTTON_STYLE_PRESSED = "background-color: green"
