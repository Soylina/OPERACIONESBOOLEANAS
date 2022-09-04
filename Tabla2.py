from machine import Pin as pin 
from utime import sleep

ledVerde = pin(12,pin.OUT)
botonAma = pin(21,pin.IN)
botonRojo = pin(22,pin.IN)
botonAzu = pin(23,pin.IN)
pausa = 0.1

def prende():
  print("prende")
  ledVerde.value(1)
  sleep(pausa)
  ledVerde.value(0)


menu2 = int(input("SELECCIONE LA OPCION QUE DESEE: \n =/=/=/=/=/=/=/=/=/=/= \n 1. A and C \n 2. B and C \n 3. A or C \n 4. B or C \n 5. NOT A and C"))

while menu2 != 0:

  if menu2 ==1:
   if (botonAma.value() and botonAzu.value()):
    prende() 
  
  elif menu2 ==2:
   if (botonRojo.value() and botonAzu.value()):
    prende()
  
  elif menu2 ==3:
   if (botonAma.value() or botonAzu.value()):
    prende()
    
  elif menu2 ==4:
   if (botonRojo.value() or botonAzu.value()):
    prende() 

  elif menu2 ==5                         :
   if not(botonAma.value() and botonAzu.value()):
    prende() 


