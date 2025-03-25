#01
'''
num = float(input("Número: "))
resultado = num % 2
if resultado == 0:
    print(num, "é par")
else:
    print(num, "é ímpar")
'''
from pydoc import describe
from sys import float_info

#02
'''
num = float(input("Número: "))
if num > 10:
    print("É maior que 10")
else:
    print("Não é maior que 10")
'''


#03
'''
idade = int(input("Qual a sua idade? "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
'''


#04
'''
idade = int(input("Idade: "))
if idade >= 18 and idade < 70:
    print("Voto obrigatório")
elif idade >= 16 or idade >= 70:
    print("Voto opcional")
else:
    print("Não vota")
'''


#05
'''
num = float(input("Digite um número: "))
if num > 0:
    print("Número positivo")
elif num == 0:
    print("O número é 0")
else:
    print("Número negativo")
'''


#06
'''
nota = float(input("Nota: "))
if nota == 9 or nota == 10:
    print("Nota A")
elif nota == 7 or nota == 8:
    print("Nota B")
elif nota == 5 or nota == 6:
    print("Nota C")
elif nota == 4 or nota == 3:
    print("Nota D")
else:
    print("Nota E")
'''


#07
'''
idade = int(input("Qual a sua idade? "))
if idade <= 12:
    print("Tem desconto!")
elif idade >= 60:
    print("Tem desconto!")
else:
    print("Não tem desconto")
'''


#08
'''
#é triângulo se a soma de dois dos lados for sempre (em todos os casos) maior que o terceiro lado

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1:
    print("É possível formar um triângulo.")
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("O triângulo é isóceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Não é possível formar um triângulo")
'''


#09
'''
valor = float(input("Digite o valor total da compra: "))
if valor < 100:
    desconto = valor*(5/100)
elif valor >= 100 and valor <= 500:
    desconto = valor*(10/100)
else:
    desconto = valor*(15/100)

valorFinal = valor-desconto
print("Valor com desconto: ", valorFinal)
'''


#10
'''
ano = int(input("Ano: "))
if ano%4 == 0:
    print("Ano bissexto")
elif ano%100 == 0 and ano%400 == 0:
    print("Ano bissexto")
else:
    print("Não é bissexto")
'''


#11
'''
peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso/(altura)**2

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")
'''


#12
'''
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

if n1 < n2 and n2 < n3:
    print("Ordem crescente")
elif n1 > n2 and n2 > n3:
    print("Ordem decrescente")
elif n1 == n2 == n3:
    print("Os números são iguais")
else:
    print("Os números não estão em ordem")
'''


#13
'''
t = float(input("Temperatura em °C: "))
if t < 10:
    print("Frio")
elif t < 25:
    print("Aconchegante")
elif t < 40:
    print("Quente")
else:
    print("Muito quente")
'''


#14
data = input("Digite a data: ")
data = datetime.strptime(data, dd/nm/aaaa)
print(data)