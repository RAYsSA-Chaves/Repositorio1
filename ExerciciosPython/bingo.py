#Sorteador para um Bingo

import random

qtd_sorteada = 0

while qtd_sorteada%5 != 0:
    valor_aleatorio = random.sample(75,1)
    print("Número: ", valor_aleatorio)