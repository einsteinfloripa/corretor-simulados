from variaveis import *

def corrigir(lista_respostas):
    alunos = []
    for resposta in lista_respostas:
        pessoa = lista_base_alunos
        pessoa[0] = resposta[2]
        alunos.append(pessoa)
    print(alunos)
        
