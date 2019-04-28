import yaml
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
    
    read_power_led()
    power_button()
    GPIO.cleanup()
    
def read_power_led():
    pled_status = GPIO.input(C.POWER_LED_PIN)
    print('POWER LED', pled_status)
    return pled_status == 1
    
def read_hdd_led():
    pass
    
def power_button():
    GPIO.output(C.POWER_BUTTON_PIN, 1)
    while read_power_led() == False:
        sleep(C.OPERATION_WAIT_DURATION)
    GPIO.output(C.POWER_BUTTON_PIN, 0)

if __name__ == '__main__':
    main()
