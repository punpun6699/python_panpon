from machine import Pin,PWM
import time

led = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)]
bt = Pin(6, Pin.IN, Pin.PULL_UP)
bt2 = Pin(7, Pin.IN, Pin.PULL_UP)
bt3 = Pin(8, Pin.IN, Pin.PULL_UP)

while True:
    bts = bt.value()
    bts2 = bt2.value()
    bts3 = bt3.value()
    #print(bts3)
    
    if bts == 0:
        print("R")
        led[0].value(1)
        led[1].value(0)
        led[2].value(0)
    elif bts2 == 0:
        print("G")
        led[0].value(0)
        led[1].value(1)
        led[2].value(0)
    elif bts3 == 0:
        print("B")
        led[0].value(0)
        led[1].value(0)
        led[2].value(1)
    else:
        led[0].value(0)
        led[1].value(0)
        led[2].value(0)

    time.sleep(0.1)  # Add a small delay to avoid rapid button presses
