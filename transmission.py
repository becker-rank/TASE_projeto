import config
from machine import PWM, Pin


def trans():
    tx = PWM(Pin(config.txPin), freq=100_000, duty_u16=32768)
    print("PWM configurado no GPIO", config.txPin)

    while(1):
        tx.duty_u16(32768)
