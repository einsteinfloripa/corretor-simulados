import sys
from corretores.corretor_enem import correcao_enem
from corretores.corretor_simulinho import correcao_simulinho


def corrigir(df_respostas, df_gabarito, _, tipo_correcao):

    if tipo_correcao == "simufsc":
        print("Correção de simulado ufsc não implementado")
        # dados_alunos, resultado_alunos = correcao_ufsc(
        #     gabarito, dados_alunos, resultado_alunos)
        # return gerar_lista_resultado_alunos_ufsc(resultado_alunos, redacoes)
        sys.exit()

    if tipo_correcao == "simuenem":
        # TODO Arrumar argumento "tipo_correcao" e Imports
        # df_resultado = correcao_enem(df_respostas, df_gabarito, tipo_correcao)
        df_resultado = correcao_enem(df_respostas, df_gabarito)
        return df_resultado

    if tipo_correcao == "simulinho":
        # print("Correção de simulinho não implementada")
        # sys.exit()

        df_resultado = correcao_simulinho(df_respostas, df_gabarito, tipo_correcao)
        return df_resultado
