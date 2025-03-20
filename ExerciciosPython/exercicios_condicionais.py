#1 - Ano bissexto
'''
ano = int(input("Ano: "))
if ano%4 == 0:
    print("Ano bissexto")
elif ano%100 == 0 and ano%400 == 0:
    print("Ano bissexto")
else:
    print("Não é bissexto")
'''


#2 - Calculadora de IMC
'''
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura)**2

if imc < 18.5:
    classificaçao = "Peso baixo"
elif imc < 24.9:
    classificaçao = "Peso normal"
elif imc < 29.9:
    classificaçao = "Sobrepeso"
elif imc < 34.9:
    classificaçao = "Obesidade"
else:
    classificaçao = "Obesidade mórbida"

print(f"Seu IMC é: {imc:.02f} e sua classificação é: {classificaçao}")
'''


#3 - Verificação de voto
'''
idade = int(input("Digite a sua idade: "))
if idade >= 18 and idade < 70:
    print("Voto obrigatório")
elif idade >= 16 or idade >= 70:
    print("Voto facultativo")
else:
    print("Não eleitor") #menores de 16
'''


#4 - Maior e menor idade entre 3 pessoas
'''
idade1 = int(input("Idade: "))
idade2 = int(input("Idade: "))
idade3 = int(input("Idade: "))

if idade1 > idade2 and idade1 > idade3:
    maior = idade1
    if idade2 < idade3:
        menor = idade2
    else:
        menor = idade3
elif idade2 > idade1 and idade2 > idade3:
    maior = idade2
    if idade1 < idade3:
        menor = idade1
    else:
        menor = idade3
else:
    maior = idade3
    if idade1 < idade2:
        menor = idade1
    else:
        menor = idade2
        
print(f"Idade maior: {maior}. Idade menor: {menor}")
'''


#5 - Conversão de nota em letra
'''
nota = float(input("Nota: "))
if nota < 0 or nota > 10:
    letra = "Erro. Nota inválida"
elif nota >= 0 and nota < 3:
    letra = "E"
elif nota >= 3 and nota < 5:
    letra = "D"
elif nota >= 5 and nota < 7:
    letra = "C"
elif nota >= 7 and nota < 9:
    letra = "B"
else:
    letra = "A"

print("Letra: ", letra)
'''


#6 - Verificação de quadrado ou retângulo
'''
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
l4 = float(input("Lado 4: "))

if l1 == l2 == l3 == l4:
    figura = "Quadrado"
elif l1 == l2 and l3 == l4 or l1 == l3 and l2 == l4 or l1 == l4 and l2 == l3:
    figura = "Retângulo"
else:
    figura = "Nenhum dos dois"

print(figura)
'''


#7 - Calculadora simples
'''
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operaçao = input("Escolha uma operação (+, -, *, /): ")

if operaçao == "+":
    resultado = n1+n2
elif operaçao == "-":
    resultado = n1-n2
elif operaçao == "*":
    resultado = n1*n2
elif operaçao == "/":
    resultado = n1/n2
else:
    resultado = "Operação inválida"

print("Resultado: ", resultado)
'''


# Desafio - Jogo de adivinhação

import random
numAleatorio = random.randint(1, 10)

chute = int(input("Chute um número de 0 a 10: "))

if chute == numAleatorio:
    print("Acertou!")
elif chute < numAleatorio:
    print("Chutou baixo. Última tentativa")
    chute = int(input("Chute um número: "))
    if chute == numAleatorio:
        print("Acertou!")
    else:
        print("Você perdeu. O número era ", numAleatorio)
else:
    print("Chutou alto. Última tentativa")
    chute = int(input("Chute um número: "))
    if chute == numAleatorio:
        print("Acertou!")
    else:
        print("Você perdeu. O número era", numAleatorio)
