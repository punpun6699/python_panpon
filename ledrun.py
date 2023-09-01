from machine import Pin,Timer
from time import sleep
led= [Pin(25,Pin.OUT),
      Pin(17,Pin.OUT),
      Pin(18,Pin.OUT),
      Pin(19,Pin.OUT)]
bt=Pin(10,Pin.IN,Pin.PULL_DOWN)
bt2=Pin(11,Pin.IN,Pin.PULL_DOWN)
timer=Timer()
def blink(timer):
   for q in range (4,1,-1):
        led[q].value(1)
        sleep(1)
        led[q].value(0)   
def ledrun():
    for q in range (1,4):
        led[q].value(1)
        sleep(1)
        led[q].value(0)
    
while 0==0:
     bts=bt.value()
     bts1=bt2.value()
    if bts  == True:
        ledrun()
    elif bts1 == True:
        blink()
    else :
        for q in range (1,4):
            led[q].value(0)
           
while 0==0:
    bts=bt.value()
    if bts == True:
        led.value(1)
    else:
        led.value(0)