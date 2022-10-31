print('###Exercício 1###')
print("Números Pares no intervalor ] 1, 20 [")
n = 0
def f(n):
    for n in range(1, 20):
        if n % 2 == 0:
            print(n, end='\n')
    print("FIM")
res = f(n)
###############################################################
print('###Exercício 2###')
quantidade = 0
def g(quantidade):
    palavra = 'palavra'
    letra = 'a'
 
    for c in palavra:
        if(c==letra):
            quantidade=quantidade+1
    print(quantidade)
res = g(quantidade)
###############################################################
print('####Exercício 3###')
nomes = []
newName =""
def h(newName):
    for i in range(3):
        nome=input('Digite o nome %d'%(i+1))
        nomes.append(nome)
    print(nomes)
    for nome in nomes:
        newName=newName + nome[0] + nome[1]
    print(newName)
res = h(newName)
###############################################################
print('###Exercício 4###')
notas = []
def i(notas):
    for turma in range(2):
        notas.append([0]*10)
        print(notas)
    for turma in range(2):
        print('Preencha as notas da turma', turma+1)
        for aluno in range(10):
            print('nota do aluno', aluno+1, end=": ")
            notas[turma][aluno] = float(input())
    for turma in range (2):
        soma = 0
        for aluno in range(10):
            soma + soma + notas[turma][aluno]
        print("Média da turma ", turma,": ", soma/len(notas[turma]))
res = i(notas)
###############################################################
print('###Exercício 6###')
x = 1
def j(x):
    for x in range(1,11,):
        print(x)

    while x<6:
        print(x)
        x = x + 1
res = j(x)
###############################################################
print('###Exercício 7###')
X = [[12,7,3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
def k(result):
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
res = k(result)
###############################################################
print('###Exercício 8###')
import numpy as numpy

arr = numpy.array([0,1,2,3,4,5,6,7,8,9])

def l(arr):

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
    print("Subtração de cada elemento da matriz: ")
    print(numpy.substract(x,y))

    # Uso do divide() para dividir
    print ("Divisão de cada elemento da matriz: ")
    print(numpy.divide(x,y))

    # Uso do multiply() para multiplicar cada elemento
    print("Multiplicação de cada elemento da matriz: ")
    print(numpy.multiply(x,y))
res = l(arr)
###############################################################
print('###Exercício 9###')
print("Números Ímpares no intervalor ] 1, 20 [")
n = 0
def m(n):
    for n in range(1, 20, 2):
        if n % 1 == 0:
            print(n, end='\n')
    print("FIM")
res = m(n)