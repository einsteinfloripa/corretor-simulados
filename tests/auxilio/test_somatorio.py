import pytest
from src.auxilio.somatorio import somatorio

class TestSomatorio():

    @pytest.mark.parametrize(
        'resposta,gabarito,quantidade_proposicoes,saida_esperada',
        [
            (11, 26, 5, 60),
            ( 9, 26, 5, 0),
            ( 5, 45, 6, 67),
            (45, 45, 6,100),
            (31, 45, 6, 50),
            (15,  7, 4, 75),
            ( 2, 94, 7, 43),
        ]
    )
    def test_se_retorna_valores_corretos_para_alguns_casos(
            self, resposta, gabarito, quantidade_proposicoes, saida_esperada
        ):

        saida = somatorio(resposta, gabarito, quantidade_proposicoes)

        assert saida == saida_esperada
