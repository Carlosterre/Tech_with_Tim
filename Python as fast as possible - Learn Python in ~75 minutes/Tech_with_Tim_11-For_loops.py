# PYTHON COURSE 11
# Carlos Terreros Sanchez
# Tech with Tim

# For loops
for i in range(10):                                                            # Funcion range(start, stop, step). Si solo se da un argumento, por defecto se asume que es stop, con start = 0. Dos argumentos se asumen como start, stop
    print(i)
    
for i in range(10, -1, -1):
    print(i)
    
for i in [3, 4, 42, 3, 2, 4]:
    print(i)
    
x = [3, 4, 42, 3, 2, 4]

for i in range(len(x)):                                                        # El loop va hasta pero sin incluir la longitud de x, que es 6, luego va a ir desde 0 hasta 5
    print(x[i])
    
for i, element in enumerate(x):
    print(i, element)
    