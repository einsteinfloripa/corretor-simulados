import pandas as pd

from src.auxilio.constantes import PS

def check(dados_entrada : dict[str : pd.DataFrame], tipo_correcao : str) -> None:
    mapa_correcao = {
        "simuenem": check_simuenem,
        "simufsc": check_ufsc,
        "simulinho": check_simulinho,
        "ps": check_ps
    }

    # Universal checks
    # Valores NaN ou nulos
    
    if True in dados_entrada['gabarito'].isnull().any().values:
        raise ValueError(f'Valores nulos encontrados no gabarito')
    if True in dados_entrada['dados_alunos'][['aluno', 'cpf']].isna().any().values:
        raise ValueError(f'Valores nulos encontrados nos dados dos alunos')
    if True in dados_entrada['respostas'].isna().any().values:
        raise ValueError(f'Valores nulos encontrados nas respostas')
    

    # Checa se todos os alunos em dados_alunos estão em respostas
    cpf_alunos = dados_entrada['dados_alunos']['cpf'].astype(str)
    cpf_respostas = dados_entrada['respostas']['cpf'].astype(str)
    cpf_nao_encontrados = list(dados_entrada['respostas'][~cpf_respostas.isin(cpf_alunos)]['cpf'])
    if len(cpf_nao_encontrados) > 0:
        raise ValueError(
            f'Cpf(s) {[cpf for cpf in cpf_nao_encontrados]} não encontrado(s) na lista de dados dos alunos.'
        )
    
    mapa_correcao[tipo_correcao](dados_entrada)


def check_ps(dados_entrada):

    df_alunos = dados_entrada['dados_alunos']
    df_gabarito = dados_entrada['gabarito']
    df_respostas = dados_entrada['respostas']

    # Checa se os campos obrigatórios estão presentes
    _check_required_fields(dados_entrada)

    # Checa se o número de questões é o esperado
    n_gab = len(dados_entrada['gabarito'])
    if n_gab != PS.n_questoes:
        raise ValueError(f"O número de questões no gabarito({n_gab}) é diferente de {PS.n_questoes}")



def check_simuenem(*args, **kwargs):
    print(f"Função de check_simuenem não implementada")

def check_ufsc(*args, **kwargs):
    print(f"Função de check_ufsc não implementada")

def check_simulinho(*args, **kwargs):
    print(f"Função de check_simulinho não implementada")



# Private
    
def _check_required_fields(dados_entrada : dict[str : pd.DataFrame]) -> None:
    for nome, df in dados_entrada.items():
        required_fields = PS.required_fields[nome]
        columns = df.columns
        for field in required_fields:
            if field not in columns:
                raise ValueError(f'Coluna "{field}" não encontrado no arquivo: "{nome}"')

