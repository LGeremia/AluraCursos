import random

def playing_adivinha():
    secret_number = random.randrange(1,101)
    score = 100
    select = 0

    print("Jogo do Advinha")
    print('Escolha o nível de dificuldade:')
    level = int(input("1-Fácil 2-Intermediário 3-Difícil: "))

    if(level == 1):
        total = 15
    elif(level == 2):
        total = 10
    elif(level == 3):
        total = 5
    else:
        print("Opção inválida!!!")
        exit()

    for actual_round in range(1, total+1):
        print("Tentativa {} de {} ".format(actual_round, total))
        select = int(input("Digite um número entre 0 e 100: "))

        if(select < 0 or select > 100):
            print("Valor inválido, tente novamente!")
            continue

        if(select == secret_number):
            print("Acerto Miseravi!!!!!")
            break
        elif(select > secret_number):
            print("Errooooo!!!! O número secreto é menor do que você digitou: ")
            score = score-abs(secret_number - select)
        elif(select < secret_number):
            print("Errooooo!!!! O número secreto é maior do que você digitou: ")
            score = score-abs(secret_number - select)

    print("Fim de jogo, a sua pontuação foi {} e o número secreto era: {}".format(score, secret_number))

    '''
    while (actual_round <= total):
        print("Tentativa {} de {} ".format(actual_round, total))
        select = int(input("Digite um número: "))

        if(select == secret_number):
            print("Acerto Miseravi!!!!! O numero secreto é: {}".format(secret_number))
            break
        elif(select > secret_number):
            print("Errooooo!!!! O número secreto é menor do que você digitou: ")
        elif(select < secret_number):
            print("Errooooo!!!! O número secreto é maior do que você digitou: ")

        actual_round += 1
    '''
if(__name__ == "__main__"):
    playing_adivinha()
