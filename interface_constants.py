# Application
APP_HRES = 1024
APP_VRES = 700

WINDOW_TITLE = 'Interface'
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
CONNECT_SSH_BUTTON_STYLE = "background-image: url(\"icons/ssh_off.png\")"   # Color: 333333
CONNECT_SSH_BUTTON_STYLE_PRESSED = "background-image: url(\"icons/ssh_on.png\")"

SCRIPT_BUTTON_TEXT = ''
SCRIPT_BUTTON_HPOS = 50
SCRIPT_BUTTON_VPOS = 50 + BTN_VSIZE + 30
SCRIPT_BUTTON_STYLE = "background-image: url(\"icons/script_off.png\")"
SCRIPT_BUTTON_STYLE_PRESSED = "background-image: url(\"icons/script_on.png\")"

FILE_BUTTON_TEXT = ''
FILE_BUTTON_HPOS = 50
FILE_BUTTON_VPOS = 50 + BTN_VSIZE * 2 + 30 * 2
FILE_BUTTON_STYLE = "background-image: url(\"icons/file_off.png\")"
FILE_BUTTON_STYLE_PRESSED = "background-image: url(\"icons/file_on.png\")"

WLAN_BUTTON_TEXT = ''
WLAN_BUTTON_HPOS = 50
WLAN_BUTTON_VPOS = 50 + BTN_VSIZE * 3 + 30 * 3
WLAN_BUTTON_STYLE = "background-image: url(\"icons/wifi_off.png\")"
WLAN_BUTTON_STYLE_PRESSED = "background-image: url(\"icons/wifi_on.png\")"

#Label
LABEL_HSIZE = 300
LABEL_VSIZE = 60

IP_LABEL_TEXT = 'IP: Waiting'
IP_LABEL_HPOS = 50 + BTN_HSIZE + 30
IP_LABEL_VPOS = 50
IP_LABEL_STYLE = "color: white"

SSH_TEXT_HSIZE = APP_HRES
SSH_TEXT_VSIZE = APP_VRES // 3
SSH_TEXT_HPOS = 0
SSH_TEXT_VPOS = APP_VRES - 40 - SSH_TEXT_VSIZE
SSH_TEXT_STYLE = "border: 1px solid white; color: white"

CAR_TEXT = ''
CAR_HSIZE = 75
CAR_VSIZE = 142
CAR_HPOS = APP_HRES // 1.6
CAR_VPOS = APP_VRES // 3 - CAR_VSIZE // 2
CAR_STYLE = "background-image: url(\"icons/car_off.png\")"
CAR_STYLE_GOOD = "background-image: url(\"icons/car_good.png\")"
CAR_STYLE_BAD = "background-image: url(\"icons/car_bad.png\")"

OBSTACLE_LABEL_HSIZE_H = 30
OBSTACLE_LABEL_VSIZE_H = 50
OBSTACLE_LABEL_HSIZE_V = 50
OBSTACLE_LABEL_VSIZE_V = 30
OBSTACLE_LABEL_TEXT = ''

F_OBSTACLE_LABEL_HPOS = CAR_HPOS + (CAR_HSIZE - OBSTACLE_LABEL_HSIZE_V) // 2 + 2
F_OBSTACLE_LABEL_VPOS = CAR_VPOS - OBSTACLE_LABEL_VSIZE_V - 20
F_OBSTACLE_LABEL_STYLE = "background-image: url(\"icons/ultrasonic/ultrasonic_none_f.png\")"
L_OBSTACLE_LABEL_HPOS = CAR_HPOS - 20 - OBSTACLE_LABEL_HSIZE_H
L_OBSTACLE_LABEL_VPOS = CAR_VPOS + (CAR_VSIZE - OBSTACLE_LABEL_VSIZE_H) // 2
L_OBSTACLE_LABEL_STYLE = "background-image: url(\"icons/ultrasonic/ultrasonic_none_l.png\")"
R_OBSTACLE_LABEL_HPOS = CAR_HPOS + 20 + CAR_HSIZE
R_OBSTACLE_LABEL_VPOS = CAR_VPOS + (CAR_VSIZE - OBSTACLE_LABEL_VSIZE_H) // 2
R_OBSTACLE_LABEL_STYLE = "background-image: url(\"icons/ultrasonic/ultrasonic_none_r.png\")"

#Line edit
SSH_IN_HSIZE = APP_HRES
SSH_IN_VSIZE = 40
SSH_IN_HPOS = 0
SSH_IN_VPOS = APP_VRES - SSH_IN_VSIZE
SSH_IN_STYLE = "color: white"
