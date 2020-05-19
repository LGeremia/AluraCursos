print("Calculadora")
print("O que você deseja fazer?")
while True:
    i = int(input("1 - Soma 2 - Subtração 3 - Mutiplicação 4 - Divisão 5 - Sair"))
    if(i == 1):
        numero1 = int(input("Digite o 1º número"))
        numero2 = int(input("Digite o 2º número"))
        numero = numero2 + numero1
        print(numero)
    elif(i == 2):
        numero1 = int(input("Digite o 1º número"))
        numero2 = int(input("Digite o 2º número"))
        numero = numero1 - numero2
        print(numero)
    elif(i == 3):
        numero1 = int(input("Digite o 1º número"))
        numero2 = int(input("Digite o 2º número"))
        numero = numero2*numero1
        print(numero)
    elif(i == 4):
        numero1 = int(input("Digite o 1º número"))
        numero2 = int(input("Digite o 2º número"))
        numero = numero1/numero2
        print(numero)
    elif(i == 5):
        break
    else:
        print("Opção inválida")