import csv
import json
from formatar import *
from variaveis import *
from corrigir import *

dados_formatados = formatar_dados(aplicacoes)

correcao = corrigir(dados_formatados)

#print(dados_formatados)

with open("./output/output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dados_formatados)