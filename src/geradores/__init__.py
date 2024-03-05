
def gerar_relatório(dados, tipo_correcao, dir_saida, extencao_saida='.json'):

    if tipo_correcao == "ps":
        import src.geradores.gerar_ps as gerador
        return gerador.gerar(dados, extencao_saida, dir_saida)
    
    elif tipo_correcao == "enem":
        raise NotImplementedError("Ainda não implementado")
    
    elif tipo_correcao == "ufsc":
        raise NotImplementedError("Ainda não implementado")
    
    elif tipo_correcao == "simulinho":
        raise NotImplementedError("Ainda não implementado")

