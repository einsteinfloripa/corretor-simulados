from pathlib import Path

import pandas as pd


def carregar_dados(caminho: str, tipo_prova: str) -> pd.DataFrame:
    # Checar se o caminho existe e é um diretório
    caminho = Path(caminho)
    if not caminho.exists():
        raise ValueError("O caminho fornecido não existe")
    if not caminho.is_dir():
        raise ValueError("O caminho fornecido não é um diretório")

    # Procurar os arquivos de dados
    tipo_arquivos = ["dados_alunos", "respostas", "gabarito"]
    exts = [".csv", ".json", ".xlsx"]

    caminhos = []
    for tipo_arquivo in tipo_arquivos:
        found = False
        for ext in exts:
            caminho_arquivo = caminho / f"{tipo_arquivo}{ext}"
            if caminho_arquivo.exists():
                caminhos.append((caminho_arquivo, ext, tipo_arquivo))
                found = True
                break
        if not found:
            raise ValueError(
                f'Arquivo "{tipo_arquivo}" não encontrado na pasta de entrada'
            )

    # Ler e checar os arquivos
    dados = {}
    for _caminho in caminhos:
        dados[_caminho[2]] = _carregar_dados(_caminho, tipo_prova)

    return dados


# Funções auxiliares
def _carregar_dados(dados_arquivo: tuple, tipo_prova: str) -> pd.DataFrame:
    if tipo_prova != "ps":
        raise NotImplementedError(f"Tipo de prova '{tipo_prova}' não implementado")

    mapa_extensao = {
        ".csv": _carrega_csv,
        ".json": _carrega_json,
        ".xlsx": _carrega_excel,
    }
    caminho, extensao, tipo_arquivo = dados_arquivo
    return mapa_extensao[extensao](caminho, tipo_arquivo)


# EXCEL
# args = (caminho, tipo_arquivo)
def _carrega_excel(*args : tuple[str, str]):
    dataframe = pd.read_excel(args[0], dtype=str)
    return dataframe


# CSV
# args = (caminho, tipo_arquivo)
def _carrega_csv(*args : tuple[str, str]):
    dataframe = pd.read_csv(args[0], dtype=str)
    return dataframe


# JSON
def _carrega_json(
    file_path: Path, tipo_arquivo: str):
    import json

    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    if tipo_arquivo == "respostas":
        try:
            data.pop("config")
        except KeyError:
            pass

        dados_formatados = list(data.values())

        df = pd.DataFrame.from_records(dados_formatados)

        return df

    raise NotImplementedError
