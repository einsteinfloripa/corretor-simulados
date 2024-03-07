# test_integration.py
import json
from unittest import mock

import pytest

from src.__main__ import main

class TestIntegration:

    @pytest.mark.t
    def test_integration_ps(self, tmp_path, dados_validados):
        # Variaveis de entrada
        dir_entrada = 'recursos/exemplos/exemplo_ps'
        tipo_de_correcao = 'ps'
        dir_saida = tmp_path

        # Para evitar erros de interface grafica, que nao esta presente nos testes
        window = mock.MagicMock()
        # Gera relatorio com os dados de entrada
        main({
            'dir_entrada': dir_entrada,
            'tipo_de_correcao': tipo_de_correcao,
            'dir_saida': dir_saida
        },
        window
        )
        #Carrega relatorio gerado
        with open(tmp_path / 'output' / 'relatorio.json') as f:
            data = json.load(f)
        
        # Carrega dados validados e dados gerados para o aluno 1
        saida_aluno_A_validada = dados_validados.PS.saida_aluno_A
        saida_aluno_A_gerada = data['alunos'][0]
        # Carrega os dados validados e gerados por materia
        materias_validadas = dados_validados.PS.materias
        materias_geradas = data['materias']
        # Carrega os dados validados e gerados para o total
        total_validado = dados_validados.PS.total
        total_gerado = data['total']

        # Compara relatorio gerado com dados validados
        # Sao dicionarios e, portanto, podem ser comparados diretamente
        assert saida_aluno_A_gerada == saida_aluno_A_validada
        assert materias_geradas == materias_validadas
        assert total_gerado == total_validado