from machine import Pin
import config

def rec():
    rx = Pin(config.rxPin, Pin.IN)

    while(1):
        print("sinal recebido: ", rx.value())
