import geometry as g

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


CONNECT_SSH_BUTTON_TEXT = 'Connect to Raspberry through SSH'
CONNECT_SSH_BUTTON_HPOS = g.APP_HRES // 2 - g.BTN_HSIZE // 2
CONNECT_SSH_BUTTON_VPOS = g.APP_VRES // 5
CONNECT_SSH_BUTTON_STYLE = "background-color: white"
CONNECT_SSH_BUTTON_STYLE_PRESSED = "background-color: green"

CONNECT_SOCKET_BUTTON_TEXT = 'Connect to Raspberry through sockets'
CONNECT_SOCKET_BUTTON_HPOS = g.APP_HRES // 2 - g.BTN_HSIZE // 2
CONNECT_SOCKET_BUTTON_VPOS = g.APP_VRES // 3
CONNECT_SOCKET_BUTTON_STYLE = "background-color: white"
CONNECT_SOCKET_BUTTON_STYLE_PRESSED = "background-color: green"

RUN_BUTTON_TEXT = 'Run script on Raspberry'
RUN_BUTTON_HPOS = g.APP_HRES // 2 - g.BTN_HSIZE // 2
RUN_BUTTON_VPOS = g.APP_VRES - g.BTN_VSIZE
RUN_BUTTON_STYLE = "background-color: white"
RUN_BUTTON_STYLE_PRESSED = "background-color: green"
