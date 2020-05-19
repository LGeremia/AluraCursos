def calcula_idade():
    ano_como_string = input("Digite o ano que você nasceu: ")
    ano_como_int = int(ano_como_string)
    idade = (2020 - ano_como_int)
    print("Sua idade atual é: ", idade)

def cadastrar(names):
    name = input("Digite o seu nome: ")
    names.append(name)

def remover(names):
    name = input("Digite o nome que gostaria de remover: ")
    names.remove(name)