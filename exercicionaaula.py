x = int(input("Quantidade de cópias:"))
while x < 0:
    print("Valor inválido!!")
    x = int(input("Quantidade de cópias:"))
if x <= 2:
    print(f"{x} *0,10 = {x*0.10} ")
elif x > 2 and x <= 10:
    print(f"{x}*0,10 ={x*0.10}")
elif x > 10 and x <= 100:
    print(f"{x}*0,06 = {x*0.06}")
else:
    print(f"{x}*0,04 = {x*0.04}")