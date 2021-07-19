# PYTHON COURSE 08
# Carlos Terreros Sanchez
# Tech with Tim

# Chained conditionals
x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2                                                            # Lo mismo que result3 = z < (x + 2)

result4 = result1 or result2                                                   # True si una u otra son true
print(result4)

result5 = result1 or result2 or result3
print(result5)

print(not True)                                                                # Invierte el boolean de la derecha
print(not (False or True))

print(False and True)

print(not(False and True or True))                                             # Orden de prioridad: not - and - or
