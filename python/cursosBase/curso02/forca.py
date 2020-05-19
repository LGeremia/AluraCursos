import random

def playing_forca():
    print("Jogo da Forca")
    secret_word = create_secret_word()
    word = create_characteres_secret_word(secret_word)
    wrong_rounds = 0
    right_rounds = 0
    hanged = False
    hit = False

    while(not hanged and not hit):
        print(word)
        rest = 5 - wrong_rounds
        print("Aida tem {} tentativas".format(rest))
        i = 0
        shot = shot()
        if (shot in secret_word):
            right_rounds = mark_shot(secret_word, shot)
        elif (shot not in secret_word):
            wrong_rounds += 1
            print("Desculpe mas você errou")

        hit = right_rounds == len(word)
        hanged = wrong_rounds == 5

    print(word)

    if (hit):
        print("Parabéns você descobriu a palavra secreta: {}!!!".format(secret_word))
    else:
        print("Você não tem mais tentativas....")

def create_secret_word():
    words = []
    arquivo = open("palavras.txt", "r")

    for linha in arquivo:
        linha = linha.strip()
        words.append(linha)

    number = random.randrange(0, len(words))
    secret_word = words[number]
    return secret_word
    arquivo.close()

def mark_shot(secret_word, shot):
    for letra in secret_word:
        if(letra == shot):
            word[i] = shot
            right_rounds += 1
            print("Encontrei a letra {} na posição {}".format(shot,i))
        i += 1
    return right_rounds

def shot():
    shot = input("Digite uma letra da palavra secreta: ")
    shot = shot.strip().lower()
    return shot

def create_characteres_secret_word(secret_word):
    return ["_" for char in secret_word]

if(__name__ == "__main__"):
    playing_forca()
