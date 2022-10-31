#Vetores e matrizes são coleções de variáveis contínuas na memória e acessadas por meio de um número de índice.
#A diferença entre vetores e matrizes é que vetores são de uma única dimensão,
#enquanto matrizes podem conter váruas dimensões.

#- Programa com vetor
#Números ímpares com Numpy em um array de única dimensão
import numpy as numpy

arr = numpy.array([0,1,2,3,4,5,6,7,8,9])

arr[arr % 2 == 1]

#- Programa com matrizes

# Importando Numpy para opreações de matriizes
import numpy

# Inicialização de marizes de duas dimensões 
x = numpy.array([[1,2], [4,5]])
y = numpy.array([[7,8],[9,10]])


# Uso do add() para adicionar
print("Adição de cada elemento da metriz: ")
print(numpy.add(x,y))

# Uso do substract() para subtrair
#print("Subtração de cada elemento da matriz: ")
#print(numpy.substract(x,y))

# Uso do divide() para dividir
print ("Divisão de cada elemento da matriz: ")
print(numpy.divide(x,y))

# Uso do multiply() para multiplicar cada elemento
print("Multiplicação de cada elemento da matriz: ")
print(numpy.multiply(x,y))