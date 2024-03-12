def tipo_correcao_simulado():
    tipo_correcao = ""
    while tipo_correcao not in ["simufsc", "simuenem", "simulinho"]:
        tipo_correcao = input(
            "Tipo de correção: (A: SIMUFSC, B: SIMUENEM, C: SIMULINHO) \n"
        ).lower()

        if tipo_correcao == "a":
            tipo_correcao = "simufsc"
        elif tipo_correcao == "b":
            tipo_correcao = "simuenem"
        elif tipo_correcao == "c":
            tipo_correcao = "simulinho"

        if tipo_correcao not in ["simufsc", "simuenem", "simulinho"]:
            print(
                "Tipo de correção inválido, somente é aceito SIMUFSC, SIMUENEM ou SIMULINHO"
            )

    return tipo_correcao
