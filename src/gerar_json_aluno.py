# TODO: por questão de tempo, não fiz um bom if para verificar se o aluno fez ingles ou espanhol, vou arrumar melhor depois, talvez em um simuenem?

from dis import dis
from gerar_json_disciplina import *
from variaveis import areas_ufsc

def gerar_json_alunos(correcao, dados_alunos, gabarito):
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
                "details": gerar_details_aluno(aluno, gabarito)  
                # TODO: Incluir redação no detalhado
                # TODO: Incluir msg do tutor
            }
        )
    return students_dataset

def gerar_details_aluno(aluno, gabarito):
    details = {}
    for area_ufsc in areas_ufsc:
        lingua_estrangeira_aluno = aluno[83]
        for chave_dicionario, disciplinas_area in area_ufsc.items():
            details[chave_dicionario] = {}
            for disciplina in disciplinas_area:
                # TODO: mudar esse if depois tá muito feito
                if disciplina == "Inglês" or disciplina == "Espanhol":
                    if lingua_estrangeira_aluno == disciplina[0].lower():
                        details[chave_dicionario][disciplina] = {
                            "question_numbers": 0,
                            "general_percent": 0,
                            "answered": []
                        }
                        continue
                    else:
                        continue

                details[chave_dicionario][disciplina] = {
                        "question_numbers": 0,
                        "general_percent": 0,
                        "answered": []
                    }

    details = gerar_anwsers_aluno(aluno, gabarito, details)
    details = calcular_general_porcent(details, aluno)
    return details

def gerar_anwsers_aluno(aluno, gabarito, details):
    for questao in gabarito:
        disciplina = questao[0]
        numero_questao = questao[2]
        resposta_aluno = aluno[numero_questao + 1]
        area = questao[5]
        pontuacoes = 0.
        lingua_estrangeira_aluno = aluno[83]
        if "ANULADA" not in str(aluno[numero_questao + 1]):
            pontuacoes += aluno[numero_questao + 1]
        # TODO: mudar esse if depois tá muito feito
        if disciplina == "Inglês" or disciplina == "Espanhol":
                    if lingua_estrangeira_aluno == disciplina[0].lower():
                        details[area][disciplina]["question_numbers"] += 1
                        details[area][disciplina]["general_percent"] += pontuacoes
                        details[area][disciplina]["answered"].append(resposta_aluno)
                        continue
                    else:
                        continue

        details[area][disciplina]["question_numbers"] += 1
        details[area][disciplina]["general_percent"] += pontuacoes
        details[area][disciplina]["answered"].append(resposta_aluno)
    return details

def calcular_general_porcent(details, aluno):
    lingua_estrangeira_aluno = aluno[83]
    for area_ufsc in areas_ufsc:
        for chave_dicionario, disciplinas_area in area_ufsc.items():
            for disciplina in disciplinas_area:
                # TODO: mudar esse if depois tá muito feito
                if disciplina == "Inglês" or disciplina == "Espanhol":
                    if lingua_estrangeira_aluno == disciplina[0].lower():
                        details[chave_dicionario][disciplina]["general_percent"] = round(details[chave_dicionario][disciplina]["general_percent"] / \
                    details[chave_dicionario][disciplina]["question_numbers"] * 100, 2)
                        continue
                    else:
                        continue

                details[chave_dicionario][disciplina]["general_percent"] = round(details[chave_dicionario][disciplina]["general_percent"] / \
                    details[chave_dicionario][disciplina]["question_numbers"] * 100, 2)
    return details

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