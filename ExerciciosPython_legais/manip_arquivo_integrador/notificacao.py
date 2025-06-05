#Rayssa Chaves. 1DSTB - DS17

#02 - ENVIAR NOTIFICAÇÃO DE ATUALIZAÇÃO DO ESTOQUE POR EMAIL

import csv
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import random

#Guardando a data de hoje
hoje = datetime.today().strftime('%Y-%m-%d')  #formato: ano-mes-dia
#Guardando o horário
agora = datetime.now().strftime("%H:%M:%S")  #formato: hora:minuto:segundo
#Criando lista para guardar as linhas do arquivo
dados = []

#Escrever nova linha com a data de hoje
nova_linha = [hoje, agora, random.randint(0,3), random.randint(0,3), random.randint(0,3)]
with open("Esp8266_Receiver.csv", "a", newline="") as arquivo:  #'a' = append
    escritor = csv.writer(arquivo)
    escritor.writerow(nova_linha)

#Ler o arquivo
with open("Esp8266_Receiver.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        dados.append(linha)

#Criando as mensagens dos status
status = {
    "0": "⚪ Sem estoque, produto indisponível",
    "1": "🟢 Estoque baixo, nível crítico",
    "2": "🟡 Estoque médio, planejar",
    "3": "🔴 Estoque cheio, sem necessidade de planejamento",
}

#Configurando o servidor de email
servidor_smtp = "smtp.gmail.com"
porta = 587
usuario = "rayssa.ccmelo@gmail.com"
senha = "qcat ljei lwtz thmd"

#Conectando ao servidor
servidor = smtplib.SMTP(servidor_smtp, porta)
servidor.starttls()
servidor.login(usuario, senha)

#Mensagem
assunto = 'Aviso de Atualização do Estoque'
corpo = "Estoque atual:\n\n"
for dado in dados:
    if dado[0] == hoje:  #0 = 'Date'
        data = dado[0]
        hora = dado[1]
        corpo += f"Data: {data}, Hora: {hora}\n"
        for i in range(2, 5):
            esteira = dado[i]
            mensagem = status.get(esteira, "Erro")
            corpo += f"Esteira {i-1}: {mensagem}\n"

#Verificar como ficou o corpo do email
print(f"Corpo do e-mail gerado:\n{corpo}")

#Envio do e-mail
mensagem = MIMEText(corpo, "plain", "utf-8")
mensagem['Subject'] = assunto
mensagem['From'] = usuario
mensagem['To'] = 'rayssa.c.melo@aluno.senai.br'

#Enviando
servidor.send_message(mensagem)

#Fechando a conexão com o servidor
servidor.quit()

print("E-mail enviado com sucesso!")