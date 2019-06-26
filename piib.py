import yaml
import logging
import picamera

from CONSTS import C
from RPi import GPIO
from time import sleep
from flask import Flask
from functools import partial
from piib_gpio import PinMonitor


app = Flask('piib_ui')


#######################################################################
# UI
#######################################################################
@app.route('/')
def ui():
    return '''
    <h1>hello, world!"</h1>
    hdd: %s<br />
    power: %s
    ''' % (monitored_pins['HDD_LED_PIN'].status, monitored_pins['POWER_LED_PIN'].status)


#######################################################################
# Get data
#######################################################################
@app.route('/host_status')
def host_status():
    # TODO: monitored_pins[name] should probably return the status automatically without needing to specify the '.status'
    #       then we can just `return dict(monitored_pins)` to simplify the code here.
    status = {}
    for name,pin in monitored_pins.items():
        status[name] = pin.status
    return status, 200, {'Content-type': 'application/json'}

#~ @app.route('/power_led')
#~ def power_led():
    #~ return monitored_pins[C.KEYWORD_POWER_LED_PIN].status
 
 
#~ @app.route('/hdd_led')
#~ def hdd_led():
    #~ return monitored_pins[C.KEYWORD_HDD_LED_PIN].status


#~ @app.route('/pc_speaker')
#~ def pc_speaker():
    #~ return monitored_pins[C.KEYWORD_PC_SPEAKER_PIN].status


#######################################################################
# Set data
#######################################################################
# TODO: it might make more sense to make the input a single function where the user must specify the action (force poweroff, press power button, press reset button, etc)
@app.route('/power_button/<action>')
def power_button_action(action):
    #TODO:
    return "not yet", 501
    

@app.route('/reset_button/<action>')
def reset_button_action(action):
    #TODO:
    return "not yet", 501


#######################################################################
# I/O
#######################################################################
# TODO: these functions probably make zero sense as they exist. They're just here as a sort of roadmap.
@app.route('/mouse_move/<action>')
def mouse_move(action):
    #TODO: move left, move right, up, down
    return "not yet", 501
    

@app.route('/key/<action>')
def keyboard(action):
    #TODO: key down, up, 
    return "not yet", 501


@app.route('/screen')
def screen():
    # the "start_preview()" function that all tutorials say to run actually start a visual preview which isn't the desired result here.
    if display:
        try:
            cam = picamera.PiCamera()
        except picamera.exc.PiCameraMMALError as e:
            # We've never set up 'cam' and this error tells us there's no signal yet
            # TODO: return "no signal"
            pass
        except picamera.exc.PiCameraRuntimeError as e:
            # We had a signal, but this error means we lost it
            #TODO: return "no signal"
            pass
    # TODO: regurn a jpeg image (as an rtsp stream?)
    return "not yet", 501
    

#######################################################################
# Setup
#######################################################################
def _gpio_setup():
    # Set up board
    GPIO.setmode(GPIO.BOARD)

    # Set up GPIO output pins
    global write_pins
    write_pins = {}
    for name,pin in getattr(C, C.KEYWORD_FP_HEADERS_WRITE).items():
        GPIO.setup(pin, GPIO.OUT)
        write_pins[name] = pin

    # set up GPIO input pins
    global monitored_pins
    monitored_pins = {}
    for name,pin in getattr(C, C.KEYWORD_FP_HEADERS_READ).items():
        # If the pin is set to <=0, skip it.
        if pin > 0:
            GPIO.setup(pin, GPIO.IN)
            monitored_pins[name] = PinMonitor(partial(GPIO.input, pin), name)
            # Start a thread that monitors the pin
            monitored_pins[name].start()

    #power_toggle()
    #read_hdd_led_until(max_tries=500)
    #~ for name,monitored_pin in monitored_pins.items():
        #~ # Tell the thread that monitors the pin to stop checking.
        #~ sleep(2)
        #~ monitored_pin.continue_monitoring = False


if __name__ == '__main__':
    logging.basicConfig(format='{"timestamp": "%(asctime)s", '
                        '"log_name": "%(name)s", '
                        '"log_level": "%(levelname)s", '
                        '"log_message": "%(message)s"}')
    logger = logging.getLogger('')
    logger.setLevel(getattr(logging, C.LOG_LEVEL.upper(), 'INFO'))

    _gpio_setup()
    global display
    display = None
    
    app.run(host='0.0.0.0', port='5112')
    GPIO.cleanup()
    picamera.stop_preview()
