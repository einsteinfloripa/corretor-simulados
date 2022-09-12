from auxilio.variaveis import *

def gerar_json_disciplinas(correcao, gabarito, tipo_correcao):
    
    if (tipo_correcao == "simufsc"):
        subjects = gerar_estrutura_disciplinas_ufsc()
        subjects = gerar_detalhado_disciplina_estrutura_ufsc(subjects, correcao, gabarito)
        subjects = calcular_general_porcent_ufsc(subjects)
        return subjects
    
    if (tipo_correcao == "simuenem"):
        subjects = gerar_estrutura_disciplinas_enem()
        subjects = gerar_detalhado_disciplina_estrutura_enem(subjects, correcao, gabarito)
        subjects = calcular_general_porcent_enem(subjects)
        return subjects
    
    if (tipo_correcao == "simulinho"):
        print("Correção de simulinho não implementada")
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

def gerar_detalhado_disciplina_estrutura_enem(subjects, correcao, gabarito):
    for questao in gabarito:
        area = questao[0]
        disciplina = questao[-1]
        numero_questao = int(questao[2])
        resposta_gabarito = questao[3]
        pontuacoes = 0.

        for aluno in correcao:
            if aluno[numero_questao] != 0:
                pontuacoes += 1

            subjects[area][disciplina]["question_numbers"] += 1

        subjects[area][disciplina]["general_percent"] += pontuacoes
        subjects[area][disciplina]["detailed"].append(resposta_gabarito)
    return subjects


def calcular_general_porcent_ufsc(subjects):
    for area_ufsc in areas_ufsc:
        for chave_dicionario, disciplinas_area in area_ufsc.items():
            for disciplina in disciplinas_area:
                subjects[chave_dicionario][disciplina]["general_percent"] = subjects[chave_dicionario][disciplina]["general_percent"] / \
                    subjects[chave_dicionario][disciplina]["question_numbers"] * 100
    return subjects

def calcular_general_porcent_enem(subjects):
    for area_enem in areas_enem:
        for chave_dicionario, disciplinas_area in area_enem.items():
            for disciplina in disciplinas_area:
                subjects[chave_dicionario][disciplina]["general_percent"] = (subjects[chave_dicionario][disciplina]["general_percent"] / subjects[chave_dicionario][disciplina]["question_numbers"]) * 100
    return subjects