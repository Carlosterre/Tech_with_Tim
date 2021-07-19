# PYTHON COURSE 15
# Carlos Terreros Sanchez
# Tech with Tim

# Dictionaries. Sets y diccionarios usan hash por lo que son muy rapidos de acceder y modificar
x = {'key': 4}
print(x['key'])

x['key2'] = 5

print(x)

x[2] = [2, 2, 1, 1, 1]
print(x)

print('key' in x)

print(x.values())
print(list(x.values()))
print(list(x.keys()))

del x['key']
print(x)

y = {'key': 4}

for key, value in y.items():
    print(key, value)

for key in y:
    print(key)
    
for key in y:
    print(key, y[key])
    