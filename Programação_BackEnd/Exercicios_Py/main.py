#01 - Calcular o dobro do preço de três produtos
'''
produtoA = 5.00
produtoB = 8.00
produtoC = 12.00

promoA = produtoA*2
promoB = produtoB*2
promoC = produtoC*2

print(f"Promocção relâmpago!!!\nProdutoA: R${promoA:.2f}\nProdutoB: R${promoB:.2f}\nProdutoC: R${promoC:.2f}")
'''

#02 - Sistema de boas-vindas para um curso online
'''
novos_alunos = ["João", "Maria", "Carlos"]

for nome in novos_alunos:
    print(f"{nome}, bem-vindo(a) ao curso de Desenvolvimento de Sisitemas!")
'''

#03 - Se o número que cair no dado for par, o jogador avança, senão, recua
'''
numeros = [4, 7, 10]
for n in numeros:
    if n % 2 == 0:
        print(f"Número {n}. Jogador avança!")
    else:
        print(f"Número {n}. Jogador recua!")
'''

#04 - Gerar tabuadas do 2, 3 e 4
'''
print("Tabuada do 2")
for n in range (1,11):
    resultado = 2*n
    print(f"2 * {n} = {resultado}")
print()
print("Tabuada do 3")
for n in range(1,11):
    resultado = 3*n
    print(f"3 * {n} = {resultado}")
print()
print("Tabuada do 4")
for n in range(1,11):
    resultado = 4*n
    print(f"4 * {n} = {resultado}")
'''

#05 - Verificar se três clientes podem assistir um filme para maiores de 18 anos
'''
idades = [15, 20, 8]
for idade in idades:
    if idade < 18:
        print(f"Cliente de {idade} anos não pode assistir ao filme")
    else:
        print(f"Cliente de {idade} anos pode assistir ao filme")
'''

#06 - 10% de desconto em cada produto
'''
produto1 = 50
produto2 = 120
produto3 = 200
desconto = 0.1

preço_final1 = produto1 - (produto1 * desconto)
preço_final2 = produto2 - (produto2 * desconto)
preço_final3 = produto3 - (produto3 * desconto)

print(f"Somente hoje!!! Produtos com 10% de desconto:\nProduto 1: R${preço_final1:.2f}\nProduto 2: R${preço_final2:.2f}\nProduto 3: R${preço_final3:.2f}")
'''

#07 - Quantas letras têm as palavras
'''
palavras = ["casa", "paralelepípedo", "python"]

for palavra in palavras:
    contador = 0
    for c in palavra:
        contador += 1
    print(f"{palavra} tem {contador} letras")
'''

#08 - Converter temperaturas de Celsius para Fahrenheit
'''
temperaturas_celsius = [30, 100, 0]

print("Temperaturas em Fahrenheit:")
for temp in temperaturas_celsius:
    fahrenheit = (temp * 9/5) + 32
    print(f"{fahrenheit:.0f}°F")
'''

#09 - Classificar os números como "pequeno", "médio" ou "grande"
n1 = 3
n2 = 9
n3 = 12

if (n2 > n1 < n3):
    print(f"{n1} é Pequeno")
elif (n3 > n2 < n1):
    print(f"{n2} é Pequeno")
else:
    print(f"{n3} é Pequeno")