# PYTHON COURSE 06
# Carlos Terreros Sanchez
# Tech with Tim

# String methods
hello = 'hello'
print(type(hello))                                                             # class 'str' quiere decir que la variable es una instancia de la clase string

hello2 = 'hello'.upper()                                                        # Utilizamos el metodo upper() sobre el string. El metodo upper pone en mayusculas el contenido del string
print(hello2)

print(hello.upper())

hello3 = 'heLLO'
print(hello3.lower())

print(hello.capitalize())

print(hello3.lower().count('ll'))
