'''
TIPOS DE DATOS
String : cadenas de texto ""  o ''
int
float
boolean

Phyton en general

ESTRUCTURAS DE DATOS
sets : {} instanciamos con new Set
    nos sirven para almacenar datos únicos
    type class: 'set'>
    no interesa el orden de los elemnetos

    tiplas: () instanciamos con tuplas
    permite elementos repetidos
    distintos tipos de dstos
    tiene posición (orden)
    count: cuenta el numero de veces que aparece un elemento

listas : [] instanciamos con new List
tuplas: () instanciamos con tuple 
diccionarios {clave1:valor1, clave2:valor2, claveN:valorN} instanciamos con Dict
'''


conjunto={1,2,3,5,6,9,2}
print(conjunto)
print(type(conjunto))
conjunto2={5,10,'2',3,6,9,}
print(conjunto2)

#Metodos "Qué podemos hacer con los objetos"
conjunto.add(8)
print(conjunto) #{1,2,3,5,6,'2',8,9}
conjunto.pop()
print(conjunto) #{2,3,5,6,8,9,'2'}
print(conjunto.intersection(conjunto2))
print("metodo union",conjunto.union(conjunto2)) #{5,10,"2",3,6,9} metodo union {2,3,5,6,8,9}

#tuplas
tupla1=(4,5,"9",5)
tupla2=(3,9,"uv")

print(type(tupla1))
print(tupla1)
print(tupla1.count("b"))
print(tupla1.index(5)) #1 #posición de un elemento en el objeto


#Listas
lista1={True,"true",5,"b",10,10}
print(type(lista1))


'''
Index: encontrar la posición de un elemento en su primera aparición
Remove:Elimina el elemento indicado
Insert:Permite insertar un elemento en una poscisión especifica
Extend: Agrega dos o mas elementos [,]
Short: Ordena los elementos de una lista
Reverse:devuelve la lista en orden invertido
append:añade un elemento
copy:crea una copia de la lista
clear: elimina todos los elementos de la lista y devuelve []
pop:Elimina y retorna el elemento ubicado en la poscisión indicada


'''

#Dicionario

usuario1={"nombre":"andres","email":"andres@univalle","password":1234,"estudiante":True}
print(type(usuario1))
#print(usuario1.keys())
#print(usuario1.values())
print(usuario1.pop("email"))
print(usuario1)

#Acceder a la información
lista10=[5,3,9,10,9,12,"True"]
print(lista10[0])
print(lista10[-1])
print(lista10[-2])
print(lista10[2:])
print(lista10[:])
print(lista10[2:4])
print(lista10[-4:-1])

tupla20=(2,9,5,6,"uv")
print(tupla20[2])

#Accediendo a un diccionario
curso={"nombre":"TDMI","cantidad":20,"cancelar":"si"}
print(curso["cantidad"]) #20
curso["cancelar"]="No"
print(curso)

