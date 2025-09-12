#Ejercicio 2,20

calificaciones={"liliana":4.5,"carme":3.3,"josefina":4.1,"daniela":4.9,"pedro":2.9,"jose":4.6,"mario":3.3}
print(type(calificaciones))

#Ejercicio 2,21

#c_ordenado = (sorted(calificaciones))
#print(c_ordenado) #Nos permite ordenar las claves por odern alfabetico, en este caso los nombres de los estudiantes.


#Ejercicio 2,22

''' 
calificaciones.popitem({'Daniela':4.9})

¿Qué interpretación se le puede dar
al mensaje de error que nos entrega
el intérprete cuando ejecutamos?

R// El error de mensaje se puede interpretar como que no es necesario añadir un argumento, en este caso 'Daniela':4.9},
debido a que este ya se ejecuta por defecto para eliminar y devolver el ultimo par clave/valor insertado en el diccionario

¿Cuándo es conveniente aplicar este
método?

R// Este método es conveniente utilizarlo cuando los datos finales no son relevantes o carecen de información por algun motivo

'''
#print(calificaciones.popitem())
#print(calificaciones)

#Ejercicio 2,23
print(calificaciones.items())

'''
¿qué retorna este
método?

R// Este método retorna la información que se encuentra en el diccionario creado, en este caso el de los estudiantes y notas.

¿qué tipo de estructura de datos parece, una lista?una lista delistas?, ¿una lista de tuplas?. 

R// la estructura en este caso parece ser una lista de tuplas.

'''

#Ejercicio 2,24

print(calificaciones.update({"liliana:4.7}))
print(calificaciones)
