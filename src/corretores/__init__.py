def corrigir(dados, tipo_de_correçao):
    if tipo_de_correçao == "ps":
        import src.corretores.corretor_ps as corretor_ps
        return corretor_ps.corrigir(dados)
    else:
        raise NotImplementedError(f'Correção "{tipo_de_correçao}" ainda não implementada')


