import os
import sys
from pathlib import Path


# Constatntes
# .../corretor-simulados
def get_root_path() -> str:

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return str(Path(sys._MEIPASS).resolve())

    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


ROOT_PATH = get_root_path()


# adiciona relatorio ao caminho, se ja existir adiciona relatorio_1 ...
def get_caminho_de_saida(dir_selecionado: str) -> str:

    cont = 0
    while True:
        path_output_arquivos_correcao = os.path.join(dir_selecionado, f"output_{cont}")

        if path_output_arquivos_correcao[-2:] == "_0":
            path_output_arquivos_correcao = path_output_arquivos_correcao.strip("_0")

        if not os.path.exists(path_output_arquivos_correcao):
            break
        cont += 1

    return path_output_arquivos_correcao


def join_paths(*args):
    return os.path.join(*args)

def mkdir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

def rmdir(path: str):
    if os.path.exists(path):
        os.removedirs(path)
    