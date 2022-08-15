import csv
import json
from auxilio.formatar import *
from auxilio.variaveis import *
from corrigir import *
from auxilio.somatorio import *
from geradores.gerar_json_aluno import *
from geradores.gerar_json_geral_disciplina import *
from geradores.gerar_json_geral_redacao import *
from leitura_e_escrita.escrever_arquivo import *
from leitura_e_escrita.ler_arquivo import *

dados_formatados = formatar_dados(aplicacoes)

escrever_csv("./output/output.csv", dados_formatados)

dados_alunos = ler_csv("./input/cpfs.csv")
gabarito = ler_csv("./input/Gabarito.csv")
redacoes = ler_csv("./input/redacao.csv")

redacoes = formatar_redacao(redacoes, dados_alunos)

correcao = corrigir(dados_formatados, gabarito, redacoes)

escrever_csv("./output/correcao.csv", correcao)

subjects = gerar_json_disciplinas(correcao, gabarito)
writing = gerar_json_redacao(correcao, len(redacoes))

students_dataset = gerar_json_alunos(correcao, dados_alunos, gabarito)

data = {
    "config": config,
    "general": {
        "subjects": subjects,
        "writing": writing,
    },
    "students_dataset": students_dataset
}

escrever_json('./output/data.json', data)
