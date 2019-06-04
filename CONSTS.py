import yaml


# 'C' is for constants, and that's good enough for me.
class C(object):
    # Set user-overridable values here.
    SAMPLING_WAIT_TIME = 0.25
    LOG_LEVEL = 'INFO'

    # Just declare these exist so IDEs don't complain. Actual values
    # are set below so that users can't override values in config.yaml
    KEYWORD_FP_HEADERS_WRITE = ''
    KEYWORD_FP_HEADERS_READ = ''
    KEYWORD_SAMPLING_WAIT_TIME = ''

    KEYWORD_POWER_LED_PIN = ''
    KEYWORD_HDD_LED_PIN = ''
    KEYWORD_PC_SPEAKER_PIN = ''

    KEYWORD_POWER_BUTTON_PIN = ''
    KEYWORD_RESET_BUTTON_PIN = ''
    
    ON = 1
    OFF = 0

    NPN_ON_CHECK = None
    PNP_ON_CHECK = None
    NPN_OFF_CHECK = None
    PNP_OFF_CHECK = None

# Set values specified by the user in the config.
fin = open('config.yaml', 'r')
confs = fin.read()
fin.close()
conf = yaml.load(confs, Loader=yaml.SafeLoader)

for k,v in conf.items():
    setattr(C, k, v)    


# Set the actual values of constants that users
# should not be able to override.
C.KEYWORD_SAMPLING_WAIT_TIME = 'SAMPLING_WAIT_TIME'

C.KEYWORD_FP_HEADERS_WRITE = 'FP_HEADERS_WRITE'
C.KEYWORD_FP_HEADERS_READ = 'FP_HEADERS_READ'

C.KEYWORD_POWER_LED_PIN = 'POWER_LED_PIN'
C.KEYWORD_HDD_LED_PIN = 'HDD_LED_PIN'
C.KEYWORD_PC_SPEAKER_PIN = 'PC_SPEAKER_PIN_PIN'

C.KEYWORD_POWER_BUTTON_PIN = 'POWER_BUTTON_PIN'
C.KEYWORD_RESET_BUTTON_PIN = 'RESET_BUTTON_PIN'

C.ON = 1
C.OFF = 0

C.NPN_ON_CHECK = lambda x: x == C.ON
C.PNP_ON_CHECK = lambda x: x == C.OFF
C.NPN_OFF_CHECK = C.PNP_ON_CHECK  # Confusing as heck to read, but ensures we are
C.PNP_OFF_CHECK = C.NPN_ON_CHECK  # re-pointing at existing functions, using less memory
