import csv

def ler_csv(caminho):
    with open(caminho, "r", encoding="utf-8") as g:
        reader = csv.reader(g, delimiter=",", quotechar='"')
        dados = [row for row in reader]
    return dados
