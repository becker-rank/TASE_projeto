from machine import Pin, PWM
import time
import config
import _thread
import transmission
import reception

# Transmissão no segundo núcleo
_thread.start_new_thread(transmission.trans, ())

# Recepção no núcleo principal
reception.rec()
# 3. Wait for both threads to finish before continuing


#tx = Pin(trans_pin, Pin.OUT)
#tx.on()
while(1):
    x =1

    