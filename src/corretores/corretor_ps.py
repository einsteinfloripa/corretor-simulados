import pandas as pd

from src.auxilio.constantes import PS


def corrigir(dados: dict[str : pd.DataFrame]) -> pd.DataFrame:

    df_alunos = dados["dados_alunos"]
    df_gabarito = dados["gabarito"]
    df_respostas = dados["respostas"]

    df_alunos = df_alunos.astype(str)
    # junta os dados dos alunos com as respostas
    df_total = df_alunos.merge(df_respostas, on="cpf")
    ponto_de_corte = len(df_total.columns)

    # Isola df com as respostas e o gabarito
    somente_respostas = df_total.iloc[:, len(df_alunos.columns) :].values
    somente_gabarito = df_gabarito["resposta"].values

    # compara e cria um novo dataframe com valores booleanos
    df_corrigido = pd.DataFrame(
        somente_respostas == somente_gabarito,
        columns=[f"c{int(q):02}" for q in df_gabarito["numero"].values],
    )
    # junta as correçoes ao df total
    df_total = df_total.merge(df_corrigido, left_index=True, right_index=True)

    # cria uma coluna com a quantidade de acertos por aluno
    df_total["total"] = df_total.iloc[
        :, (len(df_total.columns) - len(df_corrigido.columns)) :
    ].sum(axis=1)

    # cria um linha com a quantidade de acertos por materia
    linha_soma = pd.concat(
        [
            pd.Series(["total"] + [None for _ in range(len(df_alunos.columns) - 1)]),
            pd.Series(df_gabarito["resposta"].values),
            df_total.iloc[:, ponto_de_corte:].sum(),
        ]
    )

    linha_soma.index = df_total.columns
    df_total.loc["gabarito"] = linha_soma

    # cria uma linha com as materias

    linha_materias = (
        ["materias", "cpf"]
        + [f"{i}_info" for i in range(len(df_alunos.columns) - 2)]
        + [
            subject
            for _ in range(2)
            for subject, values in PS.mapa_de_materias.items()
            for _ in range(values[1] - values[0] + 1)
        ]
        + ["total"]
    )

    df_total.columns = pd.MultiIndex.from_tuples(
        [*zip(df_total.columns, linha_materias)]
    )

    return df_total
