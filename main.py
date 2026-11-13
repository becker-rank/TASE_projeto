from machine import Pin, PWM
import time

trans_pin = 16   #gpio 17 , pin 22
receive_pin = 17 #gpio 16, pin 21

#tx = Pin(trans_pin, Pin.OUT)
rx = Pin(receive_pin, Pin.IN)
tx = PWM(Pin(16), freq=1000, duty_u16=32768)
#tx.on()
T = 1000000 #time in microseconds
while(1):
    print("sinal recebido: ", rx.value())
    
    #ponto
    tx.duty_u16(32768)
    time.sleep_us(T)
    
    # Pausa entre os sinais da letra
    tx.duty_u16(0)
    time.sleep_us(T)

   # Traço
    tx.duty_u16(32768)
    time.sleep_us(3 * T)
    
    tx.duty_u16(0)
    time.sleep_us(T)

    