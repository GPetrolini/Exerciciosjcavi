'''
este programa calcula o IMC de um atleta e verifica a situação do atleta

autor : Gustavo
data : 16/11/2023

'''


print("MENU")
print("1-ler o nome do atleta")
print("2-ler o peso do atleta")
print("3- ler a altura do atleta")
print("4- calcular o IMC")
print("5- apresentar o IMC e informar a situação do atleta")
print("6- fim do programa")

opcao = int(input("digite sua opção"))

while opcao != 6:
    if opcao == 1:
        atleta = input("digite o nome do atleta")
    elif opcao == 2:
        peso = float(input("digite o peso do atleta"))
    elif opcao == 3:
        altura = float(input("digite a altura do atleta"))
    elif opcao == 4:
        imc = peso/altura**2
    elif opcao == 5:
        if imc >= 0 and imc <19:
            print ("IMC = ",imc,"e o(a)" ,atleta, "está MUITO MAGRO")
        elif imc >=19 and imc <25:
            print("IMC =",imc,"e o(a)",atleta,"esta NORMAL")
        elif imc >=25 and imc <30:
            print("IMC =",imc,"e o(a)",atleta,"está SOBREPESO")
        elif imc >=30 and imc <40:
            print("IMC =",imc,"e o(a)",atleta,"está OBESO")
        else:
            print("o IMC =",imc,"e o(a)",atleta,"está OBESO GRAVE")
        #fim se
    else:
        print("opção inválida")
    #fim se
    print("MENU")
    print("1-ler o nome do atleta")
    print("2-ler o peso do atleta")
    print("3- ler a altura do atleta")
    print("4- calcular o IMC")
    print("5- apresentar o IMC e informar a situação do atleta")
    print("6- fim do programa")

    opcao = int(input("digite sua opção"))
#fim enquanto

print("fim do programa")


