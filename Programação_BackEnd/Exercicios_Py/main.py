#01 - Calcular o dobro do preço de três produtos
'''
produtoA = 5
produtoB = 8
produtoC = 12

promoA = produtoA*2
promoB = produtoB*2
promoC = produtoC*2

print(f"Promoção relâmpago!!!\nProduto A: R${promoA:.2f}\nProduto B: R${promoB:.2f}\nProduto C: R${promoC:.2f}")
'''


#02 - Sistema de boas-vindas para um curso online
'''
novos_alunos = ["João", "Maria", "Carlos"]

for nome in novos_alunos:
    print(f"{nome}, bem-vindo(a) ao curso de Desenvolvimento de Sistemas!")
'''


#03 - Se o número que cair no dado for par, o jogador avança, se não, recua
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
    print(f"2 x {n} = {resultado}")
print()
print("Tabuada do 3")
for n in range(1,11):
    resultado = 3*n
    print(f"3 x {n} = {resultado}")
print()
print("Tabuada do 4")
for n in range(1,11):
    resultado = 4*n
    print(f"4 x {n} = {resultado}")
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


#07 - Quantas letras as palavras tem
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
'''
n1 = 3
n2 = 9
n3 = 12

if n1 > n2 > n3:
    pequeno = n3
    medio = n2
    grande = n1
elif n2 > n1 > n3:
    pequeno = n3
    medio = n1
    grande = n2
elif n2 > n3 > n1:
    pequeno = n1
    medio = n3
    grande = n2
elif n1 > n3 > n2:
    pequeno = n2
    medio = n3
    grande = n1
elif n3 > n1 > n2:
    pequeno = n2
    medio = n1
    grande = n3
else:
    pequeno = n1
    medio = n2
    grande = n3

print(f"{pequeno} é Pequeno\n{medio} é Médio\n{grande} é Grande")
'''


#10 - Verificar se as palavras são palíndromos
'''
palavras = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]

for palavra in palavras:
    palavra_sem_espaço = palavra.replace(" ", "")
    palavra_invertida = palavra_sem_espaço[::-1]  #percorre a string de trás para frente
    if palavra_invertida.lower() == palavra_sem_espaço.lower():
        print(f'"{palavra}" é um palíndromo')
    else:
        print(f'"{palavra}" não é um palíndromo')
'''


#11 - Calcular o fatorial dos números
numeros = [3, 7, 9, 25, 26]

for n in numeros:
    contador = n
    resultado = 1
    fatorial = ""
    while contador > 0:
        resultado *= contador
        fatorial += f"{contador} x "
        contador -= 1
    print(f"{n}! = {fatorial.rstrip(" x ")} = {resultado}")