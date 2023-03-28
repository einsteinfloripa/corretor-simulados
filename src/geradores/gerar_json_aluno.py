import re
from geradores.utils.geradores_enem_utils import gerar_details_aluno_enem, gerar_details_aluno_simulinho
import pandas as pd
from leitura_e_escrita.escrever_arquivo import escrever_csv

def gerar_json_alunos(df_resultado, df_gabarito, tipo_correcao):

    if tipo_correcao == "simufsc":
        print("Simulado UFSC não implementado ainda")
        # return gerar_json_simufsc(correcao, respostas, dados_alunos, gabarito)
    if tipo_correcao == "simuenem":
        return gerar_json_simuenem(df_resultado, df_gabarito)
    if tipo_correcao == "simulinho":
        return gerar_json_simulinho(df_resultado, df_gabarito)


def gerar_json_simuenem(df_resultado, df_gabarito):
    student_dataset = []
    lista_total = []
    nomes_lista = df_resultado.index.get_level_values("Nome").unique()

    for nome in nomes_lista:
        total = df_resultado.loc[df_resultado.index.get_level_values(
            "Nome") == nome, "Verificação"].sum()
        lista_total.append([nome, total])
    lista_total_ordenada = [x for x in sorted(lista_total, key=lambda x: x[1])]
    lista_total_ordenada.reverse()

    grupos = df_resultado.groupby("Nome", sort=False)
    for nome, grupo in grupos:
        nome_aluno = nome
        total_acertos = grupo["Verificação"].eq(1).sum()
        cpf = re.sub("\\D", "", grupo.loc[nome, "CPF"].iat[0])
        msg_tutor = grupo.loc[nome, "2Lingua"].iat[0]
        posicao = next(lista_total_ordenada.index(listas)
                       for listas in lista_total_ordenada if listas[0] == nome)

        student_dataset.append(
            {
                "info": {
                    "name": nome_aluno,
                    "cpf": cpf,
                    "total": str(total_acertos),
                    "position": str(posicao+1),
                    "msg": msg_tutor
                },
                "detailed": {
                    "subjects": gerar_details_aluno_enem(nome_aluno, df_gabarito, df_resultado),
                }
            }
        )

    return student_dataset


def gerar_json_simufsc(correcao, respostas, dados_alunos, gabarito):

    for aluno in correcao:
        print(aluno)
        nome_aluno = aluno[0]
        nota_total = aluno[84] + aluno[89]
        cpf, msg_tutor = pegar_cpf_e_msg_tutor(nome_aluno, dados_alunos)
        # posicao = encontrar_posicao(correcao, nota_total)

        nota_total = "1"
        posicao = 1

        return (
            {
                "info": {
                    "name": nome_aluno,
                    "cpf": cpf,
                    "total": nota_total,
                    "position": posicao,
                    "msg": msg_tutor
                },
                "detailed": {
                    "subjects": []
                    # "subjects": gerar_details_aluno(aluno, gabarito, respostas),
                    # "writing": {
                    #     "c1": {
                    #         "note": aluno[-11],
                    #         "comment": aluno[-6]
                    #     },
                    #     "c2": {
                    #         "note": aluno[-10],
                    #         "comment": aluno[-5]
                    #     },
                    #     "c3": {
                    #         "note": aluno[-9],
                    #         "comment": aluno[-4]
                    #     },
                    #     "c4": {
                    #         "note": aluno[-8],
                    #         "comment": aluno[-3]
                    #     },
                    #     "general_comment": aluno[-2],
                    #     "iframe": aluno[-1],
                    #     "total": aluno[-7]
                    # }
                }
            }
        )

# TODO: Arrumar CPF simulinho
def gerar_json_simulinho(df_resultado, df_gabarito):
    student_dataset = []
    lista_total = []

    # TODO: Remover
    lista_posicao = []
    dicionario_final = {}
    #

    nomes_lista = df_resultado.index.get_level_values("Nome").unique()

    for nome in nomes_lista:
        total = df_resultado.loc[df_resultado.index.get_level_values(
            "Nome") == nome, "Verificação"].sum()
        lista_total.append([nome, total])
    lista_total_ordenada = [x for x in sorted(lista_total, key=lambda x: x[1])]
    lista_total_ordenada.reverse()

    grupos = df_resultado.groupby("Nome", sort=False)
    for nome, grupo in grupos:
        nome_aluno = nome
        total_acertos = grupo["Verificação"].eq(1).sum()
        # TODO: Arrumar CPF depois que tiver formato final dos inputs
        # cpf = re.sub("\\D", "", grupo.loc[nome, "CPF"].iat[0])
        # TODO: A princípio não tem 2Lingua
        # msg_tutor = grupo.loc[nome, "2Lingua"].iat[0]
        posicao = next(lista_total_ordenada.index(listas)
                       for listas in lista_total_ordenada if listas[0] == nome)

        student_dataset.append(
            {
                "info": {
                    "name": nome_aluno,
                    "cpf": "PLACE-HOLDER",
                    "total": str(total_acertos),
                    "position": str(posicao+1),
                   #"msg": msg_tutor
                },
                "detailed": {
                    "subjects": gerar_details_aluno_simulinho(nome_aluno, df_gabarito, df_resultado),
                }
            }
        )
#region
# TODO: Remover - TEMPORARIO
        dicionario_final[nome_aluno] = {}
        dicionario_final[nome_aluno]["Nota"] = str(total_acertos)
        dicionario_final[nome_aluno]["Posição"] = posicao+1
        lista_posicao.append((nome_aluno, posicao+1))

    lista_posicao = sorted(lista_posicao, key = lambda x: x[1])
    df_final = pd.DataFrame(dicionario_final)
    df_final = df_final.transpose()
    print(lista_posicao)
    print(df_final)
    escrever_csv("/home/matos/Einstein/Vale/corretor/corretor-simulados/src/TEMP/agora_vai/resultado_final.xlsx", df_final)
#endregion
    return student_dataset




# TODO: Verificar/Remover essas funções abaixo
def pegar_cpf_e_msg_tutor(nome_aluno, dados_alunos):
    cpf = ""
    msg_tutor = ""
    nome_formatado = nome_aluno.lower()
    for aluno in dados_alunos:
        if nome_formatado in aluno[0].lower():
            cpf = aluno[1].replace("-", "").replace(".", "")
            if len(aluno) >= 3:
                msg_tutor = aluno[2]
            break
    return cpf, msg_tutor


def encontrar_posicao(correcao, nota_total):
    todas_notas_totais = []
    for aluno in correcao:
        todas_notas_totais.append(calcular_total_acertos(aluno))

    todas_notas_totais.sort(reverse = True)
    posicao = todas_notas_totais.index(nota_total) + 1
    return posicao


def calcular_total_acertos(aluno):
    acertos = 0
    for questao in aluno:
        if questao != 0:
            acertos += 1

    return acertos
