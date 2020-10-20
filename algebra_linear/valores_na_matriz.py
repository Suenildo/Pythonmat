"""
Dada uma Matriz, vamos aprender a encontrar alguns
valores dentro da mesma.
"""

import numpy as np

m = np.random.randint(1, 507, size=(10, 7))
print(m)

print()

# apezar de já conecer vamos verificar o shape de "m":
print(f'Sou uma matriz do tipo: {m.shape}')

print()

# Vamos buscar o menor valor na matriz:
print(f'O menor valor na matriz é: {np.min(m)}')

print()

# Vamos buscar o maior valor na matriz:
print(f'O maior valor na matriz é: {np.max(m)}')

print()

# Vamos buscar a média dos valores na matriz:

print(f'A média dos valores da matriz é : {np.mean(m)}')
