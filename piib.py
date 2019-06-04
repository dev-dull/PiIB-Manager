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
    global write_pins
    write_pins = {}
    for name,pin in getattr(C, C.KEYWORD_FP_HEADERS_WRITE):
        GPIO.setup(pin, GPIO.OUT)
        write_pins[name] = pin

    # set up GPIO input pins
    global monitored_pins
    monitored_pins = {}
    for name,pin in getattr(C, C.KEYWORD_FP_HEADERS_READ):
        # If the pin is set to <=0, skip it.
        if pin > 0:
            GPIO.setup(pin, GPIO.IN)
            monitored_pins[name] = PinMonitor(partial(GPIO.input, pin), name)
            # Start a thread that monitors the pin
            monitored_pins[name].start()

    power_toggle()
    read_hdd_led_until(max_tries=500)
    for name,monitored_pin in monitored_pins.items():
        # Tell the thread that monitors the pin to stop checking.
        monitored_pin.continue_monitoring = False
    GPIO.cleanup()


def read_pin_until(pin, until_func=C.NPN_ON_CHECK, max_tries=25):
    while read_pin(pin, until_func) and max_tries:
        max_tries -= 1
        sleep(C.SAMPLING_WAIT_TIME)
    else:
        # while loop + elif is not a thing, apparently.
        if max_tries == 0:
            logging.info('max tries for reading %s state change exhausted.' % pin.name)


def read_pin(pin, func=C.NPN_ON_CHECK):
    return func(pin.status)


#######################################################################
# Power operations
#######################################################################
def read_power_led():
    return read_pin(monitored_pins[C.KEYWORD_POWER_LED_PIN], func=C.NPN_ON_CHECK)


# def read_power_led_until(status, max_tries=25):
#     while read_power_led() != status and max_tries:
#         sleep(C.OPERATION_WAIT_DURATION)
#         max_tries -= 1


def power_toggle():
    power_button(C.NPN_OFF_CHECK if read_power_led() else C.NPN_ON_CHECK)


def power_button(until_func):
    GPIO.output(write_pins[C.KEYWORD_POWER_BUTTON_PIN], C.ON)
    read_pin_until(monitored_pins[C.KEYWORD_POWER_LED_PIN], until_func=until_func)
    GPIO.output(write_pins[C.KEYWORD_POWER_BUTTON_PIN], C.OFF)


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
        sleep(C.SAMPLING_WAIT_TIME)
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
