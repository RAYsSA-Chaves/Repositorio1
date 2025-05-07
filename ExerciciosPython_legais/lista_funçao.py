#01 - Calculadora de IMC
'''
def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    print(f"Seu IMC é {imc:.2f}")

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
calcular_imc(peso, altura)
'''


#02 - Retornar o maior número entre os n números digitados pelo usuário
'''
def maior(lista_numeros):
    maior = lista_numeros[1]
    for n in lista_numeros:
        if n > maior:
            maior = n
    return maior

qtd = int(input("Quantos números você gostaria de digitar?\n"))
lista_numeros = []
for i in range(qtd):
    num = float(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(num)

print(f"O maior número é {maior(lista_numeros)}")
'''


#03 - Converter de celsius para fahrenheit
'''
def converter_celsius_para_fahrenheit(c):
    fahrenheit = c * 1.8 + 32
    return fahrenheit

c = float(input("Digite a temperatura em graus celsius: "))
print(f"{converter_celsius_para_fahrenheit(c):.2f}°F")
'''


#04 - Calcular troco
'''
def calcular_troco(valor_compra, valor_pago):
    troco = valor_pago - valor_compra
    if troco >= 0:
        print(f"Troco: R${troco:.2f}")
    else:
        print(f"Troco: R$00,00. Pagamento insuficiente!")

valor_compra = float(input("Informe o valor da compra: R$"))
valor_pago = float(input("Informe o valor pago pelo cliente: R$"))

calcular_troco(valor_compra, valor_pago)
'''


#05 - Verificar se o número é primo

def eh_primo(n):
    divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisores += 1   

n = int(input("Digite um número inteiro para verificar se ele é primo: "))
