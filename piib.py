import yaml
import logging
import gpiozero

from CONSTS import C
from RPi import GPIO
from time import sleep

def main():
    # Set up board
    GPIO.setmode(GPIO.BOARD)

    # Set up GPIO output pins
    GPIO.setup(C.POWER_BUTTON_PIN, GPIO.OUT)

    # set up GPIO input pins
    GPIO.setup(C.POWER_LED_PIN, GPIO.IN)

    power_toggle()
    GPIO.cleanup()

def read_power_led():
    pled_status = GPIO.input(C.POWER_LED_PIN)
    print('POWER LED: %s' % pled_status)
    return pled_status == 1

def read_power_led_until(status, max_tries=25):
    while read_power_led() != status and max_tries:
        sleep(C.OPERATION_WAIT_DURATION)
        max_tries -= 1

def read_hdd_led():
    pass

def power_toggle():
    power_button(C.OFF if read_power_led() else C.ON)

def power_button(led_status):
    GPIO.output(C.POWER_BUTTON_PIN, 1)
    read_power_led_until(led_status)
    GPIO.output(C.POWER_BUTTON_PIN, 0)

if __name__ == '__main__':
    main()
