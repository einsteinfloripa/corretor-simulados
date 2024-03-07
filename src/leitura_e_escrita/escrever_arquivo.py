import json
import os.path

def escrever_saida(caminho: str, extencao : str, dados : dict) -> None:
    if extencao == ".json":
        with open(os.path.join(caminho, "relatorio.json"), "w") as f:
            json.dump(dados, f)
    else:
        raise NotImplementedError(f"Saida {extencao} não implementada")
