import xmlrpc.client

def verify_connection():
    try:
        print(proxy.connection())
    except:
        print("Ocorreu um erro! Verifique a conexão com o servidor.")
        exit()

def verify_numbers(chose, number1, number2):
    try:
        chose, number1, number2 = int(chose), int(number1), int(number2)
        return chose, number1, number2
    except:
        print("Ocorreu um erro, digite apenas números!")
        exit()

def calculate(chose, number1, number2):
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

    return result

def is_six(chose):
    if(int(chose) == 6):
        exit()

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
chose = 0
print("Bem vindo a calculadora remota")

verify_connection()

while(True):
    print("Digite: \n1-Soma 2-Subtração 3-Multiplicação 4-Divisão 5-Potenciação 6-Sair:")
    chose = input()
    is_six(chose)
    number1 = input('Digite o primeiro número da operação: ')
    number2 = input('Digite o segundo número da operação: ')
    
    chose, number1, number2 = verify_numbers(chose, number1, number2)
    
    result = calculate(chose, number1, number2)

    print("A resposta é: {}".format(result))

