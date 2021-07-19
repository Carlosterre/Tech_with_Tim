# PYTHON COURSE 12
# Carlos Terreros Sanchez
# Tech with Tim

# While loops
x = [3, 4, 42, 3, 2, 4]

i = 0
while i < 10:
    print('run')
    i += 1                                                                     # Para añadir 1 a la variable i. Es lo mismo que i = i + 1. Otras sintaxis son i -= 1, i *= 2, i/= 2, etc
    
i = 0
while True:
    print('run with break')
    i += 1
    if i == 7:
        break
