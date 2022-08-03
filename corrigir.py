from variaveis import *
from somatorio import *


def corrigir(lista_respostas, gabarito):
    dados_alunos = {}
    resultado_alunos = {}

    for resposta_base in lista_respostas:
        if resposta_base[2] not in dados_alunos:
            dados_alunos[resposta_base[2]] = lista_base_alunos.copy()
            resultado_alunos[resposta_base[2]] = lista_base_alunos.copy()
        if resposta_base[0] == "d1":
            dados_alunos[resposta_base[2]][82] = resposta_base[1]
            resultado_alunos[resposta_base[2]][82] = resposta_base[1]

    for resposta in lista_respostas:
        if resposta[0] == "d1":
            numero_questao = int(resposta[3])
            dados_alunos[resposta[2]][numero_questao-1] = resposta[4]
        elif resposta[0] == "d2":
            numero_questao = int(resposta[3]) + 42
            dados_alunos[resposta[2]][numero_questao-1] = resposta[4]

    for questao in gabarito:
        questao[2] = int(questao[2]) - 1
        if questao[1] == "d2" and not questao[3] == "ANULADA":
            questao[2] += 42
        for aluno, respostas in dados_alunos.items():
            if questao[1] == "d1" and questao[2] >= 14 and questao[2] <= 21:
                # Verifica se é a segunda lingua do aluno
                if not questao[0][0] == respostas[-1].upper():
                    continue

            if questao[3] == "ANULADA":
                # Questão foi anulada no gabarito
                resultado_alunos[aluno][questao[2]] = 100
                continue

            if "ANULADA" in str(dados_alunos[aluno][questao[2]]):
                # Aluno teve sua resposta anulada
                resultado_alunos[aluno][questao[2]] = str(
                    dados_alunos[aluno][int(questao[2])])
                continue

            if questao[4] == "ABERTA":
                # Questões abertas, só pontua se for a resposta for exatamente igual ao gabarito
                if questao[3] == dados_alunos[aluno][questao[2]]:
                    resultado_alunos[aluno][questao[2]] = 100
            else:
                # Aplica o método por somatorio
                resultado_alunos[aluno][questao[2]] = somatorio(
                    dados_alunos[aluno][questao[2]], int(questao[3]), int(questao[4]))

    lista_resultado_alunos = []
    for aluno, resultados in resultado_alunos.items():
        resultado_aluno = [aluno] + resultados
        PT = 0
        for i in range(len(resultado_aluno)):
            if isinstance(resultado_aluno[i], int):
                PT += resultado_aluno[i]
                resultado_aluno[i] /= 100
        resultado_aluno.append(PT / 100)
        lista_resultado_alunos.append(resultado_aluno)

    return lista_resultado_alunos
