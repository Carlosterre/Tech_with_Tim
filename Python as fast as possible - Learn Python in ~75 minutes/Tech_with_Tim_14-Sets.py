# PYTHON COURSE 14
# Carlos Terreros Sanchez
# Tech with Tim

# Sets. No tienen nocion de posicion, solo si un item esta o no esta. Utilizan hash por lo que son muy faciles de acceder y modificar en cualquier momento
x = set()
s = {4, 32, 2, 2}

print(type({}))                                                                # Si no se declara un set vacío primero, se corre el riesgo de declarar un diccionario
print(type(s))

s.add(5)
print(s)

s.remove(5)
print(s)

print(4 in s)                                                                  # Para comprobar si algo está en el diccionario. Esta operacion es mucho, mucho más rápida que declarar s como una lista y hacer print(4 in s)

s2 = {3, 4, 22, 1}
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))
