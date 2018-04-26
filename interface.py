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
