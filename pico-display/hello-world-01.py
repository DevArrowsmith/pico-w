from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
from pimoroni import RGBLED

# LED

led = RGBLED(6, 7, 8)
led.set_rgb(5, 5, 20)

# Text

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)

r = 255
g = 100
b = 100

my_pen = display.create_pen(r, g, b)

display.set_pen(my_pen)

display.set_font("bitmap8")
display.text("Hello World!", 0, 40, 240, 4)



display.update()
