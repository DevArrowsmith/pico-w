from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
from pimoroni import RGBLED

# LED

led = RGBLED(6, 7, 8)
led.set_rgb(5, 5, 20)

# Display

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)

# Text

display.set_font("bitmap8")

my_pen_1 = display.create_pen_hsv(0.0, 1.0, 1.0)
display.set_pen(my_pen_1)
display.text("Hello World!", 0, 40, 240, 4)

my_pen_2 = display.create_pen_hsv(0.1, 1.0, 1.0)
display.set_pen(my_pen_2)
display.text("Hello World", 0, 40, 240, 4)

my_pen_3 = display.create_pen_hsv(0.2, 1.0, 1.0)
display.set_pen(my_pen_3)
display.text("Hello Worl", 0, 40, 240, 4)

my_pen_4 = display.create_pen_hsv(0.3, 1.0, 1.0)
display.set_pen(my_pen_4)
display.text("Hello Wor", 0, 40, 240, 4)

my_pen_5 = display.create_pen_hsv(0.4, 1.0, 1.0)
display.set_pen(my_pen_5)
display.text("Hello Wo", 0, 40, 240, 4)

my_pen_6 = display.create_pen_hsv(0.5, 1.0, 1.0)
display.set_pen(my_pen_6)
display.text("Hello W", 0, 40, 240, 4)

my_pen_7 = display.create_pen_hsv(0.6, 1.0, 1.0)
display.set_pen(my_pen_7)
display.text("Hello", 0, 40, 240, 4)

my_pen_8 = display.create_pen_hsv(0.7, 1.0, 1.0)
display.set_pen(my_pen_8)
display.text("Hell", 0, 40, 240, 4)

my_pen_9 = display.create_pen_hsv(0.8, 1.0, 1.0)
display.set_pen(my_pen_9)
display.text("Hel", 0, 40, 240, 4)

my_pen_10 = display.create_pen_hsv(0.9, 1.0, 1.0)
display.set_pen(my_pen_10)
display.text("He", 0, 40, 240, 4)

my_pen_11 = display.create_pen_hsv(1.0, 1.0, 1.0)
display.set_pen(my_pen_11)
display.text("H", 0, 40, 240, 4)

display.update()
