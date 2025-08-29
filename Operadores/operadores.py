'''
Operadores matemáticos
suma
resta
división
multiplicación
potencia
floor división
modulo
'''
#Operador suma
x= 2
y= 5
print(x+y)
w= 2.5
print(type(x), type(y))
z = x + w
print(z, type(z))

#operador resta
a=10
b=15
c=b-a
print("El resultado de la resta es: ",c, type(c))

#operador división
d=12
f=4
print(d/f, type(d/f))
#operador multiplicación
a=50
print(2*a)
#Operador potencia
y=a**f
print(f"el número {a} elevado a la variable f {f} es {y}")
#división piso
m=50
n=3
print(m//n)

#módulo
g=10
h=3
print(g%h) #Es el residuo de la división

#Ejercicio propuesto
l=8
c=-3
print(l/c) #arroja el valor exacto
print(l//c) #arroja el entero mas cercano

'''
Este tipo de operadores los usamos cuando deseamos comparar expresiones o
variables. Python evalúa si se cumple la comparación y nos devuelve (retorna) un
valor True o False
'''

#es igual a ==
print(2==2)
print(2==2.0)

#es diferente a !=
print("univalle"!="Univalle")

x = 4.123456789000001058946546
y = 4.123456789000001
print("la variable x es igual a la variable y?:",x==y)
