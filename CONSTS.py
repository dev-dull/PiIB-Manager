import yaml


# 'C' is for constants, and that's good enough for me.
class C(object):
    # Set user-overridable values here.
    FOO = 'bar'

    # Just declare these exist so IDEs don't complain. Actual values
    # are set below so that users can't override values in config.yaml
    KEYWORD_FP_HEADERS_WRITE = ''
    KEYWORD_FP_HEADERS_READ = ''
    KEYWORD_SAMPLING_WAIT_TIME = ''
    
    ON = 1
    OFF = 0


# Set values specified by the user in the config.
fin = open('config.yaml', 'r')
confs = fin.read()
fin.close()
conf = yaml.load(confs, Loader=yaml.SafeLoader)

for k,v in conf.items():
    setattr(C, k, v)    


# Set the actual values of constants that users
# should not be able to override.
C.KEYWORD_FP_HEADERS_WRITE = 'FP_HEADERS_WRITE'
C.KEYWORD_FP_HEADERS_READ = 'FP_HEADERS_READ'
C.KEYWORD_SAMPLING_WAIT_TIME = 'SAMPLING_WAIT_TIME'

C.ON = 1
C.OFF = 0
