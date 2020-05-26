import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
multicall = xmlrpc.client.MultiCall(proxy)
chose = 0
print("Bem vindo a calculadora remota")

try:
    multicall.connection(1)
    result = multicall()
    result = list(result)
    print(result[0])
except:
    print("Ocorreu um erro! Verifique a conexão com o servidor.")
    exit()

while(chose != 6):
    print("Digite: \n1-Soma 2-Subtração 3-Multiplicação 4-Divisão 5-Potenciação 6-Sair:")
    chose = int(input())
    number1 = int(input('Digite o primeiro número da operação: '))
    number2 = int(input('Digite o segundo número da operação: '))

    multicall.add(number1, number2)
    multicall.subtract(number1, number2)
    multicall.multiply(number1, number2)
    multicall.divide(number1, number2)
    multicall.potentiation(number1, number2)
    result = multicall()
    result = list(result)

    if(chose == 1):
        print("O valor da soma entre {} e {} é: {}".format(number1, number2, result[chose]))
    elif(chose == 2):
        print("O valor da subtração entre {} e {} é: {}".format(number1, number2, result[chose]))
    elif(chose == 3):
        print("O valor da multiplicação entre {} e {} é: {}".format(number1, number2, result[chose]))
    elif(chose == 4):
        print("O valor da divisão entre {} e {} é: {}".format(number1, number2, result[chose]))
    elif(chose == 5):
        print("O valor da potenciação entre {} e {} é: {}".format(number1, number2, result[chose]))
    elif(chose != 6):
        chose = 0
