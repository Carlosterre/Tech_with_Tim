# PYTHON COURSE 16
# Carlos Terreros Sanchez
# Tech with Tim

# Comprehensions
x = [x for x in range(5)]
print(x)

y = [y + 5 for y in range(5)]
print(y)

z = [z % 5 for z in range(5)]
print(z)

a = [0 for a in range(5)]
print(a)

b = [[0 for x in range(100)]for b in range(5)]
print(b)

c = [i for i in range(100) if i % 5 == 0]
print(c)

d = {i:0 for i in range(100) if i % 5 == 0}
print(d)

e = {i for i in range(100) if i % 5 == 0}
print(e)

f = tuple(i for i in range(100) if i % 5 == 0)
print(f)
