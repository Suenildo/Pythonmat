"""
Utilizando a função anterior, vamos agora calcular
a taxa média de mudança para um determinado intervalo
na linha calculando a inclinação de uma linha secante
que conecta dois pontos na linha.
"""
from matplotlib import pyplot as plt
from calculo_diferencial.calculo_v0 import f

x = list(range(0, 20))
y = [f(i) for i in x]

# Definição dos valores para a taxa média:
x1 = 3
x2 = 6

# Vamos obter os valores de f(x):
y1 = f(x1)
y2 = f(x2)

# Vamos calcular as inclinações:
z = (y2 - y1) / (x2 - x1)

# Vamos criar os valores para a linha secante:
sec_x = [x1, x2]

# Obtendo os valores de y:
sec_y = [f(j) for j in sec_x]

plt.xlabel('x')
plt.ylabel('f(x)')

# Plotando a função:
plt.plot(x, y, color='black')

# Plotando os intervalos:
plt.scatter([x1, x2], [y1, y2], color='green')

# Plotando a linha secante:
plt.plot(sec_x, sec_y, color='red')

# xxxxxxxxxxxxxxx:
plt.annotate('mudança Média = ' + str(z), (x2, (y2 + y1)/2))

plt.show()

