import yaml
import logging

from CONSTS import C
from RPi import GPIO
from time import sleep
from functools import partial
from piib_gpio import PinMonitor

def main():
    # Set up board
    GPIO.setmode(GPIO.BOARD)

    # Set up GPIO output pins
    for name,pin in getattr(C, C.KEYWORD_FP_HEADERS_WRITE):
        GPIO.setup(pin, GPIO.OUT)

    # set up GPIO input pins
    monitored_pins = {}
    for name,pin in getattr(C, C.KEYWORD_FP_HEADERS_READ):
        GPIO.setup(pin, GPIO.IN)
        monitored_pins[name] = PinMonitor(partial(GPIO.input, pin), name)
        monitored_pins[name].start()

    power_toggle()
    read_hdd_led_until(max_tries=500)
    GPIO.cleanup()


#######################################################################
# Power operations
#######################################################################
def read_power_led():
    pled_status = GPIO.input(C.POWER_LED_PIN)
    logging.info('POWER LED: %s' % pled_status)
    return pled_status == 1


def read_power_led_until(status, max_tries=25):
    while read_power_led() != status and max_tries:
        sleep(C.OPERATION_WAIT_DURATION)
        max_tries -= 1


def power_toggle():
    power_button(C.OFF if read_power_led() else C.ON)


def power_button(led_status):
    GPIO.output(C.POWER_BUTTON_PIN, 1)
    read_power_led_until(led_status)
    GPIO.output(C.POWER_BUTTON_PIN, 0)


#######################################################################
# Disk operations
#######################################################################
def read_hdd_led():
    # Currently set up to evaluate value from PNP transistor.
    hdd_status = GPIO.input(C.HDD_LED_PIN)
    logging.info('HDD LED: %s' % hdd_status)
    return hdd_status == 1  # Are you inverting this logic? Did you update the previous comment first?


def read_hdd_led_until(max_tries=25):
    while max_tries:
        read_hdd_led()
        sleep(C.OPERATION_WAIT_DURATION)
        max_tries -= 1


#######################################################################
# Glue
#######################################################################
if __name__ == '__main__':
    logging.basicConfig(format='{"timestamp": "%(asctime)s", '
                        '"log_name": "%(name)s", '
                        '"log_level": "%(levelname)s", '
                        '"log_message": "%(message)s"}')
    logger = logging.getLogger('')
    logger.setLevel(getattr(logging, C.LOG_LEVEL.upper(), 'INFO'))

    main()
