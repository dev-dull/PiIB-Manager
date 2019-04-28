import yaml
import gpiozero

from CONSTS import C
from RPi import GPIO
from time import sleep

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, 1)
    sleep(0.25)
    GPIO.output(16, 0)

if __name__ == '__main__':
    main()
