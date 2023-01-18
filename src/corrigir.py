from corretores.corretor_enem import correcao_enem

def corrigir(df_respostas, df_gabarito, redacoes, tipo_correcao):

    if (tipo_correcao == "simufsc"):
        print("Correção de simulado ufsc não implementado")
        # dados_alunos, resultado_alunos = correcao_ufsc(
        #     gabarito, dados_alunos, resultado_alunos)
        # return gerar_lista_resultado_alunos_ufsc(resultado_alunos, redacoes)
        exit()

    if (tipo_correcao == "simuenem"):

        df_resultado = correcao_enem(df_respostas, df_gabarito)
        return df_resultado

    if (tipo_correcao == "simulinho"):
        print("Correção de simulinho não implementada")
        exit()



