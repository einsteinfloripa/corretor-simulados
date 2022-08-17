from auxilio.formatar import *
from auxilio.variaveis import *
from corrigir import *
from auxilio.somatorio import *
from geradores.gerar_json_aluno import *
from geradores.gerar_json_geral_disciplina import *
from geradores.gerar_json_geral_redacao import *
from leitura_e_escrita.escrever_arquivo import *
from leitura_e_escrita.ler_arquivo import *

dados_alunos = ler_csv("./input/cpfs.csv")
redacoes = ler_csv("./input/redacao.csv")
gabarito = ler_csv("./input/gabarito.csv")

respostas = formatar_respostas(aplicacoes)
redacoes = formatar_redacao(redacoes, dados_alunos)

correcao = corrigir(respostas, gabarito, redacoes)

escrever_csv("./output/respostas.csv", respostas)
escrever_csv("./output/correcao.csv", correcao)

subjects = gerar_json_disciplinas(correcao, gabarito)
writing = gerar_json_redacao(correcao, len(redacoes))
student_dataset = gerar_json_alunos(correcao, respostas, dados_alunos, gabarito)

data = {
    "config": {
        "role": 0,
        "type": 4,
        "version": "I 07/2022",
        "name": "SIMUFSC 2022"
    },
    "general": {
        "subjects": subjects,
        "writing": writing,
    },
    "student_dataset": student_dataset
}

escrever_json('./output/data.json', data)
