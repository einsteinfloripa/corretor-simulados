import csv, re

def formatar_dados(aplicacoes):
    dados = []
    for aplicacao in aplicacoes:
        with open(f"./input/{aplicacao}.csv", "r", encoding="utf-8") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            dados_aplicacao = [row for row in reader]

            del dados_aplicacao[0] #Excluir header

            for respostas in dados_aplicacao:
                respostas[5] = formatar_resposta(respostas[5])
                lingua = ""
                dia = aplicacao[0:2]

                respostaVazia = respostas[5] == None
                formulasd1 = dia == "d1" and re.sub(r'\s+', '', respostas[4]) == "22"
                formulasd2 = dia == "d2" and re.sub(r'\s+', '', respostas[4]) == "20"

                if respostaVazia or formulasd1 or formulasd2:
                    continue

                if dia == "d1":
                    lingua = aplicacao[3:4]


                dados.append([dia, lingua] + respostas[2:3] + respostas[4:6] + respostas[8:9])
    return dados



def formatar_resposta(resposta):
    resposta = re.sub(r'\s+', '', resposta)

    if resposta == "":
        #print("Resposta é nula")
        return None

    if "=" and "+" in resposta:
        resposta = extrair_da_soma(resposta)

    if not resposta.isdigit():
        #print(resposta + " não é um número")
        return f"ANULADA ('{resposta}' não é um número inteiro válido)"

    resposta = int(resposta)

    if resposta < 1 or resposta > 99:
        #print( str(resposta) + " é um número inválido")
        return f"ANULADA ('{resposta}' não um numero inteiro entre 1 e 99)"

    return resposta


def extrair_da_soma(resposta):
    print(resposta)
    return resposta.split("=")[1]