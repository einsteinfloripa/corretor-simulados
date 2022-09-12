from auxilio.variaveis import *
from auxilio.somatorio import *

def gerar_lista_resultado_alunos_ufsc(resultado_alunos, redacoes):
    lista_resultado_alunos = []

    for aluno, resultados in resultado_alunos.items():
        resultado_aluno = [aluno] + resultados
        PT = calcula_PT(resultado_aluno)
        resultado_aluno.append(PT / 100)

        resultado_aluno = inserir_redacao(redacoes, aluno, resultado_aluno)

        lista_resultado_alunos.append(resultado_aluno)

    return lista_resultado_alunos

def gerar_lista_resultado_alunos_enem(resultado_alunos, redacoes):
    lista_resultado_alunos = []

    for aluno, resultados in resultado_alunos.items():
        resultado_aluno = [aluno] + resultados

        resultado_aluno = inserir_redacao(redacoes, aluno, resultado_aluno)

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

def calcula_PT(resultado_aluno):
    PT  = 0
    for i in range(len(resultado_aluno)):
        if isinstance(resultado_aluno[i], int):
            PT += resultado_aluno[i]
            resultado_aluno[i] /= 100
    return PT

def gera_base(lista_respostas):    
    #Pega base de arrays de variaveis
    dados_alunos = {}
    resultado_alunos = {}

    for resposta_base in lista_respostas:
        if resposta_base[2] not in dados_alunos:
            dados_alunos[resposta_base[2]] = [0] * total_questoes
            resultado_alunos[resposta_base[2]] = [0] * total_questoes

        if resposta_base[0] == "d1":
            dados_alunos[resposta_base[2]][total_questoes - 1] = resposta_base[1]
            resultado_alunos[resposta_base[2]][total_questoes - 1] = resposta_base[1]

    return dados_alunos, resultado_alunos

def separa_dia_de_prova(lista_respostas, dados_alunos):
    for resposta in lista_respostas:
        if resposta[0] == "d1":
            numero_questao = int(resposta[3])
            dados_alunos[resposta[2]][numero_questao - 1] = resposta[4]

        elif resposta[0] == "d2":
            numero_questao = int(resposta[3]) + max_questoes_por_dia
            dados_alunos[resposta[2]][numero_questao - 1] = resposta[4]

    return dados_alunos