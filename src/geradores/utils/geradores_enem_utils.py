from auxilio.variaveis import areas_enem

def gerar_details_aluno_enem(nome_aluno, df_gabarito, df_resultado):
    subjects = gerar_estrutura_disciplinas_enem_aluno()
    df_aluno = df_resultado[df_resultado.index.get_level_values("Nome") == nome_aluno]
    grupos = df_aluno.groupby(["Área", "Matéria"], as_index=False)
    for nome, grupo in grupos:
        subjects[nome[0]][nome[1]]["question_numbers"] = len(grupo)
        subjects[nome[0]][nome[1]]["general_percent"] = round((
                grupo["Verificação"].eq(1).sum() * 100 /
                subjects[nome[0]][nome[1]]["question_numbers"]
            ), 2
        )
        subjects[nome[0]][nome[1]]["answered"] = list(grupo["Verificação"])
        subjects[nome[0]][nome[1]]["detailed"] = list(grupo["Gabarito"])
    return subjects

def gerar_estrutura_disciplinas_enem_aluno():
    estrutura = {}
    for area_enem in areas_enem:
        for chave_dicionario, disciplinas_area in area_enem.items():
            estrutura[chave_dicionario] = {}
            for disciplina in disciplinas_area:
                estrutura[chave_dicionario][disciplina] = {
                    "question_numbers": 0,
                    "general_percent": 0,
                    "answered": [],
                    "detailed": []
                }
    return estrutura
    