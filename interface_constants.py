# Application
APP_HRES = 1024
APP_VRES = 700

WINDOW_TITLE = 'Interface'
WINDOW_STYLE = 'background-color: black'

# Buttons
_button_hsize = 160
_button_vsize = 60

CONNECT_SSH_BUTTON = {
'name': 'connect_ssh_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50,
'stylesheet': "background-image: url(\"icons/ssh_off.png\")",
'stylesheet_pressed': "background-image: url(\"icons/ssh_on.png\")",
}

SCRIPT_BUTTON = {
'name': 'script_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50 + _button_vsize + 30,
'stylesheet': "background-image: url(\"icons/script_off.png\")",
'stylesheet_pressed': "background-image: url(\"icons/script_on.png\")",
}

FILE_BUTTON = {
'name': 'file_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50 + _button_vsize * 2 + 30 * 2,
'stylesheet': "background-image: url(\"icons/file_off.png\")",
'stylesheet_pressed': "background-image: url(\"icons/file_on.png\")",
}

WLAN_BUTTON = {
'name': 'wlan_button',
'text': '',
'hsize': _button_hsize,
'vsize': _button_vsize,
'hpos': 50,
'vpos': 50 + _button_vsize * 3 + 30 * 3,
'stylesheet': "background-image: url(\"icons/wifi_off.png\")",
'stylesheet_pressed': "background-image: url(\"icons/wifi_on.png\")",
}

BUTTONS = {
'connect_ssh_button': CONNECT_SSH_BUTTON,
'script_button': SCRIPT_BUTTON,
'file_button': FILE_BUTTON,
'wlan_button': WLAN_BUTTON,
}

# Labels
_label_hsize = 300
_label_vsize = 60

IP_LABEL = {
'name': 'ip_label',
'text': 'IP: Waiting',
'hsize': _label_hsize,
'vsize': _label_vsize,
'hpos': 50 + _button_hsize + 30,
'vpos': 50,
'stylesheet': 'color: white',
}

SSH_TEXT = {
'name': 'ssh_text',
'text': '',
'hsize': APP_HRES,
'vsize': APP_VRES // 3,
'hpos': 0,
'vpos': APP_VRES - 40 - APP_VRES // 3,
'stylesheet': 'border: 1px solid white; color: white'
}

CAR = {
'name': 'car',
'text': '',
'hsize': 75,
'vsize': 142,
'hpos': APP_HRES // 1.6,
'vpos': APP_VRES / 3 - 142 // 2,
'stylesheet': "background-image: url(\"icons/car_off.png\")",
'stylesheet_good': "background-image: url(\"icons/car_good.png\")",
'stylesheet_bad': "background-image: url(\"icons/car_bad.png\")"
}


_obs_label_hsize_h = 30
_obs_label_vsize_h = 50
_obs_label_hsize_v = 50
_obs_label_vsize_v = 30
_obs_label_text = ''

F_OBSTACLE_LABEL = {
'name': 'f_obstacle_label',
'text': _obs_label_text,
'hsize': _obs_label_hsize_v,
'vsize': _obs_label_vsize_v,
'hpos': CAR['hpos'] + (CAR['hsize'] - _obs_label_hsize_v) // 2 + 2,
'vpos': CAR['vpos'] - _obs_label_vsize_v - 20,
'stylesheet': "background-image: url(\"icons/ultrasonic/ultrasonic_none_f.png\")",
}

L_OBSTACLE_LABEL = {
'name': 'l_obstacle_label',
'text': _obs_label_text,
'hsize': _obs_label_hsize_h,
'vsize': _obs_label_vsize_h,
'hpos': CAR['hpos'] - 20 - _obs_label_hsize_h,
'vpos': CAR['vpos'] + (CAR['vsize'] - _obs_label_vsize_h) // 2,
'stylesheet': "background-image: url(\"icons/ultrasonic/ultrasonic_none_l.png\")",
}

R_OBSTACLE_LABEL = {
'name': 'r_obstacle_label',
'text': _obs_label_text,
'hsize': _obs_label_hsize_h,
'vsize': _obs_label_vsize_h,
'hpos': CAR['hpos'] + 20 + CAR['hsize'],
'vpos': CAR['vpos'] + (CAR['vsize'] - _obs_label_vsize_h) // 2,
'stylesheet': "background-image: url(\"icons/ultrasonic/ultrasonic_none_r.png\")",
}

SSH_IN = {
'name': 'ssh_in',
'text': '',
'hsize': APP_HRES,
'vsize': 40,
'hpos': 0,
'vpos': APP_VRES - 40,
'stylesheet': "color: white"
}
