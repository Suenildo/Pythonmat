"""
Em python, números complexos (Conjunto C), são representados da
seguinte forma: x + yj
exemplos: 3 + 5j; 0.2 + 2j; 3j; -5 -2j;...

Caso queira se aprofundar em números complexos,
é aconselhável utilizar o módulo: "cmath"
"""

# Formas de criar números complexos:
a = 3 + 2j
y = complex(5, 2)

print(type(a))
print(a)
print(type(y))
print(y)

print()

# Operações simples com complexos:
c = a + y
d = a - y
e = a * y
f = a / y

print(c)
print(d)
print(e)
print(f)

print()

# Obtendo as partes do número complexo:
print(a.real)  # obtendo a parte real do número
print(a.imag)  # obtendo a parte imaginária do número
print(a.conjugate())  # obtendo o conjugado do número complexo
