import matplotlib.pyplot as plt


def g(x):
    return 3 * x + 2


x = list(range(-10, 10))

y = [g(k) for k in x]

plt.xlabel('Ordenadas')
plt.ylabel('Abscissas')
plt.grid()

plt.plot(x, y, color='black', marker='o', markeredgecolor='green', markerfacecolor='blue', markersize=10)

plt.show()
