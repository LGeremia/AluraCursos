names = []
import re

def menu():
    chose = 0
    while (chose != 6):
        chose = int(input("Digite 1-Cadastrar 2-Excluir 3-Listar 4-Atualizar 5-Pesquisar e 6-Sair: "))
        remove = ''
        name = ''
        update = ''
        if (chose == 1):
            name = input("digite o nome que deseja cadastrar: ")
            create_name(name)
        elif (chose == 2):
            remove = input("digite o nome que deseja remover: ")
            delete_name(remove)
        elif (chose == 3):
            show_list(names)
        elif (chose == 4):
            update = input("Digite o nome da lista que deseja atualizar: ")
            update_name(update, names)
        elif (chose == 5):
            search_name(names)
        
def create_name(name):
    names.append(name)

def show_list(names):
    for nome in names:
        print(nome)

def delete_name(remove):
    names.remove(remove)

def search_name(names):
    regular_expression = input("Digite a expressão regular: ")
    concatenated_names = ''.join(names)
    search = re.findall(regular_expression, concatenated_names)
    print(search)

def update_name(name, names):
    i = 0
    for laranja in names:
        if laranja == name:
            atualizador = input("Digite o nome de deseja por: ")
            print(i)
            names[i] = atualizador
        i = i+1

menu()
