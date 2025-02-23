#Exercício 1 - Soma de dois números
'''
num1 = float(input("Digite um número "))
num2 = float(input("Digite outro número "))
soma = num1 + num2
print("A soma é ", soma)
'''

#Exercício 2 - Número é ímpar?
'''
num = float(input("Digite um número "))
numPar = num%2
print("O número é ímpar? ", numPar!=0)
'''

#Exercício 3 - Valor1 é maior que 3 ou valor2 é menor que 4?
'''
valor1 = float(input("Digite um valor "))
valor2 = float(input("Digite outro valor "))
print(valor1, " é maior que 3?", valor1 > 3)
print(valor2, "é menor que 4?", valor2 < 4)
'''

#Exercício 4 - Calcular o valor absoluto
'''
valor = float(input("Digite um valor "))
print("Valor absoluto:", abs(valor))
'''

#Exercício 5 - Verificar se os valores são pares
'''
num1 = float(input("Digite um número "))
num2 = float(input("Digite outro número "))
print(num1, "é par", num1%2 == 0)
print(num2, "é par?", num2%2 == 0)
'''

#Exercício 6 - Verificar se um dos valores é negativo
'''
valor1 = float(input("Digite um valor "))
valor2 = float(input("Digite outro valor "))
print(valor1, "é negativo?", valor1<0)
print(valor2, "é negativo?", valor2<0)
'''

#Exercício 7 - Média de 3 valores
'''
num1 = float(input("Digite um número "))
num2 = float(input("Digite outro número "))
num3 = float(input("Digite mais um número "))
media = (num1 + num2 + num3)/3
print(f"A média é: {media}")
'''

#Exercício 8 - O resultado da expressão valor1+15 = valor2*3  é True ou False?
'''
valor1 = float(input("Digite um valor "))
valor2 = float(input("Digite outro valor "))
resultado = valor1+15 == valor2*3
print(valor1, "+ 15 é igual a ", valor2, "* 3? ", resultado)
'''

#Exercício 9 - Calcular resultado e resto da divisão e exibir todas as informações
'''
dividendo = float(input("Digite o valor a dividir "))
divisor = float(input("Digite o divisor "))
resultado = dividendo//divisor
resto = dividendo%divisor
print("O resultado da divisão é: ", resultado, ". E o resto é: ", resto)
'''

#Exercício 10 - Converter graus Celsius em Fahrenheit
'''
celsius = float(input("Digite a temperatura em °c "))
fahrenheit = int((celsius*9)/5 + 32)
print(f"A temperatura em fahrenheit é: {fahrenheit}°F")
'''

#Exercício 11 - Calcular o índice de massa corporal da pessoa e mostrar a resposta com no máximo 2 dígitos decimais
'''
peso = float(input("Digite seu peso em kg "))
altura = float(input("Digite sua altura "))
imc = peso/(altura)**2
print(f"Seu IMC é: {imc:.02f}")
'''

#Exercício 12 - Calcular média ponderada de três notas
'''
nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))
nota3 = float(input("Digite a terceira nota "))

peso1 = 5
peso2 = 2
peso3 = 3

Mp = ((nota1*peso1) + (nota2*peso2) + (nota3*peso3))/(peso1+peso2+peso3)

print(f"A média ponderada é: {Mp}")
'''

#Exercício 13 - Potência
'''
num = float(input("Digite um número "))
exp = float(input("Digite o expoente "))
potencia = num**exp
print(f"Resultado: {potencia}")
'''

#Desafio 1 - Raiz cúbica
'''
n = float(input("Digite um número "))
raizC = n**(1/3)
print(f"A raiz cúbica é: {raizC}")
'''

#Desafio 2 - Calcular o montante após um período de tempo com juros composto
''
c = float(input("Digite o valor do capital inicial "))
taxa = float(input("Digite a taxa de juros "))
t = int(input("Digite o tempo em anos "))

taxaDecimal = taxa/100

montante = c * (1+taxaDecimal) ** t

print(f"Valor do montante: {montante:.02f}")
''