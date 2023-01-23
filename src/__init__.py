from corrigir import corrigir
from geradores.gerar_json_aluno import gerar_json_alunos
from geradores.gerar_json_geral_disciplina import gerar_json_disciplinas
from leitura_e_escrita.escrever_arquivo import escrever_csv, escrever_json
from leitura_e_escrita.ler_arquivo import csvs_to_dfs
from GUI import Aplication


def main(dados):
    # Leitor de arquivos
    df_dados_alunos, df_respostas, df_gabarito = csvs_to_dfs(dados_alunos_path, respostas_alunos_path, gabarito_path)
    df_redacoes = []   # PLACE HOLDER Não implementado

    # Corrigir Provas
    df_resultado = corrigir(df_respostas, df_gabarito, df_redacoes, tipo_correcao)

    # escrever_csv("./output/respostas.csv", respostas)  ### Igual ao input...
    escrever_csv("./output/resultado.csv", df_resultado)
    escrever_csv("./output/gabarito.csv", df_gabarito)

    subjects = gerar_json_disciplinas(df_resultado, df_gabarito, tipo_correcao)
    # writing = gerar_json_redacao(correcao, len(redacoes))
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



app = Aplication()
app.window.set_corrigir_callback(main)
app.Run()






