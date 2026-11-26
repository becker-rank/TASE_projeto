import time
from machine import Pin, PWM

import config


def trans():
    tx = PWM(Pin(config.txPin), freq=config.PWM_FREQ_HZ, duty_u16=config.PWM_DUTY_OFF)
    print("PWM configurado no GPIO", config.txPin)

    while True:
        # Ponto
        tx.duty_u16(config.PWM_DUTY_ON)
        time.sleep_us(config.T)

        # Pausa entre os sinais da letra
        tx.duty_u16(config.PWM_DUTY_OFF)
        time.sleep_us(config.T)

        # Traço
        tx.duty_u16(config.PWM_DUTY_ON)
        time.sleep_us(config.DASH_DURATION_US)

        tx.duty_u16(config.PWM_DUTY_OFF)
        time.sleep_us(config.T)
