import pandas as pd


def gerar_relatorio(
    dados: pd.DataFrame, tipo_correcao: str, dir_saida: str, extencao_saida=".json"
) -> None:

    if tipo_correcao == "ps":
        import src.geradores.gerar_ps as gerador

        return gerador.gerar(dados, extencao_saida, dir_saida)

    if tipo_correcao == "enem":
        raise NotImplementedError("Ainda não implementado")

    if tipo_correcao == "ufsc":
        raise NotImplementedError("Ainda não implementado")

    if tipo_correcao == "simulinho":
        raise NotImplementedError("Ainda não implementado")
