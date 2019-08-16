import random

def jogar():

    print("*****************************************")
    print("*** Bem vindo ao jogo de Adivinhação! ***")
    print("*****************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontuacao = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou o número", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        eh_maior = chute > numero_secreto
        eh_menor = chute < numero_secreto

        if(acertou):
            print(f"Parabéns! Você acertou e fez {pontuacao} pontos")
            break
        else:
            if(eh_maior):
                print("Você errou! O número digitado é maior que o número secreto")
            elif(eh_menor):
                print("Você errou! O número digitado é menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()