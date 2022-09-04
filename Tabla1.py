from machine import Pin as pin 
from utime import sleep 

ledVerde = pin(12,pin.OUT)
botonAma = pin(21,pin.IN)
botonRojo = pin(22,pin.IN)
pausa = 0.1

def prende():
  print("prende")
  ledVerde.value(1)
  sleep(pausa)
  ledVerde.value(0)
def apaga():
  print("apaga")
  ledVerde.value(0)

menu = int(input("SELECCIONE LA OPCION QUE DESEE: \n =/=/=/=/=/=/=/=/=/=/=\n 1. A and B \n 2. NOT B \n 3. NOT A \n 4. NOT (A and B)"))

while menu != 0:
  if menu==1:
   if (botonAma.value() and botonRojo.value()):
    prende()
 

  elif menu==2:
   if (botonAma.value() and not botonRojo.value()):
    prende()
    if (botonRojo.value()):
     apaga()
    

  elif menu==3:
   if (not botonAma.value() and botonRojo.value()):
    prende()
    if (botonAma.value()):
     apaga()
    
  elif menu==4:
   if not(botonAma.value() and botonRojo.value()):
    prende() 
    if (botonAma.value()):
     apaga()
