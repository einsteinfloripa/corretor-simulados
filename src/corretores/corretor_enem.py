from auxilio.variaveis import *
import pandas as pd
import numpy as np

def correcao_enem(df_respostas, df_gabarito):

    # 0 INGLES [0-4] + [10-184]
    df_gabarito_0 = df_gabarito.iloc[np.r_[:5, 10:185]]
    df_respostas_0 = df_respostas.loc[df_respostas["2Lingua"] == 0]
    df_respostas_0 = df_respostas_0.melt(id_vars=nome_col_df_respostas[0:4],
                                         var_name="Questão",
                                         value_name="Resposta",
                                         ignore_index = False)
    df_respostas_0["Questão"] = df_respostas_0["Questão"].astype(int)
    df_uniao_0 = pd.merge(df_respostas_0, df_gabarito_0, left_on = "Questão", right_on = "Questão").set_index(["Nome", "Questão"])
    df_uniao_0["Verificação"] = df_uniao_0.apply(lambda x: 1 if x["Gabarito"] in [x["Resposta"],"ANULADA"] else 0, axis = 1)

    # 1 ESPANHOL [5-184]
    df_gabarito_1 = df_gabarito.iloc[5:]
    df_respostas_1 = df_respostas.loc[df_respostas["2Lingua"] == 1]
    df_respostas_1 = df_respostas_1.melt(id_vars=nome_col_df_respostas[0:4], var_name="Questão", value_name="Resposta", ignore_index = False)
    df_respostas_1["Questão"] = df_respostas_1["Questão"].astype(int)
    df_uniao_1 = pd.merge(df_respostas_1, df_gabarito_1, left_on = "Questão", right_on = "Questão").set_index(["Nome", "Questão"])
    df_uniao_1["Verificação"] = df_uniao_1.apply(lambda x: 1 if x["Gabarito"] in [x["Resposta"],"ANULADA"] else 0, axis = 1)

    df_resultados = pd.concat([df_uniao_0, df_uniao_1])
    df_resultados.sort_index(inplace=True)

    return df_resultados






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
