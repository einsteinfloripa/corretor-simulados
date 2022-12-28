import pandas as pd

def ler_csv(caminho: str, nome_colunas = None) -> pd.DataFrame:

    if nome_colunas != None: # Assumindo que o CSV não vira com nomes nas colunas
        pandas_df = pd.read_csv(caminho,
                                sep=",",
                                quotechar='"',
                                names = nome_colunas,
                                encoding="utf-8")

    return pandas_df