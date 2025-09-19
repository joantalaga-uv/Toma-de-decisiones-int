'''
Funciones:
Son prodecimientos personalizados 
podemos describir una actividad a ejecutar según algunos datos de entrada
tenemos 2 consideraciones
    definición
    uso
'''

# Definición
# Uso de la palabra reservada def
# Nombre
# Parametros
#return

def mi_funcion():
    return True

# Uso
# Llamamos a la función entregandole datos en los argumentos
print(mi_funcion())


import random

def mi_aleatorio():
    return random.randint(1,100)

print(mi_aleatorio())


def mi_aleatorio_2(a,b):
    return random.randint(a,b)

print(mi_aleatorio_2(8,50))




x=90
y=100

def multiples_retornos():
    z=50
    return x,y,z

print(multiples_retornos())
#print(x,y,z) # Las variables definidas dentro de una función solo vive en ella 


# Funciones con oarametros opcionales 
def otra_funcion(a=True):
    print("Por defecto será True","Actualmente es", a)

# Llamo a la función 
otra_funcion(False)