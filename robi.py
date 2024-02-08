def on_ir_callbackuser(message):
    basic.show_string("" + str((IR.IR_read())))
    music.play(music.string_playable("C5 - B - A - B C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 - B - A - B C ", 120),
        music.PlaybackMode.UNTIL_DONE)
IR.IR_callbackUser(on_ir_callbackuser)

def on_button_pressed_a():
    basic.show_leds("""
        # # . # #
        # # # # #
        . # # # .
        . # # # .
        . . . . .
        """)
    basic.pause(500)
    basic.show_leds("""
        . . # . .
        . # # # .
        . # # # .
        . # # # .
        # . . . #
        """)
    basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.show_arrow(ArrowNames.NORTH_WEST)
input.on_button_pressed(Button.B, on_button_pressed_b)

strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB_RGB)
R = 100
G = 0
B = 100
music.play(music.string_playable("- A - E - A - E ", 218),
    music.PlaybackMode.UNTIL_DONE)
strip.show_rainbow(1, 360)
basic.show_string("Hola")

def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 20:
        maqueen.motor_stop(maqueen.Motors.M1)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 50:
        maqueen.motor_stop(maqueen.Motors.M2)
        strip.show_color(neopixel.rgb(255, 0, 255))
        for index in range(8):
            basic.show_leds("""
                . . # . .
                . . # . .
                . . # . .
                . . . . .
                . . # . .
                """)
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
            basic.pause(100)
            basic.clear_screen()
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
            basic.pause(100)
    else:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
basic.forever(on_forever)
