from pathlib import Path
import csv
import json
import sys
from unittest import mock

import pytest

from src.leitura_e_escrita.ler_arquivo import carregar_dados

## Mocks de modulos
sys.modules['src.gui'] = mock.MagicMock()

### Carregamento de dados

class MockDataLoader():

    def __init__(self):
        self.mock_root_path = Path(__file__) / '..' / '..' / 'recursos' / 'exemplos'


    def carrega_dados(self, tipo_de_prova : str):
        if tipo_de_prova == 'ps':
            dir_path = self.__get_mock_file_path('exemplo_ps')
            return carregar_dados(dir_path, 'ps')
        else:
            raise NotImplementedError(f"MockDataLoader para tipo de prova '{tipo_de_prova}' não implementado")


    def __get_mock_file_path(self, str_caminho):
        return self.mock_root_path.joinpath(str_caminho).resolve()


@pytest.fixture
def mock_data():
    return MockDataLoader()

### Dados validados a mao

class DadosValidados:
    
    class PS:
        saida_aluno_A = {
            'info' : { 'nome' : 'aluno A', 'cpf' : '11111111111'},
            'total' : { 'absoluto' : 29, 'percentual' : (29/60)},
            'materias' : {
                'portugues' : { 'absoluto' : 8, 'percentual' : (8/12)},
                'matematica' : { 'absoluto' : 5, 'percentual' : (5/10)},
                'fisica' : { 'absoluto' : 2, 'percentual' : (2/6)},
                'quimica' : { 'absoluto' : 1, 'percentual' : (1/6)},
                'historia' : { 'absoluto' : 5, 'percentual' : (5/6)},
                'biologia' : { 'absoluto' : 1, 'percentual' : (1/6)},
                'geografia' : { 'absoluto' : 0, 'percentual' : 0.0},
                'filosofia-sociologia' : { 'absoluto' : 2, 'percentual' : (2/3)},
                'interdisciplinar' : { 'absoluto' : 5, 'percentual' : 1.0}
            }
        }

        materias = {
            'portugues' : {
                'absoluto' : 13,
                'percentual' : (13/(12*4))
            },
            'matematica' : {
                'absoluto' : 11,
                'percentual' : (11/(10*4))
            },
            'fisica' : {
                'absoluto' : 4,
                'percentual' : (4/(6*4))
            },
            'quimica' : {
                'absoluto' : 3,
                'percentual' : (3/(6*4))
            },
            'historia' : {
                'absoluto' : 6,
                'percentual' : (6/(6*4))
            },
            'biologia' : {
                'absoluto' : 6,
                'percentual' : (6/(6*4))
            },
            'geografia' : {
                'absoluto' : 8,
                'percentual' : (8/(6*4))
            },
            'filosofia-sociologia' : {
                'absoluto' : 7,
                'percentual' : (7/(3*4))
            },
            'interdisciplinar' : {
                'absoluto' : 5,
                'percentual' : (5/(4*5))
            }
        }

        total = {
            'absoluto' : 63,
            'percentual' : (63/(60*4))
        }


@pytest.fixture
def dados_validados():
    return DadosValidados

###
