import pandas as pd

from src.auxilio.constantes import PS
from src.leitura_e_escrita.escrever_arquivo import escrever_saida


idx = pd.IndexSlice

def gerar(df_dados, extencao_saida, dir_saida):

    mapa_saida = {
        '.json': gerar_json,
        '.csv': gerar_csv,
        '.excel': gerar_excel
    }
    
    lista_de_materias = list(PS.mapa_de_materias.keys())
    
    # Essa operacao muda as colunas de lugar!
    df_dados = df_dados.sort_index(axis=1)
        
    df_estatistica = df_dados.loc[:, idx[['aluno','cpf','total'],:]].join(
        df_dados.loc[:, idx['c01':f'c{PS.n_questoes}', :]]
    )

    df_estatistica = df_estatistica.groupby(level=1, axis=1).sum()
    

    df_estatistica = df_estatistica[['materias', 'cpf', *lista_de_materias, 'total']]
    df_estatistica = df_estatistica.rename(columns={'materias':'aluno'})
    
    numero_de_alunos = (len(df_estatistica) - 1)
    numero_total_de_questoes = numero_de_alunos * PS.n_questoes

    return mapa_saida[extencao_saida](
        df_estatistica, lista_de_materias, numero_de_alunos,
        numero_total_de_questoes, dir_saida
    )



def gerar_json(
        df_estatistica, lista_de_materias, numero_de_alunos,
        numero_total_de_questoes, dir_saida
    ):
    
    # Estatisticas gerais 
    acertos_totais_absoluto = int(df_estatistica.loc['gabarito']['total'])
    acertos_totais_percentual = acertos_totais_absoluto/numero_total_de_questoes

    # Estatisticas dos Alunos
    # alunos = [   
    #     { 
    #       infos: { nome: (str), cpf: (int) },
    #       materias: { 
    #                    $materia1 { absoluto: (int), percentual: (float) },
    #                    ...
    #                 }, 
    #       total : { absoluto: (int), percentual: (float) }
    #     },
    #  ...
    # ]
    alunos = {}
    for linha in df_estatistica.iloc[:,2:].join(df_estatistica['aluno']).iloc[:-1].iterrows():
       
        data = dict(linha[1])
        nome = data.pop('aluno')
        total = data.pop('total')
        alunos[nome] = {}

        for materia in lista_de_materias:
            numero_de_questoes = PS.get_numero_de_questoes(materia)
            alunos[nome][materia] = {
                'absoluto':int(data[materia]), 'percentual':data[materia]/numero_de_questoes
            }
        alunos[nome]['total'] = {
            'absoluto':int(total), 'percentual':total/PS.n_questoes
        }
        
    # Estatisticas das materias
        # mateiras = { $mateira1: { absoluto: (int), percentual: (float) }, ... }
        materias = {}
        valores_absolutos = dict(df_estatistica.loc['gabarito'].iloc[2:-1])
        for materia in lista_de_materias:
            numero_de_questoes = PS.get_numero_de_questoes(materia)
            materias[materia] = {
                'absoluto':int(valores_absolutos[materia]),
                'percentual':valores_absolutos[materia]/(numero_de_questoes*numero_de_alunos)
            }
    
    dados_de_saida = {
        'alunos': alunos,
        'materias': materias,
        'total': {
            'absoluto':acertos_totais_absoluto, 'percentual':acertos_totais_percentual
        }
    }    
    escrever_saida(dir_saida, '.json', dados_de_saida)

def gerar_csv():
    raise NotImplementedError("Ainda não implementado")

def gerar_excel():
    raise NotImplementedError("Ainda não implementado")