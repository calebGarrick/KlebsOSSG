from machine import Pin, Signal, PWM
from time import sleep
import neopixel

def blink_light(blinkCount = 5):
    ledPow = Pin(5, Pin.OUT);

    for i in range(0, blinkCount):
        ledPow.on()
        sleep(0.3)
        ledPow.off()
        sleep(0.1)

    for u in range(0,3):
        ledPow.on()
        sleep(0.05)
        ledPow.off()
        sleep(0.05);
