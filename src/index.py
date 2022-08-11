import csv
import json
from formatar import *
from gerar_json_aluno import *
from variaveis import *
from corrigir import *
from somatorio import *
from gerar_json_disciplina import *
from escrever_arquivo import *
from ler_arquivo import *

dados_formatados = formatar_dados(aplicacoes)

escrever_csv("./output/output.csv", dados_formatados)

dados_alunos = ler_csv("./input/cpfs.csv")
gabarito = ler_csv("./input/Gabarito.csv")

correcao = corrigir(dados_formatados, gabarito)

escrever_csv("./output/correcao.csv", correcao)

subjects = gerar_json_disciplinas(correcao, gabarito)

students_dataset = gerar_json_alunos(correcao, dados_alunos, gabarito)

data = {
    "config": config,
    "subjects": subjects,
    "students_dataset": students_dataset
}

escrever_json('./output/data.json', data)
