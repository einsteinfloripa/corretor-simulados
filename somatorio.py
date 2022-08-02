from ast import For
from re import I


def somatorio(resposta, gabarito, quantidade_proposiçoes):
    NPC = 0
    NPI = 0
    NTPC = 0
    NP = quantidade_proposiçoes
    P = 0
    i = 2**(quantidade_proposiçoes - 1)
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
        return int(round(P * 100 , 0))
    return 0