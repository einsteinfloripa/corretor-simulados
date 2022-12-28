import json
import os.path
import pandas as pd

def escrever_csv(caminho, df):
    if not os.path.exists(os.path.dirname(caminho)):
        os.makedirs(os.path.dirname(caminho))

    df.to_csv(caminho)


def escrever_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
