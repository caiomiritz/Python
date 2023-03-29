numero_secreto = 13
tentativas = 3
rodada = 1

while(rodada <= tentativas):
    
    print("Rodada {} de {}".format(rodada, tentativas))
    chute = int(input("Digite um número: "))

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto

    if(maior):
        print("O número digitado é maior que o secreto")
    elif(menor):
        print("O número digitado é menor que o secreto")
    else:
        print("Acertou!")
        tentativas = 0
    
    rodada = rodada + 1
    if(rodada > tentativas):
        print("Perdeu !")
    


