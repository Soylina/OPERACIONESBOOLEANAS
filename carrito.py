from machine import Pin as pin 
from utime import sleep

ledrojo = pin(33,pin.OUT)
puerta1 = pin(4,pin.IN)
puerta2 = pin(16,pin.IN)
puerta3= pin(23,pin.IN)
puerta4 = pin(19,pin.IN)
pausa = 0.1
def prende():
  print("prende")
  ledrojo.value(1)
  sleep(pausa)
  ledrojo.value(0)
def apaga():
  print("apaga")
  ledrojo.value(0)
  
while (True):
   if not(puerta1.value() and puerta2.value()):
    prende() 

    

