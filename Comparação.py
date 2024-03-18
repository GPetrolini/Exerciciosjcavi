'''
Este programa em python permite a leitura de duas variaveis x e y 
e a verificação se são iguais ou diferentes de zero

autor: Gustavo Petrolini
data: 14/11/2023

'''

x = int (input("digite o valor da primeiro operando"))

y = int (input("digite o valor do segundo operando"))

if  x == 0: 
    print(x, "é igual a zero")
else:
    print(x, "é diferente de zero")
#fim do se

if y != 0:
    print(y,"é diferente de zero")
else:
    print(y,"é igual a zero")
#fim se


print("FIM DO PROGRAMA")