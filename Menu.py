'''
este programa implementa um sistema de MENU

autor : Gustavo
data : 16/11/2023


'''

print("MENU")
print("1- escrever 'OLA'")
print("2- escrever 'TUDO BEM?'")
print("3- escrever 'BOA NOITE'")
print("4- Escrever 'TCHAU'")
print("5- sair do programa")

opcao = int(input("digite sua opção"))

while opcao != 5:
    if opcao == 1:
        print("OLA")
    elif opcao == 2:
        print("TUDO BEM?")
    elif opcao == 3:
        print("BOA NOITE")
    elif opcao == 4:
        print("TCHAU")
    else:
        print("opção inválida")
    #fim se

    print("MENU")
    print("1- escrever 'OLA'")
    print("2- escrever 'TUDO BEM?'")
    print("3- escrever 'BOA NOITE'")
    print("4- Escrever 'TCHAU'")
    print("5- sair do programa")

    opcao = int(input("digite sua opção"))
#fim do programa
#
print("fim do programa")

