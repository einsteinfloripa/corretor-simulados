import csv
import json

aplicacoes = ["d1-e", "d1-i", "d2","d1-e-ae", "d1-i-ae", "d2-ae"]

def formatar_dados():
    dados = []
    for aplicacao in aplicacoes:
        with open(f"./input/{aplicacao}.csv", "r", encoding="utf-8") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            dados_aplicacao = [row for row in reader]

            del dados_aplicacao[0] #Excluir header

            for respostas in dados_aplicacao:
                dados.append(respostas[2:3] + respostas[4:6] + respostas[8:9])
    return dados



output = formatar_dados()

print(output)

with open("./output/output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)