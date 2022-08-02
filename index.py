import csv
import json
from formatar import *
from variaveis import *
from corrigir import *
from somatorio import *

dados_formatados = formatar_dados(aplicacoes)

with open("./output/output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dados_formatados)

with open(f"./input/Gabarito.csv", "r", encoding="utf-8") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    gabarito = [row for row in reader]

correcao = corrigir(dados_formatados, gabarito)

with open("./output/correcao.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(correcao)
