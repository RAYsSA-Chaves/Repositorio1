#1
'''nome = "João"
print(nome)'''

#2
'''a = 5
b= 10
soma = a + b
subtraçao = a - b
multiplicaçao = a*b
divisao = 5/10
print(f"Soma = {soma}. Subtração = {subtraçao}. Multiplicação {multiplicaçao}. Divisão = {divisao}")'''

#3
'''preço = 50
desconto = 10
desconto = 50/10
resultado = 50 - desconto
print(f"Preço com desconto: R${resultado}")'''

#4
'''resultado = 10 + 5 * 2
print(resultado)'''

#5
'''texto = "150"
valor = int(texto)
print(valor*2)'''

#6 PULAR

#7
'''a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
print("Soma:", a+b)'''

#8
'''x = float(input("Valor 1: "))
y = float(input("Valor 2: "))
divisao = x//y
print("Resultado:", divisao)'''


#9
'''num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
VF = num1>num2
print("Número 1 é maior que o número 2? ", VF)'''

#10
'''idade = int(input("Digite sua idade: "))
diasVividos = idade * 365
print(f"Você já viveu {diasVividos} dias")'''

#11
'''base = float(input("Valor da base: "))
expoente = float(input("Valor do expoente: "))
resultado = base ** expoente
print(f"Resultado: {resultado}")'''

#12
'''preco = float(input("Preço: "))
string = str(preco)
print("O preço é R$" + string)'''

#13
'''raio = float(input("Raio: "))
area_circulo = 3.14 * raio**2
print(f"A área do circulo é: {area_circulo}")'''

#14
'''a = float(input("Valor 1: "))
b = float(input("Valor 2: "))
print(a, b)
a, b = b, a
print(a, b)'''

#15
'''nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

peso1 = 2
peso2 = 3
peso3 = 5

mediaP = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
print("A média ponderada é:", mediaP)'''

#16
import math
x1 = float(input("Valor 1: "))
y1 = float(input("Valor 2: "))
x2 = float(input("Valor 3: "))
y2 = float(input("Valor 4: "))

D = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distância dos pontos é: {D}")