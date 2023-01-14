from auxilio.formatar import *
from auxilio.variaveis import *
from corrigir import *
from auxilio.somatorio import *
from geradores.gerar_json_aluno import *
from geradores.gerar_json_geral_disciplina import *
from geradores.gerar_json_geral_redacao import *
from leitura_e_escrita.escrever_arquivo import *
from leitura_e_escrita.ler_arquivo import *
import cli

# Variáveis INPUT Usuário
dados_alunos_path, respostas_alunos_path, gabarito_path, redacoes_path, tipo_correcao = cli.get_input_usuario()

# Leitor de arquivos
df_dados_alunos = ler_csv(dados_alunos_path, nome_col_df_dados_alunos)
df_respostas = ler_csv(respostas_alunos_path, nome_col_df_respostas)
df_gabarito = ler_csv(gabarito_path, nome_col_df_gabarito)
# df_redacoes = ler_csv(redacoes_path)
df_redacoes = []   # PLACE HOLDER

# Processadores de dados
#####respostas = formatar_respostas(aplicacoes, tipo_correcao)
# redacoes = formatar_redacao(redacoes, dados_alunos)  ## NÃO IMPLEMENTADO

# Corrigir Provas
df_resultado = corrigir(df_respostas, df_gabarito, df_redacoes, tipo_correcao)

# escrever_csv("./output/respostas.csv", respostas)  ### Igual ao input...
escrever_csv("./output/resultado.csv", df_resultado)
escrever_csv("./output/gabarito.csv", df_gabarito)

subjects = gerar_json_disciplinas(df_resultado, df_gabarito, tipo_correcao)
# writing = gerar_json_redacao(correcao, len(redacoes))

escrever_json('./output/data.json', subjects)
###### ^^^ OK ^^^ ######

student_dataset = gerar_json_alunos(df_resultado, df_gabarito, tipo_correcao)

data = {
    "config": {
        "role": 0,
        "type": 4,
        "version": "I 07/2022",
        "name": "SIMUFSC 2022"
    },
    "general": {
        "subjects": subjects,
        # "writing": writing,
    },
    "student_dataset": student_dataset
}

escrever_json('./output/data.json', data)

print("Arquivos gerados com sucesso!")












##########

{
    (1, 'Linguagens, códigos e suas tecnologias', '$'): [
                                                         ('Ademir Atanazio Junior', 1),
                                                         ('Agata Cristina Cidade', 1),
                                                         ('Ana Carolina de Andrade Machado', 1),
                                                         ('Ana Laura Teixeira Da Rosa', 1),
                                                         ('Byanka Lemos Veríssimo', 1),
                                                         ('Caroliny Alves Leal', 1),
                                                         ('Cecília Rost Hames', 1),
                                                         ('Echo Fabre Zimmermann', 1),
                                                         ('Emanuelli marques de souza', 1),
                                                         ('Gabriele Alban Gonçalves', 1),
                                                         ('Gabrielle Machado Bardança', 1),
                                                         ('Guilherme Cadona Da Silva', 1)
                                                        ],
    (2, 'Linguagens, códigos e suas tecnologias', '$'): [
                                                        ('Ademir Atanazio Junior', 2),
                                                        ('Agata Cristina Cidade', 2),
                                                        ('Ana Carolina de Andrade Machado', 2),
                                                        ('Ana Laura Teixeira Da Rosa', 2),
                                                        ('Byanka Lemos Veríssimo', 2),
                                                        ('Caroliny Alves Leal', 2),
                                                        ('Cecília Rost Hames', 2),
                                                        ('Echo Fabre Zimmermann', 2),
                                                        ('Emanuelli marques de souza', 2),
                                                        ('Gabriele Alban Gonçalves', 2),
                                                        ('Gabrielle Machado Bardança', 2),
                                                        ('Guilherme Cadona Da Silva', 2)
                                                        ]
}