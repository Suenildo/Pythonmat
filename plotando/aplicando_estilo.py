import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['ggplot'])

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

plt.plot(X, y, 'r.')
plt.xlabel("$x$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
_ = plt.axis([0, 2, 0, 15])

plt.show()

'''
plt.plot(X, y, 'r.')
X e y --> eixos
'r.' --> cor

_ = plt.axis([0, 2, 0, 15])
eixos:
0, 2 --> x vai de 0 a 2
0, 15 --> y vai de 0 a 15

'''