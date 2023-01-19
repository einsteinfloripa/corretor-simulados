from __future__ import print_function, unicode_literals
from InquirerPy import inquirer

def get_input_usuario():
    dados_alunos_path= inquirer.text(message="Arraste o arquivo de dados dos alunos para cá: \n").execute()
    respostas_alunos_path = inquirer.text(message="Arraste o arquivo de respostas dos alunos para cá: \n").execute()
    gabarito_path = inquirer.text(message="Arraste o arquivo de gabarito para cá: \n").execute()
    redacoes_path = inquirer.text(message="Arraste a pasta de redações para cá: \n").execute()
    tipo_correcao = inquirer.select(
            message = "Escolha o tipo da prova: \n",
            choices = ["SIMUFSC", "SIMUENEM", "SIMULINHO"]).execute()

    return(dados_alunos_path, respostas_alunos_path, gabarito_path, redacoes_path, tipo_correcao.lower())