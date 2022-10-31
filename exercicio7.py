#Numpy é uma biblioteca para computação científica em Python, para utilizá-la é necessário importá-la.
#Essa biblioteca fornece alto desempenho e ferramentas para manipulação de arrays multidimensionais.
#Um array Numpy deve ser composto por elementos do mesmo tipo. Já uma lista(list) é nativa do Python,
#ou seja, não é necessário que uma biblioteca seja importada para ela ser utilizada.
#Além disso, uma lista em Python é equivalente a um array, mas é redimensionável e pode elementos
#de diferentes tipos. Vejam o exemplo abixo para somar duas matrizes.

#- Programa para somar duas matrizes utilizando listas

X = [[12,7,3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterar ao longo das linhas
for i in range(len(X)):
    print(X[i])
    #iterar ao longo das colunas
    for j in range (len(X[i])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

#- Programa para somar duas matrizes utilizando Numpy
import numpy as np
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
print("A:",A)
print("B:",B)
C = A + B 
print("C:", C)