import csv
import re


def formatar_respostas(aplicacoes, tipo_correcao):
    dados = []
    for aplicacao in aplicacoes:
        with open(f"./input/{aplicacao}.csv", "r", encoding="utf-8") as open_file:
            reader = csv.reader(open_file, delimiter=",", quotechar='"')
            dados_aplicacao = [row for row in reader]

            # for respostas in dados_aplicacao:
            #     if (tipo_correcao == "simufsc"):
            #         respostas[5] = valida_resposta_simufsc(respostas[5])
            #     if (tipo_correcao == "simuenem"):
            #         respostas[5] = valida_resposta_simenem(respostas[5])

            #     lingua = ""
            #     dia = aplicacao[0:2]

            #     respostaVazia = respostas[5] == None
            #     formulasd1 = dia == "d1" and re.sub(
            #         r'\s+', '', respostas[4]) == "22"
            #     formulasd2 = dia == "d2" and re.sub(
            #         r'\s+', '', respostas[4]) == "20"

            #     if respostaVazia or formulasd1 or formulasd2:
            #         continue

            #     if dia == "d1":
            #         lingua = aplicacao[3:4]
            #     dados.append([dia, lingua] + [respostas[2:3][0].strip()] +
            #                  respostas[4:6] + respostas[8:9])
    return dados_aplicacao


def valida_resposta_simufsc(resposta):
    resposta_formatada = re.sub(r'\s+', '', resposta)

    if resposta_formatada == "":
        #print("Resposta é nula")
        return None

    if "=" and "+" in resposta_formatada:
        resposta_formatada = extrair_da_soma(resposta_formatada)

    if not resposta_formatada.isdigit():
        #print(resposta + " não é um número")
        return f"ANULADA ('{resposta}' não é um número inteiro válido)"

    resposta_formatada = int(resposta_formatada)

    if resposta_formatada < 1 or resposta_formatada > 99:
        #print( str(resposta) + " é um número inválido")
        return f"ANULADA ('{resposta}' não um numero inteiro entre 1 e 99)"

    return resposta_formatada


def valida_resposta_simenem(resposta):
    resposta_formatada = re.sub(r'\s+', '', resposta)

    if resposta_formatada == "":
        #print("Resposta é nula")
        return None

    return resposta_formatada


def formatar_redacao(redacoes, dados_alunos):
    for redacao in redacoes:
        for aluno in dados_alunos:
            if aluno[1].replace("-", "").replace(".", "") == redacao[2]:
                redacao.insert(0, aluno[0])
    return redacoes


def extrair_da_soma(resposta):
    # print(resposta)
    return resposta.split("=")[1]
