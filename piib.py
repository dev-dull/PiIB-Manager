import io
import yaml
import logging
import picamera

from CONSTS import C
from RPi import GPIO
from time import sleep
from functools import partial
from piib_gpio import PinMonitor
from flask import Flask, Response


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
    return Response(frame_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')


def frame_generator():
    fin = open('images/no-signal.jpg', 'rb')
    no_signal = fin.read()
    fin.close()

    screen_handle = None
    frame_buffer = io.BytesIO()
    while True:
        frame = no_signal
        if screen_handle:
            try:
                frame_buffer.seek(0)
                screen_handle.capture(frame_buffer, 'jpeg')
                frame_buffer.truncate()
                frame_buffer.seek(0)
                frame = frame_buffer.read()
            except picamera.exc.PiCameraRuntimeError as e:
                # We had gotten a picture from the camera at some point, but have since lost signal.
                # Reset the handle to force a new init of the variable on the next pass of the loop.
                screen_handle = None
                # frame = no_signal
        else:
            try:
                screen_handle = picamera.PiCamera()
                # screen_handle.resolution = (1024, 768)
            except picamera.exc.PiCameraMMALError as e:
                # We have never gotten a signal and failed to get one just now.
                screen_handle = None  # Not sure if we need screen_handle nulled out. Probably not.

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


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


if __name__ == '__main__':
    logging.basicConfig(format='{"timestamp": "%(asctime)s", '
                        '"log_name": "%(name)s", '
                        '"log_level": "%(levelname)s", '
                        '"log_message": "%(message)s"}')
    logger = logging.getLogger('')
    logger.setLevel(getattr(logging, C.LOG_LEVEL.upper(), 'INFO'))

    _gpio_setup()

    app.run(host='0.0.0.0', port='5112', threaded=False)
    GPIO.cleanup()
