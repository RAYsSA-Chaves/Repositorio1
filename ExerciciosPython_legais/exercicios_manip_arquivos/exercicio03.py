#Gerar um arquivo .json a partir do arquivo .csv do exercicio 3

import pandas

#Ler o arquivo .csv
df = pandas.read_csv('pedidos2.csv')

#Gerar .json
df.to_json('pedidos3.json', orient='records', force_ascii=False, indent=4)

#orient="records" organiza as colunas do DataFrame como dicionários
#force_ascii=False mantém os caracteres como UTF-8 em vez de forçar para ASCII