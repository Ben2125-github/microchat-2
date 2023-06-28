def on_button_pressed_a():
    global message, mode
    if mode == "msg":
        message = "" + message + letter
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_string(message)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_string("" + (letter))
    elif mode == "set":
        radio.set_group(channel)
        mode = "msg"
        basic.show_string("" + (letter))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global num, letter, channel
    if mode == "msg":
        if letter == alpha[0]:
            num = 25
            letter = alpha[num]
            basic.show_string("" + (letter))
        else:
            num = num - 1
            letter = alpha[num]
            basic.show_string("" + (letter))
    elif mode == "set":
        if channel == 1:
            channel = 9
            basic.show_number(channel)
        else:
            channel = channel - 1
            basic.show_number(channel)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_received_string(receivedString):
    if mode == "msg":
        for index in range(3):
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
            basic.show_leds("""
                . . # . .
                . . # . .
                . . # . .
                . . . . .
                . . # . .
                """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_string(receivedString)
        basic.show_string("" + (letter))
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global message, letter, num
    if mode == "msg":
        radio.send_string(message)
        message = ""
        letter = alpha[0]
        num = 0
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_icon(IconNames.YES)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_string("" + (letter))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    global num, letter, channel
    if mode == "msg":
        if letter == alpha[25]:
            num = 0
            letter = alpha[num]
            basic.show_string("" + (letter))
        else:
            num = num + 1
            letter = alpha[num]
            basic.show_string("" + (letter))
    elif mode == "set":
        if channel == 9:
            channel = 1
            basic.show_number(channel)
        else:
            channel = channel + 1
            basic.show_number(channel)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_logo_pressed():
    global mode
    if mode == "msg":
        mode = "set"
        basic.show_number(channel)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

message = ""
num = 0
letter = ""
alpha: List[str] = []
channel = 0
mode = ""
radio.set_group(1)
mode = "msg"
channel = 1
alpha = ["A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"]
letter = alpha[0]
num = 0
message = ""
basic.show_string("" + (letter))