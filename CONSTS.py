import yaml

# 'C' is for constants, and that's good enough for me.
class C(object):
    PIN_3V3_POWER = [1, 17]
    PIN_5V_POWER = [2, 4]
    PIN_BCM_0_ID_SD = [27]
    PIN_BCM_1_ID_SC = [28]
    PIN_BCM_2_SDA = [3]
    PIN_BCM_3_SCL = [5]
    PIN_BCM_4_GPCLK0 = [7]
    PIN_BCM_5 = [29]
    PIN_BCM_6 = [31]
    PIN_BCM_7_CE1 = [26]
    PIN_BCM_8_CE0 = [24]
    PIN_BCM_9_MISO = [21]
    PIN_BCM_10_MOSI = [19]
    PIN_BCM_11_SCLK = [23]
    PIN_BCM_12_PWM0 = [32]
    PIN_BCM_13_PWM1 = [33]
    PIN_BCM_14_TXD = [8]
    PIN_BCM_15_RXD = [10]
    PIN_BCM_16 = [36]
    PIN_BCM_17 = [11]
    PIN_BCM_18_PWM0 = [12]
    PIN_BCM_19_MISO = [35]
    PIN_BCM_20_MOSI = [38]
    PIN_BCM_21_SCLK = [40]
    PIN_BCM_22 = [15]
    PIN_BCM_23 = [16]
    PIN_BCM_24 = [18]
    PIN_BCM_25 = [22]
    PIN_BCM_26 = [37]
    PIN_BCM_27 = [13]
    PIN_GROUND = [9, 25, 39, 6, 14, 20, 30, 34]
    
    PIN_ALL_PINS = PIN_3V3_POWER + PIN_5V_POWER + PIN_BCM_0_ID_SD +\
                   PIN_BCM_1_ID_SC + PIN_BCM_2_SDA + PIN_BCM_3_SCL +\
                   PIN_BCM_4_GPCLK0 + PIN_BCM_5 + PIN_BCM_6 +\
                   PIN_BCM_7_CE1 + PIN_BCM_8_CE0 + PIN_BCM_9_MISO +\
                   PIN_BCM_10_MOSI + PIN_BCM_11_SCLK + PIN_BCM_12_PWM0 +\
                   PIN_BCM_13_PWM1 + PIN_BCM_14_TXD + PIN_BCM_15_RXD +\
                   PIN_BCM_16 + PIN_BCM_17 + PIN_BCM_18_PWM0 +\
                   PIN_BCM_19_MISO + PIN_BCM_20_MOSI + PIN_BCM_21_SCLK +\
                   PIN_BCM_22 + PIN_BCM_23 + PIN_BCM_24 + PIN_BCM_25 +\
                   PIN_BCM_26 + PIN_BCM_27 + PIN_GROUND
    PIN_DATA_PINS = filter(lambda p: p not in PIN_GROUND + PIN_3V3_POWER
                           + PIN_5V_POWER, PIN_ALL_PINS)
