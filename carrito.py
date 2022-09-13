from machine import Pin as pin 
from utime import sleep

led = pin(25,pin.OUT)
puerta1 = pin(15,pin.IN)
puerta2 = pin(4,pin.IN)
puerta3= pin(17,pin.IN)
puerta4 = pin(18,pin.IN)
pausa = 0.1
def prende():
  print("prende")
  led.value(1)
  sleep(pausa)
  led.value(0)
def apaga():
  print("apaga")
  led.value(0)
   
while (True):
   if not(puerta1.value() and puerta2.value()and puerta3.value() and puerta4.value()):
    prende() 

    

