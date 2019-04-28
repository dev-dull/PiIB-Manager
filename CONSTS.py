import yaml

# 'C' is for constants, and that's good enough for me.
class C(object):
    ## Set user-overridable values here.
    FOO = 'bar'

    ## Just declare these exist so IDEs don't complain. Actual values
    ## are set below so that users can't override values in config.yaml
    PIN_3V3_POWER = []
    PIN_5V_POWER = []
    PIN_BCM_0_ID_SD = []
    PIN_BCM_1_ID_SC = []
    PIN_BCM_2_SDA = []
    PIN_BCM_3_SCL = []
    PIN_BCM_4_GPCLK0 = []
    PIN_BCM_5 = []
    PIN_BCM_6 = []
    PIN_BCM_7_CE1 = []
    PIN_BCM_8_CE0 = []
    PIN_BCM_9_MISO = []
    PIN_BCM_10_MOSI = []
    PIN_BCM_11_SCLK = []
    PIN_BCM_12_PWM0 = []
    PIN_BCM_13_PWM1 = []
    PIN_BCM_14_TXD = []
    PIN_BCM_15_RXD = []
    PIN_BCM_16 = []
    PIN_BCM_17 = []
    PIN_BCM_18_PWM0 = []
    PIN_BCM_19_MISO = []
    PIN_BCM_20_MOSI = []
    PIN_BCM_21_SCLK = []
    PIN_BCM_22 = []
    PIN_BCM_23 = []
    PIN_BCM_24 = []
    PIN_BCM_25 = []
    PIN_BCM_26 = []
    PIN_BCM_27 = []
    PIN_GROUND = []
    
    PIN_ALL_PINS = []
    PIN_DATA_PINS = []
    
    ON = 1
    OFF = 0


## Set values specified by the user in the config.
fin =  open('config.yaml', 'r')
confs =  fin.read()
fin.close()
conf = yaml.load(confs, Loader=yaml.SafeLoader)


for k,v in conf.items():
    setattr(C, k, v)    


## Set the actual values of constants that users
## should not be able to override.
C.PIN_3V3_POWER = [1, 17]
C.PIN_5V_POWER = [2, 4]
C.PIN_BCM_0_ID_SD = [27]
C.PIN_BCM_1_ID_SC = [28]
C.PIN_BCM_2_SDA = [3]
C.PIN_BCM_3_SCL = [5]
C.PIN_BCM_4_GPCLK0 = [7]
C.PIN_BCM_5 = [29]
C.PIN_BCM_6 = [31]
C.PIN_BCM_7_CE1 = [26]
C.PIN_BCM_8_CE0 = [24]
C.PIN_BCM_9_MISO = [21]
C.PIN_BCM_10_MOSI = [19]
C.PIN_BCM_11_SCLK = [23]
C.PIN_BCM_12_PWM0 = [32]
C.PIN_BCM_13_PWM1 = [33]
C.PIN_BCM_14_TXD = [8]
C.PIN_BCM_15_RXD = [10]
C.PIN_BCM_16 = [36]
C.PIN_BCM_17 = [11]
C.PIN_BCM_18_PWM0 = [12]
C.PIN_BCM_19_MISO = [35]
C.PIN_BCM_20_MOSI = [38]
C.PIN_BCM_21_SCLK = [40]
C.PIN_BCM_22 = [15]
C.PIN_BCM_23 = [16]
C.PIN_BCM_24 = [18]
C.PIN_BCM_25 = [22]
C.PIN_BCM_26 = [37]
C.PIN_BCM_27 = [13]
C.PIN_GROUND = [9, 25, 39, 6, 14, 20, 30, 34]

C.PIN_ALL_PINS = C.PIN_3V3_POWER + C.PIN_5V_POWER + C.PIN_BCM_0_ID_SD +\
               C.PIN_BCM_1_ID_SC + C.PIN_BCM_2_SDA + C.PIN_BCM_3_SCL +\
               C.PIN_BCM_4_GPCLK0 + C.PIN_BCM_5 + C.PIN_BCM_6 +\
               C.PIN_BCM_7_CE1 + C.PIN_BCM_8_CE0 + C.PIN_BCM_9_MISO +\
               C.PIN_BCM_10_MOSI + C.PIN_BCM_11_SCLK + C.PIN_BCM_12_PWM0 +\
               C.PIN_BCM_13_PWM1 + C.PIN_BCM_14_TXD + C.PIN_BCM_15_RXD +\
               C.PIN_BCM_16 + C.PIN_BCM_17 + C.PIN_BCM_18_PWM0 +\
               C.PIN_BCM_19_MISO + C.PIN_BCM_20_MOSI + C.PIN_BCM_21_SCLK +\
               C.PIN_BCM_22 + C.PIN_BCM_23 + C.PIN_BCM_24 + C.PIN_BCM_25 +\
               C.PIN_BCM_26 + C.PIN_BCM_27 + C.PIN_GROUND
C.PIN_DATA_PINS = filter(lambda p: p not in C.PIN_GROUND + C.PIN_3V3_POWER
                       + C.PIN_5V_POWER, C.PIN_ALL_PINS)

C.ON = 1
C.OFF = 0
