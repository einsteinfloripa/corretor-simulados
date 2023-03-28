from pathlib import Path
import pandas as pd
from auxilio.variaveis import (
    nome_col_df_dados_alunos_enem,
    nome_col_df_gabarito_enem,
    nome_col_df_respostas_enem,
    nome_col_df_gabarito_simulinho,
    nome_col_df_respostas_simulinho
)

# TODO: Adicionar UFSC
def csvs_to_dfs(*paths, tipo_correcao):
    dfs = []
    if tipo_correcao == "simuenem":
        lista_tupla_paths = list(
            zip(
                paths,
                [nome_col_df_dados_alunos_enem, nome_col_df_respostas_enem, nome_col_df_gabarito_enem]
            )
        )

    if tipo_correcao == "simulinho":
        lista_tupla_paths = list(
            zip(
                paths,
                #[nome_col_df_dados_alunos_simulinho, nome_col_df_respostas_simulinho, nome_col_df_gabarito_simulinho],
                [nome_col_df_dados_alunos_enem, nome_col_df_respostas_simulinho, nome_col_df_gabarito_simulinho] # PLACE HOLDER
            )
        )

    for tupla in lista_tupla_paths:
        dfs.append(ler_csv(tupla[0], nome_colunas=tupla[1]))
    return dfs


def ler_csv(caminho: str, nome_colunas=None) -> pd.DataFrame:

    if nome_colunas is not None:  # Assumindo que o CSV não vira com nomes nas colunas
        pandas_df = pd.read_csv(
            Path(caminho), sep=",", quotechar='"', names=nome_colunas, encoding="utf-8"
        )

    return pandas_df
