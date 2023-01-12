from auxilio.variaveis import *
from auxilio.variaveis import codigo_2lingua_dicionario as c2l
import pandas as pd
import numpy as np



def correcao_enem(df_respostas, df_gabarito):
    # [resposta_1, gabarito_1, resposta_2, gabarito_2]
    lista_dfs_2lingua = get_pares_dfs_2lingua(df_respostas, df_gabarito)
    # [df_1, df_2]
    lista_dfs_modelados = modela_df_respostas(lista_dfs_2lingua)
    for df in lista_dfs_modelados:
        df["Verificação"] = df.apply(lambda x: 1 if x["Gabarito"] in [x["Resposta"],"ANULADA"] else 0, axis = 1)

    df_resultados = pd.concat(lista_dfs_modelados)
    df_resultados.sort_index(inplace=True)

    return df_resultados





def get_pares_dfs_2lingua(df_respostas, df_gabarito):
    dfs = []
    for lingua, dici2 in c2l["2Lingua"].items():
        df_resposta_ = df_respostas.loc[df_respostas["2Lingua"].astype(str) == lingua]
        df_gabarito_ = df_gabarito.iloc[np.r_[dici2["Posição"][0], dici2["Posição"][1]]]
        dfs.extend([df_resposta_, df_gabarito_])

    return dfs


def modela_df_respostas(dfs_2lingua):
    dfs = []
    for i in range(0, len(dfs_2lingua), 2):
        df_resposta_modelado = dfs_2lingua[i].melt(id_vars=nome_col_df_respostas[0:4],
                                                   var_name="Questão",
                                                   value_name="Resposta",
                                                   ignore_index = False)

        dfs_2lingua[i] = df_resposta_modelado
        dfs_2lingua[i]["Questão"] = dfs_2lingua[i]["Questão"].astype(int)
        df_uniao_ = pd.merge(dfs_2lingua[i], dfs_2lingua[i+1], left_on = "Questão", right_on = "Questão").set_index(["Nome", "Questão"])
        dfs.append(df_uniao_)

    return dfs






####### Antigo #####
## 0 INGLES [0-4] + [10-184]
    # df_gabarito_0 = df_gabarito.iloc[np.r_[:5, 10:]]
    # df_respostas_0 = df_respostas.loc[df_respostas["2Lingua"] == 0]
    # df_respostas_0 = df_respostas_0.melt(id_vars=nome_col_df_respostas[0:4],
    #                                      var_name="Questão",
    #                                      value_name="Resposta",
    #                                      ignore_index = False)
    # df_respostas_0["Questão"] = df_respostas_0["Questão"].astype(int)
    # df_uniao_0 = pd.merge(df_respostas_0, df_gabarito_0, left_on = "Questão", right_on = "Questão").set_index(["Nome", "Questão"])
    # df_uniao_0["Verificação"] = df_uniao_0.apply(lambda x: 1 if x["Gabarito"] in [x["Resposta"],"ANULADA"] else 0, axis = 1)

## 1 ESPANHOL [5-184]
    # df_gabarito_1 = df_gabarito.iloc[5:]
    # df_respostas_1 = df_respostas.loc[df_respostas["2Lingua"] == 1]
    # df_respostas_1 = df_respostas_1.melt(id_vars=nome_col_df_respostas[0:4],
    #                                      var_name="Questão",
    #                                      value_name="Resposta",
    #                                      ignore_index = False)
    # df_respostas_1["Questão"] = df_respostas_1["Questão"].astype(int)
    # df_uniao_1 = pd.merge(df_respostas_1, df_gabarito_1, left_on = "Questão", right_on = "Questão").set_index(["Nome", "Questão"])
    # df_uniao_1["Verificação"] = df_uniao_1.apply(lambda x: 1 if x["Gabarito"] in [x["Resposta"],"ANULADA"] else 0, axis = 1)

    # return df_resultados






################## ANTIGO ################
def correcao_enem_OLD(gabarito, dados_alunos, resultado_alunos):
    for questao in gabarito:

        num_questao_para_index_array_gabarito = int(questao[1]) - 1
        resposta_questao_gabarito = questao[2]

        for nome_aluno, array_respostas_aluno in dados_alunos.items():
            if resposta_questao_gabarito == array_respostas_aluno[num_questao_para_index_array_gabarito]:
                resultado_alunos[nome_aluno][num_questao_para_index_array_gabarito] =  1
            else:
                resultado_alunos[nome_aluno][num_questao_para_index_array_gabarito] = 0

    return dados_alunos, resultado_alunos

def verificar_lingua_extrangeira(respostas, lingua):
    if lingua == "Inglês" or lingua == "Espanhol":
        if lingua[0].lower() == respostas[-1]:
            return True
    return False

def verificar_gabarito(respostas, gabarito):
    if respostas[gabarito[2]].lower() == gabarito[3].lower():
        return True
    return False

def resposta_aluno_vazia(resposta):
    if resposta == 0:
        return True
    return False
