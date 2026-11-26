from machine import Pin

import config


def rec():
    rx = Pin(config.rxPin, Pin.IN)

    while True:
        print("sinal recebido: ", rx.value())
