from auxilio.formatar import *
from auxilio.variaveis import *
from corrigir import *
from auxilio.somatorio import *
from geradores.gerar_json_aluno import *
from geradores.gerar_json_geral_disciplina import *
from geradores.gerar_json_geral_redacao import *
from leitura_e_escrita.escrever_arquivo import *
from leitura_e_escrita.ler_arquivo import *


# Variáveis base globais
dados_alunos_url = "./input/alunos/cpfs.csv"
redacoes_url = "./input/redacoes/"
gabarito_url = "./input/gabarito/gabarito.csv"
tipo_correcao = "simuenem"

# Leitor de arquivos
dados_alunos = ler_csv(dados_alunos_url)
gabarito = ler_csv(gabarito_url)
# redacoes = ler_csv(redacoes_url)

# Processadores de dados
respostas = formatar_respostas(aplicacoes, tipo_correcao)
# redacoes = formatar_redacao(redacoes, dados_alunos)

redacoes = []

# Corrigir Provas
correcao = corrigir(respostas, gabarito, redacoes, tipo_correcao)

escrever_csv("./output/respostas.csv", respostas)
escrever_csv("./output/correcao.csv", correcao)

# subjects = gerar_json_disciplinas(correcao, gabarito)
# writing = gerar_json_redacao(correcao, len(redacoes))
# student_dataset = gerar_json_alunos(
#     correcao, respostas, dados_alunos, gabarito)

# data = {
#     "config": {
#         "role": 0,
#         "type": 4,
#         "version": "I 07/2022",
#         "name": "SIMUFSC 2022"
#     },
#     "general": {
#         "subjects": subjects,
#         "writing": writing,
#     },
#     "student_dataset": student_dataset
# }

# escrever_json('./output/data.json', data)
