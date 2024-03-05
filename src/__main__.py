from corretores import corrigir
from geradores import gerar_relatório
from leitura_e_escrita.ler_arquivo import carregar_dados
from gui import Aplication
from auxilio.path import (get_caminho_de_saida, join_paths,
                          ROOT_PATH)


def main(dados: dict):


    dir_de_entrada = dados["dir_entrada"][0]
    dir_saida = get_caminho_de_saida(dados["dir_saida"])
    tipo_correcao = dados["tipo_de_correcao"]

    dados_de_entrada = carregar_dados(dir_de_entrada, tipo_correcao)
    df_redacoes = []  # PLACE HOLDER Não implementado

    # Corrigir Provas
    df_resultado = corrigir(dados_de_entrada, tipo_correcao)

    # gerar arquivo de estatisticas de correção e salvar
    gerar_relatório(df_resultado, tipo_correcao, dir_saida)

    app.window.popup_botao_ok(
                              "Sucesso!",
                              "O relatório foi gerado com sucesso!",
                              pixmap_customizado=join_paths(
                                  ROOT_PATH, 'recursos', 'imagens','sucesso.png'
                                )
                            )


if __name__ == '__main__':
    app = Aplication()
    app.window.set_corrigir_callback(main)
    app.Run()
