#Rayssa Chaves. 1DSTB - DS17

#01 - GERAR PÁGINA HTML

import csv

#Ler o arquivo
dados = []
with open("Esp8266_Receiver.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)   #ler como um dicionário com chave (cabeçalho/primeira linha) e valor
    for linha in leitor:
        dados.append(linha)

#Criando as mensagens dos status
status = {
    "0" : "⚪ Sem estoque, produto indisponível",
    "1" : "🟢 Estoque baixo, nível crítico",
    "2" : "🟡 Estoque médio, planejar",
    "3" : "🔴 Estoque cheio, sem necessidade de planejamento",
}

#Criando a página HTML
html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Status das Esteiras - Monitoramento de Estoque</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Status das Esteiras</h1>
    <table>
        <tr>
            <th>Data</th>
            <th>Hora</th>
            <th>Esteira1</th>
            <th>Esteira2</th>
            <th>Esteira3</th>
        </tr>
"""

#Passando os dados do csv pro html
for dado in dados:
    html += (f"<tr><td>{dado['Date']}</td><td>{dado['Time']}</td>")
    for i in range(1, 4):
        esteira = dado[f"esteira{i}"]   #pega o valor da chave, ex: 2
        mensagem = status.get(esteira, "Erro")   #chave, valor_default (caso ele não encontre a chave)
        html += f"<td>{mensagem}</td>"
    html += "</tr>"

html += """
    </table>
</body>
</html>
"""

#Salvar o arquivo html
with open("monitoramento.html", "w", encoding="utf-8") as arquivo_html:
    arquivo_html.write(html)
    print("HTML gerado com sucesso!")