from machine import Pin as pin 
from utime import sleep

ledVerde = pin(12,pin.OUT)
botonAma = pin(21,pin.IN)
botonRojo = pin(22,pin.IN)
botonAzu = pin(23,pin.IN)
botonNegro = pin(19,pin.IN)
pausa = 0.1

def prende():
  print("prende")
  ledVerde.value(1)
  sleep(pausa)
  ledVerde.value(0)
def apaga():
  print("apaga")
  ledVerde.value(0)

menu3 = int(input("SELECCIONE LA OPCION QUE DESEE: \n =/=/=/=/=/=/=/=/=/=/= \n 1. (A or B) OR (C or D) \n 2. (A and B)and(C and D) \n 3. NOT(A or B) OR (C or D) \n 4. NOT ((A or B) and NOT (C and NOT D)) \n -------------------------------------->"))

while menu3 != 0:

  if menu3 ==1:
   if ((botonAma.value() or botonRojo.value()) or (botonAzu.value() or botonNegro.value())):
    prende()
    if (botonAma.value() or botonRojo.value()):
     prende()
     if (botonAzu.value() or botonNegro.value()):
      prende()

  elif menu3 ==2:
   if ((botonAma.value() and botonRojo.value()) and (botonAzu.value() and botonNegro.value())):
    prende()

  elif menu3 ==3:
   if not(botonAma.value() or botonRojo.value()) or (botonAzu.value()or botonNegro.value()):
    prende()
 
  elif menu3 ==4:
   if not(botonAma.value() or botonRojo.value() and not (botonAzu.value() and not botonNegro.value())):
    prende() 
