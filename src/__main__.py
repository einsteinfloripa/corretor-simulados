
from corrigir import corrigir
from geradores.gerar_json_aluno import gerar_json_alunos
from geradores.gerar_json_geral_disciplina import gerar_json_disciplinas, gerar_estatisticas
from leitura_e_escrita.escrever_arquivo import escrever_csv, escrever_json
from leitura_e_escrita.ler_arquivo import csvs_to_dfs
from gui import Aplication
from auxilio.path import (get_caminho_de_saida, join_paths,
                          ROOT_PATH)
import pandas as pd

def main():

    # HARD CODED
    # dados_alunos_path = join_paths(ROOT_PATH, "recursos", "exemplos",
    #                               "simuenem", "alunos-dados.csv")

    # dados_alunos_path = dados["caminhos_dados"][0] # so um item por enquanto, por isso [0]
    # respostas_alunos_path = dados["caminhos_respostas"][0]
    # gabarito_path = dados["caminhos_gabaritos"][0]
    # tipo_correcao = dados["tipo_de_correcao"]
    # path_output_arquivos_correcao = get_caminho_de_saida(dados["caminho_de_saida"])

    ## TODO: Remover
    dados_alunos_path = "/home/matos/Einstein/Vale/corretor/corretor-simulados/src/TEMP/agora_vai/dados-alunos.csv"
    respostas_alunos_path = "/home/matos/Einstein/Vale/corretor/corretor-simulados/src/TEMP/agora_vai/respostas-alunos - respostas-alunos.csv"
    gabarito_path = "/home/matos/Einstein/Vale/corretor/corretor-simulados/src/TEMP/agora_vai/gabarito-oficial.csv"
    tipo_correcao = "simulinho"
    path_output_arquivos_correcao = "/home/matos/Einstein/Vale/corretor/corretor-simulados/src/TEMP/agora_vai"
    ##


    # _, df_respostas, df_gabarito = csvs_to_dfs(
    #     dados_alunos_path, respostas_alunos_path, gabarito_path,
    #     tipo_correcao = tipo_correcao
    # )

    ## TODO: Remover
    df_dados_alunos = pd.read_csv(dados_alunos_path, sep=",", quotechar='"', names=["Nome", "CPF"], encoding="utf-8")
    df_respostas = pd.read_csv(respostas_alunos_path)
    df_gabarito = pd.read_csv(gabarito_path, names=["Área", "Questão", "Gabarito", "Matéria"])
    ##

    df_redacoes = []  # PLACE HOLDER Não implementado


    ## TODO: Arrumar/Remover
    df_respostas_ = pd.merge(df_respostas, df_dados_alunos, left_on="CPF", right_on="CPF")

    # Corrigir Provas
    df_resultado = corrigir(df_respostas_, df_gabarito, df_redacoes, tipo_correcao)

    # escrever_csv("./output/respostas.csv", respostas)  ### Igual ao input...
    escrever_csv(join_paths(path_output_arquivos_correcao, "resultado.csv"), df_resultado)
    escrever_csv(join_paths(path_output_arquivos_correcao, "gabarito.csv"), df_gabarito)

    ## TODO: Remover
    # Temporario
    relatorio_temp = gerar_estatisticas(df_resultado, df_gabarito)
    df_relatorio = pd.DataFrame(relatorio_temp)
    escrever_csv("/home/matos/Einstein/Vale/corretor/corretor-simulados/src/TEMP/agora_vai/relatorio_questoes.xlsx", df_relatorio)
    #

    subjects = gerar_json_disciplinas(df_resultado, df_gabarito, tipo_correcao)
    # writing = gerar_json_redacao(correcao, len(redacoes))
    student_dataset = gerar_json_alunos(df_resultado, df_gabarito, tipo_correcao)

    data = {
        "config": {
            "role": 0,
            "type": 4,
            "version": "I 07/2022",
            "name": "SIMUFSC 2022",
        },
        "general": {
            "subjects": subjects,
            # "writing": writing,
        },
        "student_dataset": student_dataset,
    }

    escrever_json(join_paths(path_output_arquivos_correcao, "data.json"), data)

    # app.window.popup_botao_ok(
    #                           "Sucesso!",
    #                           "O relatório foi gerado com sucesso!",
    #                           pixmap_customizado=join_paths(
    #                               ROOT_PATH, 'recursos', 'imagens','sucesso.png'
    #                             )
    #                         )


if __name__ == '__main__':
    # app = Aplication()
    # app.window.set_corrigir_callback(main)
    # app.Run()
    main()