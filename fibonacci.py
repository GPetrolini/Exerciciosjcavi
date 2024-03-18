'''
Este programa desenvolve a série dddedddd Fibonacci

autor : Gustavo
data : 16/11/2023

'''


n = int(input("Digite até qual termo deseja vizualizar"))

a = 1 
b = 1 

print (a,",",b,",",end = "")

for i in range(n-2):
    c = a + b
    print(c,",",end="")
    a = b 
    b = c
#fim para

print(". .")
