from machine import Pin,Timer
from time import sleep
led= [Pin(25,Pin.OUT),
      Pin(17,Pin.OUT),
      Pin(18,Pin.OUT),
      Pin(19,Pin.OUT)]
timer=Timer()
def blink(timer):
    for i in range (0,4):
        led[i].toggle()   
def ledrun():
    for q in range (1,4):
        led[q].value(1)
        sleep(1)
        led[q].value(0)
    
while 0==0:
    ledrun()