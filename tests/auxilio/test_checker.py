from src.auxilio.checker import check

import pytest


class TestChecker:

    #### Testes para verificar se os dados de entrada possuem valores nulos

    @pytest.mark.parametrize(
        'linha, coluna',
        [
            # (linha, coluna)
            (1, 'cpf'),
            (2, 'aluno')
        ]
    )
    def test_encontra_valores_nulos_dados_alunos(self, linha, coluna, mock_data):
        dados_entrada = mock_data.carrega_dados('ps')
        # Anula uma celula
        dados_entrada['dados_alunos'].loc[linha, coluna] = None
        

        with pytest.raises(ValueError) as excinfo:
            check(dados_entrada, 'ps')
        
        assert f'Valores nulos encontrados nos dados dos alunos' in str(excinfo.value)
        
    @pytest.mark.parametrize(
        'linha, coluna',
        [
            # (linha, coluna)
            (59, 'numero'),
            (4, 'resposta')
        ]
    )
    def test_encontra_valores_nulos_gabarito(self, linha, coluna, mock_data):
        dados_entrada = mock_data.carrega_dados('ps')
        # Anula uma celula
        dados_entrada['gabarito'].loc[linha, coluna] = None
        

        with pytest.raises(ValueError) as excinfo:
            check(dados_entrada, 'ps')
        
        assert f'Valores nulos encontrados no gabarito' in str(excinfo.value)

    @pytest.mark.parametrize(
        'linha, coluna',
        [
            # (linha, coluna)
            (1, 'cpf'),
            (3, 'aluno'),
            (2, '5')
        ]
    )
    def test_encontra_valores_nulos_respostas(self, linha, coluna, mock_data):
        dados_entrada = mock_data.carrega_dados('ps')
        # Anula uma celula
        dados_entrada['respostas'].loc[linha, coluna] = None
        

        with pytest.raises(ValueError) as excinfo:
            check(dados_entrada, 'ps')
        
        assert f'Valores nulos encontrados nas respostas' in str(excinfo.value)

    
    #### Testes para verificar se os dados de entrada do gabarito possuem o numero de questoes corretas
    @pytest.mark.parametrize(
        'linhas',
        [
            # linha
            [59],
            (4, 7, 8),
        ]
    )
    def test_verifica_numero_de_questoes_gabarito(self, linhas, mock_data):
        dados_entrada = mock_data.carrega_dados('ps')
        
        # Deleta a linha $linha do gabarito
        for linha in linhas:
            dados_entrada['gabarito'] = dados_entrada['gabarito'].drop(linha, axis=0)
        # Nova quantidade de linhas no gabarito
        n_linhas = dados_entrada['gabarito'].shape[0]

        with pytest.raises(ValueError) as excinfo:
            check(dados_entrada, 'ps')
        
        assert f'O número de questões no gabarito({n_linhas}) é diferente de 60' in str(excinfo.value)
    


    #### Testes para conferir a se todas as respostas possuem o cpf em 'dados_alunos'
    @pytest.mark.parametrize(
        'linhas',
        [
            # linha
            [1],
            (0, 2, 3),
        ]
    )
    def test_verifica_se_todos_os_alunos_tem_resostas(self, linhas, mock_data):    
        dados_entrada = mock_data.carrega_dados('ps')
        
        cpfs = []
        for linha in linhas:
            # Guarda o numeor dos cpfs que serão deletados
            cpfs.append(str(dados_entrada['dados_alunos'].loc[linha, 'cpf']))
            # Deleta a $linhas do dados_alunos
            dados_entrada['dados_alunos'] = dados_entrada['dados_alunos'].drop(linha, axis=0)

        with pytest.raises(ValueError) as excinfo:
            check(dados_entrada, 'ps')
        
        assert f'Cpf(s) {[cpf for cpf in cpfs]} não encontrado(s) na lista de dados dos alunos.' in str(excinfo.value)