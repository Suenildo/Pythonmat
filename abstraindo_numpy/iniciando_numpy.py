"""
Numpy é um pacote para computação científica usado em Python,
que fornece recursos e uma variedade de rotinas para operações
rápidas em matrizes, incluindo matemática, lógica, manipulação
de formas, classificação, seleção, E/S (I/O), transformações
discretas de Fourier, álgebra linear básica, operações estatísticas
básicas, simulação aleatória e muito mais.
"""

# O numpy não é nativo, caso você não tenha, terá que instalar.

'''Você pode utilizar o pip no console para instalar o Numpy 
se você tiver instalado o Python 3, não importa se o sistema operacional.
digite:     ((( pip install numpy))) '''

# Para iniciar, temos que importar o Numpy:

import numpy as np

# O "np" é um elias (apelido), para facilitar a sua chamada.

# Localização do Numpy:
print('Onde eu estou:')
print(np)


print()

# Checando a versão:
print('Minha versão:')
print(np.__version__)

print()

# Identificando o Blas que o Numpy está usando:
print('Estou usando o BLAS:')
print(np.__config__.show())

'''BLAS é a parte de baixo nível do seu sistema que é responsável 
por realizar de forma eficiente a álgebra linear numérica, ou seja, 
todos os cálculos pesados de números. Mais precisamente:

Subprogramas básicos de álgebra linear (BLAS) é uma especificação que 
prescreve um conjunto de rotinas de baixo nível para a realização de 
operações comuns de álgebra linear, como adição de vetores, 
multiplicação escalar, produtos escalares, combinações lineares 
e multiplicação de matrizes. Elas são as rotinas de baixo nível 
padrão de fato para bibliotecas de álgebra linear; as rotinas têm 
ligações para C e Fortran. Embora a especificação do BLAS seja geral,
as implementações do BLAS são frequentemente otimizadas para 
velocidade em uma máquina específica, portanto, usá-las pode trazer 
benefícios de desempenho substanciais.'''


