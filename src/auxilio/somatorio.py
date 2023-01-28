def somatorio(resposta, gabarito, quantidade_proposicoes):
    NPC = 0
    NPI = 0
    NTPC = 0
    NP = quantidade_proposicoes
    P = 0
    i = 2**(quantidade_proposicoes - 1)
    while i >= 1:
        if gabarito >= i:
            if resposta >= i:
                NPC += 1
                resposta -= i
            NTPC += 1
            gabarito -= i
        elif resposta >= i:
            NPI += 1
            resposta -= i
        i /= 2
    if NPC > NPI:
        P = (NP - (NTPC - (NPC - NPI))) / NP
        return int(round(P * 100, 0))
    return 0
