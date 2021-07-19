# PYTHON COURSE 13
# Carlos Terreros Sanchez
# Tech with Tim

# Slice operator
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'

sliced = x[0:4:2]                                                              # [start:stop:step] No incluye el valor final
print(sliced)

sliced2 = x[:4]                                                                # Si no hay argumento start comienza por el principio de manera predeterminada
print(sliced2)

sliced3 = x[2:4:]
print(sliced3)

sliced4 = x[4:2:-1]
print(sliced4)

sliced5 = x[::-1]                                                              # Invierte una lista
print(sliced5)

sliced6 = s[::2]
print(sliced6)

sliced7 = (2, 2, 3, 4, 5)[::2]
print(sliced7)
