import json
import os.path

def escrever_saida(caminho: str, extencao:str, dados):
    if extencao == ".json":
        with open(os.path.join(caminho, "saida.json"), "w") as f:
            json.dump(dados, f)
    else:
        raise NotImplementedError(f"Saida {extencao} não implementada")
