from src.corretores import corrigir
from src.geradores import gerar_relatorio
from src.leitura_e_escrita.ler_arquivo import carregar_dados
from src.auxilio.checker import check
from src.auxilio.path import get_caminho_de_saida, join_paths, ROOT_PATH
import src.gui as gui


def main(dados: dict, window):

    dir_de_entrada = dados["dir_entrada"]
    dir_saida = get_caminho_de_saida(dados["dir_saida"])
    tipo_correcao = dados["tipo_de_correcao"]

    # Carregar dados
    dados_de_entrada = carregar_dados(dir_de_entrada, tipo_correcao)

    # Checar se os dados são válidos
    check(dados_de_entrada, tipo_correcao)

    # Corrigir Provas
    df_resultado = corrigir(dados_de_entrada, tipo_correcao)

    # Gerar arquivo de estatisticas de correção e salvar
    gerar_relatorio(df_resultado, tipo_correcao, dir_saida)

    window.popup_botao_ok(
        "Sucesso!",
        "O relatório foi gerado com sucesso!",
        pixmap_customizado=join_paths(ROOT_PATH, "recursos", "imagens", "sucesso.png"),
    )


if __name__ == "__main__":
    app = gui.Application()
    app.window.set_corrigir_callback(main)
    app.Run()
