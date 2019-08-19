def jogar():
    print("***********************************")
    print("*** Bem vindo ao jogo de Forca! ***")
    print("***********************************")

    palavra_secreta = "abacaxi".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    acertou = False
    enforcado = False
    tentativas = 0

    print(letras_acertadas)

    while(not enforcado and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("Ops, você errou! Faltam {} tentativas"
                  .format(6 - tentativas))

        print(letras_acertadas)

        acertou = "_" not in letras_acertadas
        enforcado = tentativas == 6

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu")

    print("Fim do jogo!")


if(__name__ == "__main__"):
    jogar()
