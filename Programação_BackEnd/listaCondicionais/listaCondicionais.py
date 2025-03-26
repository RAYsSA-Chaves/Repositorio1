#01
'''
num = float(input("Número: "))
resultado = num % 2
if resultado == 0:
    print(num, "é par")
else:
    print(num, "é ímpar")
'''


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
if nota >= 9:
    print("Nota A")
elif nota >= 7:
    print("Nota B")
elif nota >= 5:
    print("Nota C")
elif nota >= 2:
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
'''
data = input("Digite uma data no formato dd/mm/aaaa: ")

#verificar se está no formato correto -> 10 caracteres no total e "/" nos lugares certos:
if len(data) == 10 and data[2] == "/" and data[5] == "/":
    dia, mes, ano = data.split("/") #split = separar; baseado em um separador específico
    print(f"Data convertida: {ano}-{mes}-{dia}")
else:
    print("Formato inválido")
'''


#15
'''
import re 
#serve para trabalhar com expressões regulares e buscar, substituir e manipular textos

print("A senha deve conter no mínimo 8 caracteres, 1 letra maiúscula, 1 letra minúscula, 1 número e 1 caractere especial (@, #, $, %, &)")
senha = input("Crie uma senha: ")

qtd_valida = len(senha) >= 8
tem_maiuscula = bool(re.search(r"[A-Z]", senha))
tem_minuscula = bool(re.search(r"[a-z]", senha))
tem_numero = bool(re.search(r"[0-9]", senha))
tem_especial = bool(re.search(r"[@#$%&]", senha))

if (qtd_valida and tem_maiuscula and tem_minuscula and tem_numero and tem_especial) == True:
    print("Senha definida com sucesso!")
elif qtd_valida == False:
    print("A senha deve ter pelo menos 8 caracteres!")
elif tem_maiuscula == False:
    print("Falta uma letra maiúscula!")
elif tem_minuscula == False:
    print("Falta uma letra minúscula!")
elif tem_numero == False:
    print("Falta um número!")
else:
    print("Falta um caractere especial (@, #, $, %, &)")
'''


#16
'''
num = int(input("Número: "))
if num < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo")
elif num > 100:
    print("Número muito grande, reduza para um valor abaixo de 100")
else:
    resultado = num**0.5
    print(f"Resultado: {resultado:.02f}")'
'''


#17
'''
data = input("Digite uma data no formato dd/mm/aaaa: ")

qtdValida = len(data) == 10 and data[2] == "/" and data[5] == "/"
dia, mes, ano = data.split("/")
digitoValido = dia.isdigit() and mes.isdigit() and ano.isdigit() #verifica se é número
dia = int(dia)
mes = int(mes)
ano = int(ano)
mesValido = mes > 1 and mes < 12

if (qtdValida and digitoValido and mesValido) == True:
    if mes == (4 or 6 or 9 or 11):
        dataValida = dia >= 1 and dia <= 30
    elif mes == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        dataValida = dia >=1 and dia <= 31
    else:
        if ano % 4 == 0 or (ano % 100 == 0 and ano % 400 == 0):
            dataValida = dia >= 1 and dia <= 29
        else:
            dataValida = dia >= 1 and dia <= 28
else:
    dataValida = False

if dataValida == True:
    print(f"Data convertida: {ano}-{mes:02d}-{dia:02d}")
else:
    print("Data inválida")
'''


#18
import re

expressao = input("Digite uma expressão matemática: ")

if re.fullmatch(r"[0-9+-*/().]", expressao):
    resultado = eval(expressao) #eval -> analisa expressões armazenadas como strings
    print("Resultado: ", resultado)
else:
    print("Expressão inválida")
