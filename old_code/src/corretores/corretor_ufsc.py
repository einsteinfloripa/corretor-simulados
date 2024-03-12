def correcao_ufsc(gabarito, dados_alunos, resultado_alunos):
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
    return dados_alunos, resultado_alunos
    