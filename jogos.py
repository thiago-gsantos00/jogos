import forca
import adivinhacao

def escolhe_jogo():
    print("***************************")
    print("*** Escolha o seu jogo! ***")
    print("***************************")

    print("Selecione o jogo")
    jogo = int(input("(1) Forca (2) Adivinhação: "))

    if(jogo == 1):
        print("Iniciando Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Iniciando Jogo da Adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()