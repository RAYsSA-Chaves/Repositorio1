#Criptografar mensagem com cifra de césar (deslocamento 3)
mensagem = "eu gosto de python"
letras = "abcdefghijklmnopqrstuvwxyz"
mensagem_criptografada = ""

for letra in mensagem:
    if letra in letras:
        posicao = letras.index(letra)
        nova_posicao = posicao + 3
        if nova_posicao > 26:
            nova_posicao = nova_posicao - 26  #volta para o começo do alfabeto
        nova_letra = letras[nova_posicao]
        mensagem_criptografada += nova_letra
    else:
        mensagem_criptografada += letra  #espaços, números e pontuações permanecem iguais

#Guardar a mesnsagem criptografa em um .txt
with open("criptografado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(mensagem_criptografada)

#Descriptografar o arquivo .txt
letras = "abcdefghijklmnopqrstuvwxyz"
mensagem_decifrada = ""

with open("criptografado.txt", "r", encoding="utf-8") as arquivo:
    mensagem_criptografada = arquivo.read()

for letra in mensagem_criptografada:
    if letra in letras:
        posicao = letras.index(letra)
        nova_posicao = posicao - 3
        if nova_posicao < 0:
            nova_posicao = nova_posicao + 26  # volta para o fim do alfabeto
        nova_letra = letras[nova_posicao]
        mensagem_decifrada += nova_letra
    else:
        mensagem_decifrada += letra

print("Mensagem decifrada:", mensagem_decifrada)
