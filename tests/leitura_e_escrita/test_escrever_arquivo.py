import json

import pandas as pd

from src.leitura_e_escrita import escrever_arquivo


class TestEscreverArquivo():

    ### Teste escrever_csv() ###

    def test_se_funcao_cria_arquivo_csv_no_lugar_certo(self, tmp_path):

        df_entrada = pd.DataFrame()

        caminho_do_arquivo_csv = tmp_path / 'teste.csv'

        escrever_arquivo.escrever_csv(caminho_do_arquivo_csv, df_entrada)

        assert caminho_do_arquivo_csv.exists()


    def test_se_conteudo_do_arquivo_csv_esta_correto(self, mock_data, tmp_path):

        df_entrada = pd.read_csv(
            mock_data.get_mock_file_path('dados_csv_1.csv'),
            index_col='id',
            header=0
        )
        caminho_do_arquivo_csv = tmp_path / 'teste.csv'

        escrever_arquivo.escrever_csv(caminho_do_arquivo_csv, df_entrada)

        df_comparacao = df_entrada = pd.read_csv(
            caminho_do_arquivo_csv,
            index_col='id',
            header=0
        )

        assert all(df_entrada == df_comparacao)


    ### Teste escrever_json() ###

    def test_se_funcao_cria_arquivo_json_no_lugar_certo(self, mock_data, tmp_path):

        caminho_do_arquivo_json = tmp_path / 'teste.json'
        dados = mock_data.carrega_dados('dados_json_1.json')

        escrever_arquivo.escrever_json(caminho_do_arquivo_json, dados)
        #testa se o arquivo foi criado
        assert (caminho_do_arquivo_json).exists()


    def test_se_conteudo_do_arquivo_json_esta_correto(self, mock_data, tmp_path):

        caminho_de_entrada = tmp_path / 'teste.json'
        dados_iniciais = mock_data.carrega_dados('dados_json_1.json')

        #funçao testada
        escrever_arquivo.escrever_json(caminho_de_entrada, dados_iniciais)
        #le arquivos escritos pela funçao e compara com os dados iniciais
        with open(caminho_de_entrada, 'r', encoding='utf-8') as file:
            dados_para_comparacao = json.load(file)

        assert dados_iniciais == dados_para_comparacao
