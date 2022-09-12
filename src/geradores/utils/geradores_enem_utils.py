from auxilio.variaveis import areas_enem 

def gerar_details_aluno_enem(aluno, gabarito, respostas):
    details = {}
    for area_enem in areas_enem:
        lingua_estrangeira_aluno = aluno[-1]
        for chave_dicionario, disciplinas_area in area_enem.items():
            details[chave_dicionario] = {}
            for disciplina in disciplinas_area:
                if verificar_lingua_estrangeira(lingua_estrangeira_aluno, disciplina):
                    continue

                details[chave_dicionario][disciplina] = {
                        "question_numbers": 0,
                        "general_percent": 0,
                        "answered": [],
                        "detailed": []
                    }

    details = gerar_anwsers_aluno_enem(aluno, gabarito, details, respostas)
    details = calcular_general_porcent(details, aluno)
    return details

def gerar_anwsers_aluno_enem(aluno, gabarito, details, respostas):
    for questao in gabarito:
        resposta_gabarito = questao[3]
        area = questao[0]
        num_questao = questao[2]
        disciplina = questao[-1]
        dia = questao[1]
        pontuacoes = 0.

        if dia == "d1":
            if verificar_lingua_estrangeira(aluno, questao[-1]):
                continue
        
        if aluno[num_questao] != 0:
            pontuacoes += 1.
            details[area][disciplina]["general_percent"] += pontuacoes

        details[area][disciplina]["question_numbers"] += 1
        details[area][disciplina]["answered"].append(aluno[num_questao])
        details[area][disciplina]["detailed"].append(resposta_gabarito) 

    return details

def calcular_general_porcent(details, aluno):
    lingua_estrangeira_aluno = aluno[-1]
    for area_enem in areas_enem:
        for chave_dicionario, disciplinas_area in area_enem.items():
            for disciplina in disciplinas_area:
                if verificar_lingua_estrangeira(lingua_estrangeira_aluno, disciplina):
                    continue

                if details[chave_dicionario][disciplina]["question_numbers"] != 0:
                    details[chave_dicionario][disciplina]["general_percent"] = round(details[chave_dicionario][disciplina]["general_percent"] / details[chave_dicionario][disciplina]["question_numbers"] * 100, 2)

    return details

def encontrar_resposta_aluno(respostas, nome, numeroQuestao, dia):
    if dia == "d2":
        numeroQuestao = numeroQuestao - 42
    for resposta in respostas:
        if resposta[2] == nome and resposta[0] == dia and str(resposta[3]) == str(numeroQuestao):
            return resposta[4]

def verificar_lingua_estrangeira(lingua_estrangeira_aluno, disciplina):
    if disciplina == "Inglês" or disciplina == "Espanhol":
        if lingua_estrangeira_aluno == disciplina[0].lower():
            return False
        else:
            return True
    return False
