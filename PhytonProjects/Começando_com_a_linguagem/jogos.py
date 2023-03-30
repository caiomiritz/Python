import forca
import advinhacao

def escolha():
    print("----------------------------------")
    print("         Escolha seu jogo         ")
    print("----------------------------------")

    print("(1) Forca (2) Advinhação")
    escolha = int(input("Qual o jogo ? "))

    if(escolha == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(escolha == 2):
        print("Jogando Advinhação")
        advinhacao.jogar()
    else:
        print("Jogo inválido")

if(__name__ == "__main__"):
    escolha()