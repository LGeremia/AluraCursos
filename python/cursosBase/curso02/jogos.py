import advinha
import forca
def chosing_game():
    print("Qual jogo você deseja jogar?")
    game = int(input("1-Adivinhação 2-Forca"))

    if(game == 1):
        advinha.playing_adivinha()
    elif(game == 2):
        forca.playing_forca()

if(__name__ == "__main__"):
    chosing_game()
