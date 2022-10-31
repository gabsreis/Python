nomes = []
newName =""
for i in range(3):
    nome=input('Digite o nome %d'%(i+1))
    nomes.append(nome)
print(nomes)
for nome in nomes:
    newName=newName + nome[0] + nome[1]
print(newName)