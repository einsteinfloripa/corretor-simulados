import pandas as pd


def corrigir(dados: dict[str : pd.DataFrame], tipo_de_correcao: str) -> pd.DataFrame:
    if tipo_de_correcao == "ps":
        from src.corretores import corretor_ps

        return corretor_ps.corrigir(dados)

    raise NotImplementedError(
        f'Correção "{tipo_de_correcao}" ainda não implementada'
    )
