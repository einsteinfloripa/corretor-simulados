import os

# Constatntes
# .../corretor-simulados
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


# adiciona relatorio ao caminho, se ja existir adiciona relatorio_1 ...
def get_caminho_de_saida(dir_selecioado):

    cont = 0
    while True:
        path_saida = os.path.join(dir_selecioado, f"output_{cont}")

        if path_saida[-2:] == "_0":
            path_saida = path_saida.strip("_0")

        if not os.path.exists(path_saida):
            break
        cont += 1

    return path_saida


def join_paths(*args):
    return os.path.join(*args)
