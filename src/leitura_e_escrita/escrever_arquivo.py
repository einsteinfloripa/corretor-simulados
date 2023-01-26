import json
import os.path

def escrever_csv(caminho, data_frame):
    if not os.path.exists(os.path.dirname(caminho)):
        os.makedirs(os.path.dirname(caminho))

    data_frame.to_csv(caminho)


def escrever_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as open_file:
        json.dump(dados, open_file, ensure_ascii=False, indent=4)
