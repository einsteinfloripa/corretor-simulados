from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'input',
        'name': 'dados_alunos_url',
        'message': 'Arraste o arquivo de dados dos alunos para cá: \n',
    },
    {
        'type': 'input',
        'name': 'redacoes_url',
        'message': 'Arraste a pasta de redações para cá: \n',
    },
    {
        'type': 'input',
        'name': 'gabarito_url',
        'message': 'Arraste o arquivo de gabarito para cá: \n',
    },
    {
        'type': 'list',
        'name': 'tipo_correcao',
        'message': 'Escolha o tipo da prova: \n',
        'choices': ['SIMUFSC', 'SIMUENEM', 'SIMULINHO']
    }
]

answers = prompt(questions)