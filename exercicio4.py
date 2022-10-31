# O código é composto por uma lista notas, que recebe as notas de 20 alunos;
# Divididos em duas turmas de 10 alunos;
# O programa pede o preenchimento das 20 notas;
# Ao final, é feito um cálculo da média das notas de cada turma e essa média é impressa na tela.  
notas = []
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