# PYTHON COURSE 17
# Carlos Terreros Sanchez
# Tech with Tim

# Functions
def func():
    print('Run')
    def func():
        print('hi')
    func()

func()

def func2(x, y):
    print('Run', x, y)
    return x * y, x / y

func2(5, 6)
print(func2(5, 6))
r1, r2 = func2(5, 6)
print(r1, r2)

def func3(x, y, z=None):                                                       # Parametro opcional, se puede pasar como argumento o no, si se pasa, sobreescribe el valor de None
    print('Run', x, y, z)
    return x * y, x / y

r3, r4 = func3(5, 6)
print(r3, r4)
r5, r6 = func3(5, 6, 7)
print(r5, r6)

def func(x):
    def func2():
        print(x)
    
    return func2                                                               # Devuelve func2 pero sin llamarla

print(func(3))
print(func(3)())                                                               # Devuelve None prorque no hay nada que imprimir en la func2

x = func(3)
x()
