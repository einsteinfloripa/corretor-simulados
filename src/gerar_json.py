from cryptography.fernet import Fernet
from variaveis import *

def gerar_json_disciplinas(correcao, gabarito):
    subjects = gerar_estrutura_disciplinas()
    subjects = gerar_detalhado_disciplina_estrutura(
        subjects, correcao, gabarito)
    subjects = calcular_general_porcent(subjects)

    return subjects


def gerar_json_alunos(correcao, dados_alunos):
    students_dataset = []
    for aluno in correcao:
        nome_aluno = aluno[0]
        nota_total = aluno[84]
        cpf = pegar_cpf(nome_aluno, dados_alunos)
        posicao = encontrar_posicao(correcao, nota_total)
        students_dataset.append(
            {
                "info": {
                    "name": nome_aluno,
                    "cpf": cpf,
                    "total": nota_total,
                    "position": posicao 
                },
                "details": [] # TODO: adicionar detalhes
                # TODO: Incluir redação no detalhado
                # TODO: Incluir msg do tutor
            }
        )

    return students_dataset


def gerar_estrutura_disciplinas():
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



def gerar_detalhado_disciplina_estrutura(subjects, correcao, gabarito):
    for questao in gabarito:
        disciplina = questao[0]
        # aplicacao = questao[1]
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


def calcular_general_porcent(subjects):
    for area_ufsc in areas_ufsc:
        for chave_dicionario, disciplinas_area in area_ufsc.items():
            for disciplina in disciplinas_area:
                subjects[chave_dicionario][disciplina]["general_percent"] = subjects[chave_dicionario][disciplina]["general_percent"] / \
                    subjects[chave_dicionario][disciplina]["question_numbers"] * 100
    return subjects

def pegar_cpf(nome_aluno, dados_alunos):
    cpf = ""
    nome_formatado = nome_aluno.lower()
    for aluno in dados_alunos:
        if nome_formatado in aluno[0].lower():
            cpf = aluno[1]
            break
    return cpf 

def encontrar_posicao(correcao, nota_total):
    todas_notas_totais = []
    for aluno in correcao:
        todas_notas_totais.append(aluno[84])
        
    todas_notas_totais.sort(reverse=True)
    posicao = todas_notas_totais.index(nota_total) + 1
    return posicao