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
    for lingua, dici2 in list(c2l["2Lingua"].items())[:-1]:
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