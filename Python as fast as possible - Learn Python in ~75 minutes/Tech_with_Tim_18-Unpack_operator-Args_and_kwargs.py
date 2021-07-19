# PYTHON COURSE 18
# Carlos Terreros Sanchez
# Tech with Tim


# Unpack operator, args and kwargs: def func(*args, **kwargs)
def func(*args, **kwargs):
    pass

x = [1, 23, 236363, 2727]

print(x)
print(*x)                                                                      # Desempaqueta los elementos, separandolos


def func2(x, y):
    print(x, y)

pairs = [(1, 2), (3, 4)]

for pair in pairs:                                                             # Funciona, pero no es la manera de hacerlo en python
    func2(pair[0], pair[1])

for pair in pairs:                                                             # La manera correcta
    func2(*pair)
    
func2(**{'x': 2, 'y': 5})                                                      # Para diccionarios. No tienen que estar en orden
func2(**{'y': 5, 'x': 2})


def func3(*args, **kwargs):                                                    # kwarg significa keyword argument
    print(args, kwargs)

func3(1, 2, 3, 4, 5, one=2, two=1)

def func4(*args, **kwargs):
    print(args)

func4(1, 2, 3, 4, 5, one=2, two=1)

def func4(*args, **kwargs):
    print(args)
