from ast import For
from auxilio.variaveis import areas_enem 

def gerar_details_aluno_enem(aluno, gabarito, respostas):
    details = {}
    for area_enem in areas_enem:
        for chave_dicionario, disciplinas_area in area_enem.items():
            details[chave_dicionario] = {}
            for disciplina in disciplinas_area:
                eh_a_lingua_correta = False
                for resposta in respostas:
                    nome_aluno = resposta[0]
                    lingua_resposta = resposta[2]
                    if nome_aluno == aluno[0]:
                        if verificar_lingua_estrangeira(lingua_resposta, disciplina):
                            eh_a_lingua_correta = True
                if eh_a_lingua_correta:
                    continue

                details[chave_dicionario][disciplina] = {
                        "question_numbers": 0,
                        "general_percent": 0,
                        "answered": [],
                        "detailed": []
                    }

    details = gerar_anwsers_aluno_enem(aluno, gabarito, details, respostas)
    details = calcular_general_porcent(details, aluno,respostas)
    return details

def gerar_anwsers_aluno_enem(resultados_aluno, gabarito, details, respostas_alunos_detalhada):
    for questao in gabarito:
        print(questao)
        area = questao[0]
        num_questao = int(questao[1])
        resposta_gabarito = questao[2]
        disciplina = questao[-1]
        pontuacoes = 0.


        eh_a_lingua_correta = False
        for resposta in respostas_alunos_detalhada:
            nome_aluno = resposta[0]
            lingua_resposta = resposta[2]
            if nome_aluno == resultados_aluno[0]:
                if verificar_lingua_estrangeira(lingua_resposta, disciplina):
                    eh_a_lingua_correta = True
        if eh_a_lingua_correta:
            continue

        print(resultados_aluno)
        
        if resultados_aluno[num_questao] != 0:
            pontuacoes += 1.
            details[area][disciplina]["general_percent"] += pontuacoes

        details[area][disciplina]["question_numbers"] += 1
        details[area][disciplina]["answered"].append(resultados_aluno[num_questao])
        details[area][disciplina]["detailed"].append(resposta_gabarito) 

    return details

def calcular_general_porcent(details, resultados_aluno, respostas_alunos_detalhada):
    lingua_estrangeira_aluno = resultados_aluno[-1]
    for area_enem in areas_enem:
        for chave_dicionario, disciplinas_area in area_enem.items():
            for disciplina in disciplinas_area:
                eh_a_lingua_correta = False
                for resposta in respostas_alunos_detalhada:
                    nome_aluno = resposta[0]
                    lingua_resposta = resposta[2]
                    if nome_aluno == resultados_aluno[0]:
                        if verificar_lingua_estrangeira(lingua_resposta, disciplina):
                                eh_a_lingua_correta = True
                if eh_a_lingua_correta:
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
        if lingua_estrangeira_aluno.lower() == disciplina.lower():
            return False
        else:
            return True
    return False
