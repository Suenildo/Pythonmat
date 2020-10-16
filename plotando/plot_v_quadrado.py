"""
Vamos plotar uma função quadrática
"""

import matplotlib.pyplot as plt


# definição da função:
def f(x):
    return x ** 2 - 3 * x + 2


# Vamos criar valores para x:
x = list(range(-4, 8))

# Vamos obter os valores de y:
y = [f(k) for k in x]

# Vamos construir o gráfico:
plt.xlabel('eixo X')
plt.ylabel('eixo Y')
plt.grid()

# Vamos plotar a função:
plt.plot(x, y, color='blue', marker='*', markeredgecolor='red')
plt.show()
