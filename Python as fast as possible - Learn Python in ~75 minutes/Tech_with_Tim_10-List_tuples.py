# PYTHON COURSE 10
# Carlos Terreros Sanchez
# Tech with Tim

# List / tuples - Collections

# List
x = [4, True, 'hi']
print(len(x))                                                                  # Longitud de la lista

y = []                                                                         # Lista vacia

z = 'hi'
print(len(z))

x.append('hello')                                                              # Formas de agregar elementos a una lista
x.extend([4, 5, 5, 5, 5, 5, 5, 5, 5])
print(x) 

x.pop()                                                                        # Elimina el ultimo elemento
print(x)

print(x.pop())                                                                 # Muestra el elemento quitado
print(x)

# Las listas se indexan comenzando por 0, siendo 0 la primera posicion de la lista
print(x.pop(0))                                                                # Elimina el primer item de la lista
print(x)

print(x[1])

x[0] = 'hello'                                                                 # Las listas son mutables, pueden ser cambiadas
print(x)

a = [4, True, 'hi']
b = a
a[0] = 'hello'                                                                 # El cambio en la lista a ha modificado la lista b porque a guarda una referencia de la lista, no una copia
print(a, b)

c = a[:]                                                                       # De esta manera se crea una copia de la lista, de modo que no se modifica
a[0] = 'bye'
print(a, c)

# Tuplas. Son inmutables. No se pueden añadir ni quitar elementos
m = (0, 0, 2)
print(m[0])

# Listas y tuplas en listas
n = [[0, 'hi', False], (0, 1, 1), [[2, 2], 1]]
print(n[2])
