from auxilio.variaveis import *
from auxilio.somatorio import *
from auxilio.funcoes_corrigir import *

from corretores.corretor_ufsc import correcao_ufsc
from corretores.corretor_enem import correcao_enem


def corrigir(lista_respostas, gabarito, redacoes, tipo_correcao):
    dados_alunos, resultado_alunos = gerar_base(lista_respostas)
    if (tipo_correcao == "simufsc"):
        dados_alunos, resultado_alunos = correcao_ufsc(
            gabarito, dados_alunos, resultado_alunos)
        return gerar_lista_resultado_alunos_ufsc(resultado_alunos, redacoes)

    if (tipo_correcao == "simuenem"):
        dados_alunos, resultado_alunos = correcao_enem(
            gabarito, dados_alunos, resultado_alunos)

        return gerar_lista_resultado_alunos_enem(resultado_alunos, redacoes)
    
    if (tipo_correcao == "simulinho"):
        print("Correção de simulinho não implementada")




