'''
este programa é um jogo de advinhação onde o usuário tenta acertar o número gerado de forma 
secreta pelo programa
autor : GUstavo
data: 21/11/2023



'''

from random import randint

gerado = int(randint(0,9))

tentativa = 0

valor = -1

while valor != gerado:
    tentativa = tentativa + 1
    valor = int(input("faça sua tentativa, digite um número entre 0 e 9"))
    if valor == gerado:
        print("parabéns...você acertou em",tentativa,"tentativa(s)")
    elif valor > gerado:
        print("você errou, tente um valor menor")
    else:
        print("você errou, tente um valor maior")
    #fim se
#fim enquanto

print("fim do programa")


