from variaveis import *

def corrigir(lista_respostas):
    dados_alunos = {}

    for resposta_base in lista_respostas:
        dados_alunos[resposta_base[2]] = lista_base_alunos
        
    for resposta in lista_respostas:

        if resposta[0] == "d1":
            numero_questao = int(resposta[3]) 
            if numero_questao > 21:
                numero_questao -= 1


            djonys = dados_alunos[resposta[2]]

            print(djonys)
        elif resposta[0] == "d2":
            #print(resposta)
            numero_questao = int(resposta[3]) 
            if numero_questao > 19:
                numero_questao -= 1
            numero_questao += 41
            dados_alunos[resposta[2]][numero_questao-1] = resposta[4]

    


    #print(dados_alunos["Emanuelli Marques de Souza"])
