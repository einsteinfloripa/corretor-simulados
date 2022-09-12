
def correcao_enem(gabarito, dados_alunos, resultado_alunos):
    for questao in gabarito:
        questao[2] = int(questao[2]) - 1
        questao[3] = questao[3].lower()

        for aluno, respostas in dados_alunos.items():
            if questao[1] == "d1":
                if resposta_aluno_vazia(respostas[questao[2]]):
                    continue

                if verificar_lingua_extrangeira(respostas, questao[4]):
                    if verificar_gabarito(respostas, questao):
                        resultado_alunos[aluno][questao[2]] = questao[3]
                    else:
                        resultado_alunos[aluno][questao[2]] = 0

                elif verificar_gabarito(respostas, questao):
                    resultado_alunos[aluno][questao[2]] = questao[3]

                else:
                    continue

            if questao[1] == "d2":
                if resposta_aluno_vazia(respostas[questao[2]]):
                    continue

                elif verificar_gabarito(respostas, questao):
                    resultado_alunos[aluno][questao[2]] = questao[3]

                else:
                    continue

    return dados_alunos, resultado_alunos

def verificar_lingua_extrangeira(respostas, lingua):
    if lingua == "Inglês" or lingua == "Espanhol":
        if lingua[0].lower() == respostas[-1]:
            return True
    return False

def verificar_gabarito(respostas, gabarito):
    if respostas[gabarito[2]].lower() == gabarito[3].lower():
        return True
    return False

def resposta_aluno_vazia(resposta):
    if resposta == 0:
        return True
    return False
