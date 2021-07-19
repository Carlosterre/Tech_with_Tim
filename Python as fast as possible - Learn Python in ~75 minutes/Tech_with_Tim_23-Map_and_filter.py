# PYTHON COURSE 23
# Carlos Terreros Sanchez
# Tech with Tim


# Map and filter
x = [1, 2, 4, 5, 3, 3, 21, 2, 21, 2, 313, 1, 23, 142, 4]

mp = map(lambda i: i + 2, x)                                                   # Mapea todos los elementos de la lista con la funcion lambda, aplicandosela a todos los elementos

print(list(mp))                                                                # Transformando a una nueva lista


mp = map(lambda i: i * 2, x)

print(list(mp))


fil = filter(lambda i: i % 2 == 0, x)                                          # i % 2 == 0 devolvera los valores que sean pares

print(list(fil))


def func(i):                                                                   # Sin utilizar la funcion lambda
    i = i * 3
    
    return i % 2 == 0

fil = filter(func, x)

print(list(fil))
