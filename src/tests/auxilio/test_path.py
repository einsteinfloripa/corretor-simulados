#import pytest

from pathlib import Path
from src.auxilio import path

### teste get_root_path() ###
def test_se_retorna_o_diretorio_que_contem_o_pyproject():
    '''
    Para garantir que o teste funcione necessario que o comando 
    "pytest" seja executado no diretorio raiz, ou seja, no 
    diretorio com o arquivo pyproject.tmol
    
    Como a finçao get_root_path() varia comforme a file qua a chama
    este teste é um teste implicito
    path.ROOT_PATH = path.get_root_path()
    '''
    saida_esperada = str(Path('.').resolve()) # <- cwd
    saida = path.ROOT_PATH

    assert saida == saida_esperada


### teste get_caminho_de_saida(diretorio) ###
def test_retorna_caminho_com_pasta_output(tmp_path):

    entrada = str(tmp_path)
    saida_esperada = str(tmp_path / 'output')

    saida = path.get_caminho_de_saida(entrada)

    assert saida == saida_esperada


def test_se_ja_existir_output_retorna_caminho_com_output_n(tmp_path):

    entrada = str(tmp_path)
    saida_esperada = str(tmp_path / 'output')

    # cria pasta output_1 no diretorio temporario
    (tmp_path / 'output_1').mkdir()

    saida = path.get_caminho_de_saida(entrada)

    assert saida == saida_esperada



### teste join_paths() ###

def test_junta_os_caminhos_corretamente():
    argumentos = ('home', 'fulano de tal', 'exemplo', 'caminho')
    saida_esperada = "home/fulano de tal/exemplo/caminho"

    saida = path.join_paths(*argumentos)

    assert saida == saida_esperada
