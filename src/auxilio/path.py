import os


# Cria pasta relatorio(1) se existir cria relatorio(1) ...
def get_caminho_de_saida(dir_selecioado):

    cont = 0
    while True:
        path_saida = os.path.join(dir_selecioado, "output")
        if not os.path.exists(path_saida):
            os.makedirs(path_saida)
            break
        cont += cont

    if path_saida[-3:] == "(0)":
        path_saida.strip("(0)")

    return path_saida
    