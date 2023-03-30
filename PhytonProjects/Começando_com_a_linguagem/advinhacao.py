import random

def jogar():

    print("----------------------------------")
    print(" Bem vindo ao jogo da advinhação  ")
    print("----------------------------------")
    print(" ")
    
    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 100

    print("Qual o nível de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Digite a dificuldade: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas+1):
    
        print(" ")
        print("Rodada {0} de {1}".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100")
            continue
    
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acertou = chute == numero_secreto

        if(maior):
            print("O número digitado é maior que o secreto")
            pontos = pontos - (chute - numero_secreto)
        elif(menor):
            print("O número digitado é menor que o secreto")
            pontos = pontos - (numero_secreto - chute)
        else:
            print("Você acertou e fez {0} pontos".format(pontos))
            break
    
    print(" ")
    print("Fim do jogo !")    

if(__name__ == "__main__"):
    jogar()
