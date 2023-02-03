import os

# Constatntes
# .../corretor-simulados
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


# adiciona relatorio ao caminho, se ja existir adiciona relatorio_1 ...
def get_caminho_de_saida(dir_selecionado):

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