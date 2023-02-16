import pandas as pd
import numpy as np
from auxilio.variaveis import (codigo_2lingua_dicionario as c2l,
                               nome_col_df_respostas_enem as ncenem,
                               nome_col_df_respostas_simulinho as ncsimulinho)


def correcao_simulinho(df_respostas, df_gabarito, tipo_correcao):

    lista_dfs_2lingua = get_pares_dfs_2lingua(df_respostas, df_gabarito, tipo_correcao)
    lista_dfs_modelados = modela_df_respostas(lista_dfs_2lingua, tipo_correcao)
    lista_dfs_modelados = add_verificacao(lista_dfs_modelados)

    df_resultados = pd.concat(lista_dfs_modelados)
    df_resultados.sort_index(inplace=True)

    return df_resultados


def correcao_enem(df_respostas, df_gabarito, tipo_correcao):

    lista_dfs_2lingua = get_pares_dfs_2lingua(df_respostas, df_gabarito, tipo_correcao)
    lista_dfs_modelados = modela_df_respostas(lista_dfs_2lingua, tipo_correcao)
    lista_dfs_modelados = add_verificacao(lista_dfs_modelados)

    df_resultados = pd.concat(lista_dfs_modelados)
    df_resultados.sort_index(inplace=True)

    return df_resultados


def correcao_ufsc():
    pass


# Auxilio TODO: Talvez mover para arquivo externo?
def get_pares_dfs_2lingua(df_respostas, df_gabarito, tc):

    dfs = []

    if tc == "simufsc":
        print("Ainda não implementado SIMUFSC")

    if tc == "simuenem":
        linguas_dici = list(c2l["2Lingua"].items())[:-1]
        ultima_questao = np.max([tupla[1]["Posição"] for tupla in linguas_dici])

        for lingua, dici2 in linguas_dici:
            df_resposta_ = df_respostas.loc[df_respostas["2Lingua"].astype(
                str) == lingua]
            df_gabarito_ = df_gabarito.iloc[
                    np.r_[
                        slice(dici2["Posição"][0], dici2["Posição"][1]),
                        slice(ultima_questao, len(df_gabarito.index))
                    ]
                ]
            dfs.extend([df_resposta_, df_gabarito_])

    if tc == "simulinho":
        dfs.extend([df_respostas, df_gabarito])
        #print(dfs[0],dfs[1])
    return dfs


def modela_df_respostas(dfs_2lingua, tc):
    dfs = []

    # TODO: Adicionar para o caso simufsc
    col_nomes = (tc == "simuenem" and ncenem) or (tc == "simulinho" and ncsimulinho )
    range_ = (tc == "simuenem" and col_nomes[0:4]) or (tc == "simulinho" and col_nomes[0:2])

    for i in range(0, len(dfs_2lingua), 2):
        df_resposta_modelado = dfs_2lingua[i].melt(id_vars=range_,
                                                   var_name="Questão",
                                                   value_name="Resposta",
                                                   ignore_index=False)

        dfs_2lingua[i] = df_resposta_modelado
        dfs_2lingua[i]["Questão"] = dfs_2lingua[i]["Questão"].astype(int)
        df_uniao_ = pd.merge(dfs_2lingua[i], dfs_2lingua[i+1], left_on="Questão",
                             right_on="Questão").set_index(["Nome", "Questão"])
        dfs.append(df_uniao_)

    return dfs


def add_verificacao(lista_dfs_modelados):
    for data_frame in lista_dfs_modelados:
        data_frame["Verificação"] = data_frame.apply(
            lambda x: 1 if x["Gabarito"] in [x["Resposta"], "ANULADA"] else 0, axis=1
        )

    return lista_dfs_modelados