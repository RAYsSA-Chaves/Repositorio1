#Jogo pedra, papel, tesoura:

import random

escolhaUsuario = input("Escolha uma opção: Pedra, Papel ou Tesoura: ").upper()

opçoes = ["Pedra", "Papel", "Tesoura"]
escolhaComputador = random.choice(opçoes)
print("Computador:", escolhaComputador)

if escolhaUsuario == "PEDRA":
        if escolhaComputador == "Papel":
            print("Computador ganhou")
        elif escolhaComputador == "Tesoura":
            print("Você ganhou")
        else:
            print("Empate")
elif escolhaUsuario == "PAPEL":
    if escolhaComputador == "Pedra":
        print("Você ganhou")
    elif escolhaComputador == "Tesoura":
        print("Computador ganhou")
    else:
        print("Empate")
elif escolhaUsuario == "TESOURA":
    if escolhaComputador == "Pedra":
        print("Computador ganhou")
    elif escolhaComputador == "Papel":
        print("Você ganhou")
    else:
        print("Empate")
else:
    print("Opção inválida")