def gerar_json_redacao(correcao, qtdRedacao):
    writing = {
        "total": 0
    }
    for i in range(4):
        competencia = "c" + str(i+1)
        writing[competencia] = 0

        for aluno in correcao:
            writing[competencia] += aluno[-11 + i]
        writing[competencia] = writing[competencia] / qtdRedacao

    for aluno in correcao:
        writing["total"] += aluno[-7]

    writing["total"] = writing["total"] / qtdRedacao
    
    return writing