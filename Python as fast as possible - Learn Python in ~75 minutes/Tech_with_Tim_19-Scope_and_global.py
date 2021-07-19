# PYTHON COURSE 19
# Carlos Terreros Sanchez
# Tech with Tim


# Scope and global
x = 'Tim'

def func(name):
    x = name

print(x)
func('changed')                                                                # x no ha cambiado porque es una variable local, esta en el scope de la funcion y no puede ser accedida ni cambiada desde el exterior
print(x)


def func(name):
    global x                                                                   # Referencia x al scope global. No es recomendable utilizarlo
    x = name

print(x)
func('changed')
print(x)
