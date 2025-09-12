'''
Escriba un programa que capture del usuario dos
valores a y b en dos inputs sucesivos. Pida al
usuario desde la función input que los valores a
ingresar deben contener al menos un número
decimal. Al ejecutar, el programa debe realizar la
multiplicación entre los dos valores y entregar la
respuesta en un formatted string que contenga
una variable llamada resultado y el texto de su
preferencia.
'''


print("Buen día, amigo, por favor Ingrese dos valores decimales para multiplicar")
a = int(input("Ingrese un número entero: "))
b = float(input("Ingrese un número decimal: "))
resultado = a * b
print(f'El resultado de la multiplicación entre {a} y {b} es: {resultado}')
