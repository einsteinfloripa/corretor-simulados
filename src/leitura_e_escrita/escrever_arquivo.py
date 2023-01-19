import csv
import json
import os.path

def escrever_csv(caminho, dados):
    if not os.path.exists(os.path.dirname(caminho)):
        os.makedirs(os.path.dirname(caminho))
    
    with open(caminho, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(dados)


def escrever_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
