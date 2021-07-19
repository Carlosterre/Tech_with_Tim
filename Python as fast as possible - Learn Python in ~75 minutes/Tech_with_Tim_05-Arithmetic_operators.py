# PYTHON COURSE 05
# Carlos Terreros Sanchez
# Tech with Tim

 # Arithmetic operators
x = 9
y = 3
result = x + y
print(result)

result2 = x / y
print(result2)                                                                 # La division siempre devuelve un float

result3 = int(x/y)                                                             # Se puede forzar a que sea un entero
print(result3)

result4 = x ** y
print(result4)

z = 10
result5 = z // y                                                               # Quita los decimales e imprime un entero
print(result5)

result6 = z % y                                                                # Mod, devuelve el resto de una division
print(result6)

# Orden de operaciones standard B E D M A S: Brackets - Exponents - Division - Multiplication - Addition - Substraction - Mods

# num = input('Number: ')
# print(num - 5)                                                                # Devuelve el error: unsupported operand type(s) for -: 'str' and 'int' porque el input se almacena como un string

num2 = input('Number: ')
print(int(num2) - 5)                                                          # int convierte el string en un entero
print(float(num2) - 5)

a = 'hello'
b = 3
print(a * b)

c = 'yes'
print(a + c)
