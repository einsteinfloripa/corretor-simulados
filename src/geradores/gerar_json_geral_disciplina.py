from auxilio.variaveis import codigo_2lingua_dicionario as c2l
from auxilio.variaveis import *
from leitura_e_escrita.escrever_arquivo import *

def gerar_json_disciplinas(df_resultado, df_gabarito, tipo_correcao):

    if (tipo_correcao == "simufsc"):
        print("Atenção: Correção de simulado ufsc não implementado")
        return {}
        # subjects = gerar_estrutura_disciplinas_ufsc()
        # subjects = gerar_detalhado_disciplina_estrutura_ufsc(subjects, correcao, gabarito)
        # subjects = calcular_general_porcent_ufsc(subjects)
        # return subjects

    if (tipo_correcao == "simuenem"):
        subjects = gerar_estrutura_disciplinas_enem()
        subjects = gerar_detalhado_disciplina_estrutura_enem(subjects, df_resultado, df_gabarito)
        #subjects = calcular_general_porcent_enem(subjects)
        return subjects

    if (tipo_correcao == "simulinho"):
        print("Atenção: Correção de simulinho não implementada")
        return {}

def gerar_estrutura_disciplinas_ufsc():
    estrutura = {}
    for area_ufsc in areas_ufsc:
        for chave_dicionario, disciplinas_area in area_ufsc.items():
            estrutura[chave_dicionario] = {}
            for disciplina in disciplinas_area:
                estrutura[chave_dicionario][disciplina] = {
                    "question_numbers": 0,
                    "general_percent": 0,
                    "detailed": [],
                    # "theme": [],
                    # "level": []
                }
    return estrutura

def gerar_estrutura_disciplinas_enem():
    estrutura = {}
    for area_enem in areas_enem:
        for chave_dicionario, disciplinas_area in area_enem.items():
            estrutura[chave_dicionario] = {}
            for disciplina in disciplinas_area:
                estrutura[chave_dicionario][disciplina] = {
                    "question_numbers": 0,
                    "general_percent": 0,
                    "detailed": [],
                    # "theme": [],
                    # "level": []
                }
    return estrutura

def gerar_detalhado_disciplina_estrutura_ufsc(subjects, correcao, gabarito):
    for questao in gabarito:
        disciplina = questao[0]
        numero_questao = questao[2]
        resposta_gabarito = questao[3]
        area = questao[5]
        pontuacoes = 0.
        for aluno in correcao:
            if "ANULADA" not in str(aluno[numero_questao + 1]):
                pontuacoes += aluno[numero_questao + 1]
            subjects[area][disciplina]["question_numbers"] += 1
        subjects[area][disciplina]["general_percent"] += pontuacoes
        subjects[area][disciplina]["detailed"].append(resposta_gabarito)
    return subjects

def gerar_detalhado_disciplina_estrutura_enem(subjects, df_resultado, df_gabarito):
    grupos = df_resultado.groupby(["Área", "Matéria"], sort=False)
    for nome, grupo in grupos:
        if nome[0] == str([*areas_enem[0]][0]):
            subjects[nome[0]][nome[1]]["question_numbers"] = len(grupo) + c2l["2Lingua"]["Quantidade"]*df_resultado["CPF"].nunique()
            subjects[nome[0]][nome[1]]["general_percent"] = round(grupo["Verificação"].eq(1).sum() * 100 / \
            subjects[nome[0]][nome[1]]["question_numbers"], 2)
        else:
            subjects[nome[0]][nome[1]]["question_numbers"] = len(grupo)
            subjects[nome[0]][nome[1]]["general_percent"] = round((grupo["Verificação"].eq(1).sum() * 100) / \
            subjects[nome[0]][nome[1]]["question_numbers"], 2)

        serie_temp_ = df_gabarito.loc[(df_gabarito["Área"] == nome[0]) & (df_gabarito["Matéria"] == nome[1]), "Gabarito"]
        subjects[nome[0]][nome[1]]["detailed"] = list(serie_temp_)
    return subjects


def calcular_general_porcent_ufsc(subjects):
    for area_ufsc in areas_ufsc:
        for chave_dicionario, disciplinas_area in area_ufsc.items():
            for disciplina in disciplinas_area:
                subjects[chave_dicionario][disciplina]["general_percent"] = round(subjects[chave_dicionario][disciplina]["general_percent"] / \
                    subjects[chave_dicionario][disciplina]["question_numbers"] * 100, 2)
    return subjects

def calcular_general_porcent_enem(subjects):
    for area_enem in areas_enem:
        for chave_dicionario, disciplinas_area in area_enem.items():
            for disciplina in disciplinas_area:
                if subjects[chave_dicionario][disciplina]["general_percent"] != 0:
                    subjects[chave_dicionario][disciplina]["general_percent"] = round(subjects[chave_dicionario][disciplina]["general_percent"] / \
                    subjects[chave_dicionario][disciplina]["question_numbers"] * 100, 2)

    return subjects