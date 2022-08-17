# TODO: por questão de tempo, não fiz um bom if para verificar se o aluno fez ingles ou espanhol, vou arrumar melhor depois, talvez em um simuenem?

from dis import dis
from geradores.gerar_json_geral_disciplina import *
from auxilio.variaveis import areas_ufsc

def gerar_json_alunos(correcao, respostas, dados_alunos, gabarito):
    student_dataset = []
    for aluno in correcao:
        nome_aluno = aluno[0]
        nota_total = aluno[84] + aluno[89]
        cpf, msg_tutor  = pegar_cpf_e_msg_tutor(nome_aluno, dados_alunos)
        posicao = encontrar_posicao(correcao, nota_total)
        
        student_dataset.append(
            {
                "info": {
                    "name": nome_aluno,
                    "cpf": cpf,
                    "total": nota_total,
                    "position": posicao,
                    "msg": msg_tutor
                },
                "detailed": {
                    "subjects": gerar_details_aluno(aluno, gabarito, respostas),
                    "writing": {
                        "c1": {
                            "note": aluno[-11],
                            "comment": aluno[-6]
                        },
                        "c2": {
                            "note": aluno[-10],
                            "comment": aluno[-5]
                        },
                        "c3": {
                            "note": aluno[-9],
                            "comment": aluno[-4]
                        },
                        "c4": {
                            "note": aluno[-8],
                            "comment": aluno[-3]
                        },
                        "general_comment": aluno[-2],
                        "iframe": aluno[-1],
                        "total": aluno[-7]
                    }
                }
            }
        )
    return student_dataset

def gerar_details_aluno(aluno, gabarito, respostas):
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
                            "answered": [],
                            "detailed": []
                        }
                        continue
                    else:
                        continue

                details[chave_dicionario][disciplina] = {
                        "question_numbers": 0,
                        "general_percent": 0,
                        "answered": [],
                        "detailed": []
                    }

    details = gerar_anwsers_aluno(aluno, gabarito, details, respostas)
    details = calcular_general_porcent(details, aluno)
    return details

def gerar_anwsers_aluno(aluno, gabarito, details, respostas):
    for questao in gabarito:
        disciplina = questao[0]
        dia = questao[1]
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
                        details[area][disciplina]["detailed"].append(encontrar_resposta_aluno(respostas, aluno[0], numero_questao + 1, dia))
                        continue
                    else:
                        continue

        details[area][disciplina]["question_numbers"] += 1
        details[area][disciplina]["general_percent"] += pontuacoes
        details[area][disciplina]["answered"].append(resposta_aluno)
        details[area][disciplina]["detailed"].append(encontrar_resposta_aluno(respostas, aluno[0], numero_questao + 1, dia))
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

def encontrar_resposta_aluno(respostas, nome, numeroQuestao, dia):
    if dia == "d2":
        numeroQuestao = numeroQuestao - 42
    for resposta in respostas:
        if resposta[2] == nome and resposta[0] == dia and str(resposta[3]) == str(numeroQuestao):
            return resposta[4]

def encontrar_posicao(correcao, nota_total):
    todas_notas_totais = []
    for aluno in correcao:
        todas_notas_totais.append(aluno[84] + aluno[89])
        
    todas_notas_totais.sort(reverse=True)
    posicao = todas_notas_totais.index(nota_total) + 1
    return posicao