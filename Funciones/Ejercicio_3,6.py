'''
Ejercicio 3.6
Un semáforo peatonal en una avenida tiene normalmente dos posiciones. 
Detenerse o Avanzar. Desarrolle un programa que genere un número aleatorio 
mediante el método randint de la librería random donde escoja uno de dos 
posibles valores 0 ó 1 y se guarde en una variable denominada peatonal. 
Utilice la expresión if y la expresión else para controlar el semáforo 
a partir del número aleatorio que se genera. En el caso de que la variable 
peatonal tome un valor de 1 se debe presentar un mensaje que indique que el peatón puede cruzar. 
En caso de que la variable tome un 0 se debe presentar un mensaje que indique que el peatón no puede cruzar.

'''

import random  # Importamos la librería random

# Generar número aleatorio 0 o 1 ( 0 no puede cruzar, 1 si puede cruzar)
peatonal = random.randint(0, 1)

# Control del semáforo peatonal dependiendo del valor de ramdon
if peatonal == 1:
    print("El peatón puede cruzar")
else:
    print("El peatón NO puede cruzar")
