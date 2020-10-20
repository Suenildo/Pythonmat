"""
Vamos plotar uma função irracional
"""

import matplotlib.pyplot as plt
import numpy as np


# definição da função:
def f(x):
    if x > 0:
        return 1 / np.sqrt(x)


# Vamos criar valores para x:
x = range(1, 102)


# Vamos obter os valores de y:
y = [f(i) for i in x]


# Vamos construir o gráfico:
plt.xlabel('eixo X')
plt.ylabel('eixo Y')
plt.grid()


# Vamos plotar a função:
plt.plot(x, y, color='blue')

plt.show()