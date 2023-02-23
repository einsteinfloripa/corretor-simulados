import pytest
from pandas import DataFrame, read_csv

from src.leitura_e_escrita.ler_arquivo import ler_csv, csvs_to_dfs

from src.auxilio.variaveis import (
    nome_col_df_dados_alunos,
    nome_col_df_gabarito,
    nome_col_df_respostas,
)

class TestLerArquivos():

    nome_colunas = [
        nome_col_df_dados_alunos,
        nome_col_df_respostas,
        nome_col_df_gabarito,
    ]

    ### Teste ler_csv() ###

    def test_se_retorna_data_frame_se_colunas_foram_passadas_como_parametro(self, mock_data):
        caminho_dados = mock_data.get_mock_file_path('dados_csv_1.csv')
        
        df_teste = ler_csv(
            caminho_dados, 
            nome_colunas=['id','first_name','last_name','email','gender','ip_address']
        )
        ler_csv(caminho_dados)

        assert isinstance(df_teste, DataFrame)


    ### Teste csvs_to_dfs() ###

    def test_se_retorna_todos_os_data_frames(self, mock_data):
        
        caminhos_de_entrada = (
            mock_data.get_mock_file_path('dados_data_frame/mock_dados_alunos.csv'),
            mock_data.get_mock_file_path('dados_data_frame/mock_gabarito.csv'),
            mock_data.get_mock_file_path('dados_data_frame/mock_respostas.csv')
        )

        saida = csvs_to_dfs(*caminhos_de_entrada)

        assert isinstance(saida[0], DataFrame) and isinstance(saida[1], DataFrame) \
               and isinstance(saida[2], DataFrame)


    @pytest.mark.parametrize('caminho_arquivo_testado,indice',
        [
            ('dados_data_frame/mock_dados_alunos.csv',0),
            ('dados_data_frame/mock_respostas.csv',1),
            ('dados_data_frame/mock_gabarito.csv',2),
        ],
        ids=['dados_alunos', 'dados_respostas', 'dados_gabarito']
    )
    def testa_se_o_conteudo_de_cada_data_frame_esta_correto(self, mock_data, 
        caminho_arquivo_testado, indice):
        
        caminhos_de_entrada = (
            mock_data.get_mock_file_path('dados_data_frame/mock_dados_alunos.csv'),
            mock_data.get_mock_file_path('dados_data_frame/mock_respostas.csv'),
            mock_data.get_mock_file_path('dados_data_frame/mock_gabarito.csv'),
        )

        saida = csvs_to_dfs(*caminhos_de_entrada)
        df_comparacao = read_csv(  # <- pandas.read_csv
            mock_data.get_mock_file_path(caminho_arquivo_testado), sep=",", quotechar='"',
            names=TestLerArquivos.nome_colunas[indice], encoding="utf-8"
        )

        assert all(saida[indice] == df_comparacao)
