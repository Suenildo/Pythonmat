"""
Para trabalhar com frações, é conveniente que importemos o módulo:
fractions

"""

from fractions import Fraction

# caso você não importe essa função:
a = 1/2
print(a)
# Notou que ele não gerou uma fração, e sim uma operação?

print()

# Criando frações:
b = Fraction(1,  2)

''' Fraction(1,  2):
1 - numerador
2 - denominador
'''
print(type(b))
print(b)  # aqui não foi realizada a operação, mas criada a fração

#  A partir de agora podemos realizar operações com a fração criada.
c = b * 3
print(f'O produto de 1/2 por 3 é = {c}')

# E se eu multiplicar b por 2.3?
d = b * 2.3
print(d)

''' Isso acontece porque quando eu multiplico uma
fração por um número inteiro, o resultado é uma fração,
entretanto, se eu multiplicar a fração por um float, o resultado
será um float'''

# Operações:
e = Fraction(3, 5)
f = Fraction(6, 7)
g = Fraction(3/2)

total = (e + (f * g)) / e
print(total)

