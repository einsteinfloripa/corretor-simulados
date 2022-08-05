import csv
import json


def escrever_csv(caminho, dados):
    with open(caminho, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(dados)


def escrever_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
