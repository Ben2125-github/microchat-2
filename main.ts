input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (mode == "msg") {
        message = "" + message + letter
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showString(message)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showString("" + letter)
    } else if (mode == "set") {
        radio.setGroup(channel)
        mode = "msg"
        basic.showString("" + letter)
    }
    
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    
    if (mode == "msg") {
        if (letter == alpha[0]) {
            num = 25
            letter = alpha[num]
            basic.showString("" + letter)
        } else {
            num = num - 1
            letter = alpha[num]
            basic.showString("" + letter)
        }
        
    } else if (mode == "set") {
        if (channel == 1) {
            channel = 9
            basic.showNumber(channel)
        } else {
            channel = channel - 1
            basic.showNumber(channel)
        }
        
    }
    
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    if (mode == "msg") {
        for (let index = 0; index < 3; index++) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            basic.showLeds(`
                . . # . .
                . . # . .
                . . # . .
                . . . . .
                . . # . .
                `)
        }
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showString(receivedString)
        basic.showString("" + letter)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (mode == "msg") {
        radio.sendString(message)
        message = ""
        letter = alpha[0]
        num = 0
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showIcon(IconNames.Yes)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showString("" + letter)
    }
    
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    if (mode == "msg") {
        if (letter == alpha[25]) {
            num = 0
            letter = alpha[num]
            basic.showString("" + letter)
        } else {
            num = num + 1
            letter = alpha[num]
            basic.showString("" + letter)
        }
        
    } else if (mode == "set") {
        if (channel == 9) {
            channel = 1
            basic.showNumber(channel)
        } else {
            channel = channel + 1
            basic.showNumber(channel)
        }
        
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (mode == "msg") {
        mode = "set"
        basic.showNumber(channel)
    }
    
})
let message = ""
let num = 0
let letter = ""
let alpha : string[] = []
let channel = 0
let mode = ""
radio.setGroup(1)
mode = "msg"
channel = 1
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letter = alpha[0]
num = 0
message = ""
basic.showString("" + letter)
