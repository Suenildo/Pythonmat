"""
Para plotarmos os gráficos deste pacote, usaremos o Matplotlib.

Matplotlib é uma biblioteca de software para criação de gráficos
e visualizações de dados em geral, feita para e da linguagem de
programação Python e sua extensão de matemática NumPy.

fonte: https://pt.wikipedia.org/wiki/Matplotlib
"""

import matplotlib.pyplot as plt


# Vamos definir uma função para o gráfico:
def f(x):
    return x + 1


# Vamos criar uma ista de valores para "x":
x = list(range(-5, 5))

# vamos definir "y" com uma list comprehension:
y = [f(k) for k in x]

# Vamos configurar o gráfico:
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Vamos plotar a função:
plt.plot(x,y, color='red', marker='*', markeredgecolor='blue', markerfacecolor='black')

# Vamos exibir o gráfico:
plt.show()


