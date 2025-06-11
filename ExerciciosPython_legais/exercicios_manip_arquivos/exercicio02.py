#Gerar um arquivo .csv a partir do arquivo .xlsx do exercicio 1

import pandas

#Ler o arquivo .xlsx
df = pandas.read_excel('pedidos.xlsx')

#Gerar .csv
df.to_csv('pedidos2.csv')