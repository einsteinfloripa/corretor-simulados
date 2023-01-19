
def correcao_enem(gabarito, dados_alunos, resultado_alunos):
    for questao in gabarito:

        num_questao_para_index_array_gabarito = int(questao[1]) - 1
        resposta_questao_gabarito = questao[2]

        for nome_aluno, array_respostas_aluno in dados_alunos.items():
            if resposta_questao_gabarito == array_respostas_aluno[num_questao_para_index_array_gabarito]:
                resultado_alunos[nome_aluno][num_questao_para_index_array_gabarito] =  1
            else:
                resultado_alunos[nome_aluno][num_questao_para_index_array_gabarito] = 0

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
