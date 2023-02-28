from pathlib import Path
import csv
import json


import pytest


### Carregamento de dados

class MockDataLoader():

    def __init__(self):
        self.mock_root_path = Path(__file__) / '..' / 'mock'


    def get_mock_file_path(self, str_caminho):
        return self.mock_root_path.joinpath(str_caminho).resolve()


    def carrega_dados(self, str_caminho):
        fullpath = self.get_mock_file_path(str_caminho)
        if '.json' in str_caminho:
            return self.__carrega_json(fullpath)
        elif '.csv' in str_caminho:
            return self.__carrega_csv(fullpath)


    def __carrega_csv(self, str_caminho):
        with open(str_caminho, 'r', encoding='utf8') as open_file:
            data = []
            for row in csv.reader(open_file):
                data.append(row)
        return data

    def __carrega_json(self, str_caminho):
        with open(str_caminho, 'r', encoding='utf8') as open_file:
            return json.load(open_file)


@pytest.fixture
def mock_data():
    return MockDataLoader()

###
