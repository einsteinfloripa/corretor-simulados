from src.auxilio import path



class TestPath():

    #TODO: falta testar o caso do executavel
        ### teste get_root_path() ###
    def test_se_retorna_o_diretorio_esperado_quando_nao_freezado_em_executavel(self, mocker):
        mocker.patch('os.path.abspath', return_value = 'home/fulano de tal/caminho')

        saida_esperada = 'home/fulano de tal/caminho'
        saida = path.get_root_path()

        assert saida == saida_esperada


    ### teste get_caminho_de_saida(diretorio) ###
    def test_retorna_caminho_com_pasta_output(self, tmp_path):

        entrada = str(tmp_path)
        saida_esperada = str(tmp_path / 'output')

        saida = path.get_caminho_de_saida(entrada)

        assert saida == saida_esperada


    def test_se_ja_existir_output_retorna_caminho_com_output_n(self, tmp_path):

        entrada = str(tmp_path)
        saida_esperada = str(tmp_path / 'output_2')

        # cria pastas output e output_1 no diretorio temporario
        (tmp_path / 'output').mkdir()
        (tmp_path / 'output_1').mkdir()

        saida = path.get_caminho_de_saida(entrada)

        assert saida == saida_esperada



    ### teste join_paths() ###

    def test_junta_os_caminhos_corretamente(self):
        argumentos = ('home', 'fulano de tal', 'exemplo', 'caminho')
        saida_esperada = "home/fulano de tal/exemplo/caminho"

        saida = path.join_paths(*argumentos)

        assert saida == saida_esperada
