import numpy as np

matriz = np.array([[14, 11, 4, 10],
                   [9, 5, 8, 13],
                   [12, 4, 6, 4],
                   [4, 13, 10, 6],
                   [9, 6, 13, 10],
                   [10, 13, 12, 12]])

slice_1 = matriz[:][:3]
print(slice_1)

print()

print("Vamos pegar a coluna 0")
slice_2 = matriz[0:, 0:1]
print(slice_2)

print()
print("Vamos pegar as linhas 0, 3 e 5")
slice_3 = matriz[[0, 3, 5]]
print(slice_3)

print()

print('Vamos retornar a coluna 0 como um vetor (lista)')
slice_4 = matriz[:, 0]
print(slice_4)


print()
print('Outra maneira de se obter a mesma coluna:')

j = 0
j = [i[j] for i in matriz]
print(j)


print()
print('obtendo um coluna a escolha:')

k = int(input('Informe que coluna você quer obter:'))
k = [i[k] for i in matriz]
print(k)
