

def gerar_lista_resultado_alunos_ufsc(resultado_alunos, redacoes):
    lista_resultado_alunos = []

    for aluno, resultados in resultado_alunos.items():
        resultado_aluno = [aluno] + resultados
        pontuacao_total = calcula_pontuacao_total(resultado_aluno)
        resultado_aluno.append(pontuacao_total / 100)

        resultado_aluno = inserir_redacao(redacoes, aluno, resultado_aluno)

        lista_resultado_alunos.append(resultado_aluno)

    return lista_resultado_alunos

def gerar_lista_resultado_alunos_enem(resultado_alunos, redacoes):
    lista_resultado_alunos = []

    for nome_aluno, array_respostas_aluno in resultado_alunos.items():
        resultado_aluno = [nome_aluno] + array_respostas_aluno

        resultado_aluno = inserir_redacao(redacoes, nome_aluno, resultado_aluno)

        lista_resultado_alunos.append(resultado_aluno)

    return lista_resultado_alunos



def inserir_redacao(redacoes, aluno, resultado_aluno):
    for redacao in redacoes:
        if redacao[0] == aluno:
            for i in range(4, 14, 2):
                resultado_aluno.append(float(redacao[i].replace(",", ".")))
            for i in range(5, 15, 2):
                resultado_aluno.append(redacao[i])
            resultado_aluno.append(redacao[14])

    if len(resultado_aluno) == 85:
        #Aluno não fez a redação
        for i in range(4, 16):
            resultado_aluno.append(0)

    return resultado_aluno

def calcula_pontuacao_total(resultado_aluno):
    pontuacao_total  = 0
    for resultado in resultado_aluno:
        if isinstance(resultado, int):
            pontuacao_total += resultado
            resultado_aluno /= 100
    return pontuacao_total

def gera_base(lista_respostas):
    #Pega base de arrays de variaveis
    dados_alunos = {}
    resultado_alunos = {}

    for resposta_base in lista_respostas:
        nome_aluno = resposta_base[0]
        array_dividi_com_respostas_alunos = resposta_base[4:]

        dados_alunos[nome_aluno] = array_dividi_com_respostas_alunos
        resultado_alunos[nome_aluno] = [0] * len(array_dividi_com_respostas_alunos)

    return dados_alunos, resultado_alunos
