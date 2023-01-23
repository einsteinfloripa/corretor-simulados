

def print_dados(dados):
    print('------------------------------------------------------')
    for key, value in dados.items():
        print(f'key: {key:20}  -   value: {value}')
    print('------------------------------------------------------')


def confere_se_nao_nulo(dados):

    nome_para_imprimir = {
        'caminhos_gabaritos': "Gabaritos",
        'caminhos_respostas'  : "Respostas",
        'tipo_de_correcao'  : "Tipo de correçao",
        'caminho_de_saida'  : "Caminho de saida",
    }

    flag_valor_adicionado = False
    valores_nulos = list()

    for key, value in dados.items():
        if value == "Não selecionado" or value == []:
            valores_nulos.append(nome_para_imprimir[key])
            flag_valor_adicionado = True
    
    if flag_valor_adicionado:
        return valores_nulos
    else:
        return None