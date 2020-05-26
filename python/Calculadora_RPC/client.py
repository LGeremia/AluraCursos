import xmlrpc.client

def verify_connection():
    try:
        print(proxy.connection())
    except:
        print("Ocorreu um erro! Verifique a conexão com o servidor.")
        exit()

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
chose = 0
print("Bem vindo a calculadora remota")

verify_connection()

while(chose != 6):
    print("Digite: \n1-Soma 2-Subtração 3-Multiplicação 4-Divisão 5-Potenciação 6-Sair:")
    chose = int(input())
    number1 = int(input('Digite o primeiro número da operação: '))
    number2 = int(input('Digite o segundo número da operação: '))
    
    if(chose == 1):
        result = proxy.add(number1, number2)
    elif(chose == 2):
        result = proxy.subtract(number1, number2)
    elif(chose == 3):
        result = proxy.multiply(number1, number2)
    elif(chose == 4):
        result = proxy.divide(number1, number2)
    elif(chose == 5):
        result = proxy.potentiation(number1, number2)
    elif(chose != 6):
        print("Opção inválida, tente novamente")
        chose = 0

    print("A resposta é: {}".format(result))

