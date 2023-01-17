from auxilio.variaveis import nome_col_df_dados_alunos, nome_col_df_gabarito, nome_col_df_respostas
import pandas as pd

def csvs_to_dfs(*paths):
    dfs = []
    lista_tupla_paths = list(zip(paths, [nome_col_df_dados_alunos, nome_col_df_respostas, nome_col_df_gabarito]))
    for tupla in lista_tupla_paths:
        dfs.append(ler_csv(tupla[0], nome_colunas = tupla[1]))
    return dfs

def ler_csv(caminho: str, nome_colunas = None) -> pd.DataFrame:

    if nome_colunas != None: # Assumindo que o CSV não vira com nomes nas colunas
        pandas_df = pd.read_csv(caminho,
                                sep=",",
                                quotechar='"',
                                names = nome_colunas,
                                encoding="utf-8")

    return pandas_df