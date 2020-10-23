"""
Vamos começar esse estudo com uma função simples.
"""
from matplotlib import pyplot as plt


# Vamos definir nossa função:
def f(x):
    return x ** 2 + x


# Vamos criar valores para x:
x = list(range(0, 20))

# Vamos atribuir os valores de y:
y = [f(i) for i in x]

# Construção do gráfico:
plt.xlabel('x')
plt.ylabel('f(x)')

# Plotagem do gráfico:
plt.plot(x, y, color='black')

# Chamada do gáfico:
plt.show()


