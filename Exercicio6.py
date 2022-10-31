from datetime import *
print('Preencha sua data de nascimento.')
d = int((input('Dia:')))
m = int((input('Mês:')))
a = int((input('Ano:')))
data = date(year= a, month= m, day= d)
if m == 1:
    print(data.strftime('Você nasceu em %d de janeiro de %Y'))
elif m == 2:
    print(data.strftime('Você nasceu em %d de fevereiro de %Y'))
elif m == 3:
    print(data.strftime('Você nasceu em %d de março de %Y'))
elif m == 4:
    print(data.strftime('Você nasceu em %d de abril de %Y'))
elif m == 5:
    print(data.strftime('Você nasceu em %d de maio de %Y'))
elif m == 6:
    print(data.strftime('Você nasceu em %d de junho de %Y'))
elif m == 7:
    print(data.strftime('Você nasceu em %d de julho de %Y'))
elif m == 8:
    print(data.strftime('Você nasceu em %d de agosto de %Y'))
elif m == 9:
    print(data.strftime('Você nasceu em %d de setembro de %Y'))
elif m == 10:
    print(data.strftime('Você nasceu em %d de outubro de %Y'))
elif m == 11:
    print(data.strftime('Você nasceu em %d de novembro de %Y'))
elif m == 12:
    print(data.strftime('Você nasceu em %d de dezembro de %Y'))