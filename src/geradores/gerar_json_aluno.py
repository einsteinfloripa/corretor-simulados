# TODO: por questão de tempo, não fiz um bom if para verificar se o aluno fez ingles ou espanhol, vou arrumar melhor depois, talvez em um simuenem?

from dis import dis
from geradores.gerar_json_geral_disciplina import *
from auxilio.variaveis import areas_ufsc
from geradores.utils.geradores_enem_utils import gerar_details_aluno_enem

def gerar_json_alunos(correcao, respostas, dados_alunos, gabarito, tipo_correcao):
    

    if tipo_correcao == "simufsc":
        return gerar_json_simufsc(correcao, respostas, dados_alunos, gabarito)
    if tipo_correcao == "simuenem":
        return gerar_json_simuenem(correcao, respostas, dados_alunos, gabarito)
    if tipo_correcao == "simulinho":
        print("Simulinho não implementado ainda")


def gerar_json_simuenem(correcao, respostas, dados_alunos, gabarito):
    student_dataset = []
    for aluno in correcao:
            nome_aluno = aluno[0]
            total_acertos = calcular_total_acertos(aluno) 
            cpf, msg_tutor = pegar_cpf_e_msg_tutor(nome_aluno, dados_alunos)
            posicao = encontrar_posicao(correcao, total_acertos)

            student_dataset.append(
                {
                    "info": {
                        "name": nome_aluno,
                        "cpf": cpf,
                        "total": total_acertos,
                        "position": posicao,
                        "msg": msg_tutor
                    },
                    "detailed": {
                        "subjects": gerar_details_aluno_enem(aluno, gabarito, respostas),
                        # "writing": {
                        #     "c1": {
                        #         "note": aluno[-11],
                        #         "comment": aluno[-6]
                        #     },
                        #     "c2": {
                        #         "note": aluno[-10],
                        #         "comment": aluno[-5]
                        #     },
                        #     "c3": {
                        #         "note": aluno[-9],
                        #         "comment": aluno[-4]
                        #     },
                        #     "c4": {
                        #         "note": aluno[-8],
                        #         "comment": aluno[-3]
                        #     },
                        #     "general_comment": aluno[-2],
                        #     "iframe": aluno[-1],
                        #     "total": aluno[-7]
                        # }
                    }
                }
            )

    return student_dataset

def gerar_json_simufsc(correcao, respostas, dados_alunos, gabarito):
   for aluno in correcao:
            print(aluno)
            nome_aluno = aluno[0]
            nota_total = aluno[84] + aluno[89]
            cpf, msg_tutor = pegar_cpf_e_msg_tutor(nome_aluno, dados_alunos)
            # posicao = encontrar_posicao(correcao, nota_total)
            
            nota_total = "1"
            posicao = 1
            
            return (
                {
                    "info": {
                        "name": nome_aluno,
                        "cpf": cpf,
                        "total": nota_total,
                        "position": posicao,
                        "msg": msg_tutor
                    },
                    "detailed": {
                        "subjects": []
                        # "subjects": gerar_details_aluno(aluno, gabarito, respostas),
                        # "writing": {
                        #     "c1": {
                        #         "note": aluno[-11],
                        #         "comment": aluno[-6]
                        #     },
                        #     "c2": {
                        #         "note": aluno[-10],
                        #         "comment": aluno[-5]
                        #     },
                        #     "c3": {
                        #         "note": aluno[-9],
                        #         "comment": aluno[-4]
                        #     },
                        #     "c4": {
                        #         "note": aluno[-8],
                        #         "comment": aluno[-3]
                        #     },
                        #     "general_comment": aluno[-2],
                        #     "iframe": aluno[-1],
                        #     "total": aluno[-7]
                        # }
                    }
                }
            ) 

def pegar_cpf_e_msg_tutor(nome_aluno, dados_alunos):
    cpf = ""
    msg_tutor = ""
    nome_formatado = nome_aluno.lower()
    for aluno in dados_alunos:
        if nome_formatado in aluno[0].lower():
            cpf = aluno[1].replace("-", "").replace(".", "")
            if len(aluno) >= 3:
                msg_tutor = aluno[2]
            break
    return cpf, msg_tutor

def encontrar_posicao(correcao, nota_total):
    todas_notas_totais = []
    for aluno in correcao:
        todas_notas_totais.append(calcular_total_acertos(aluno))
        
    todas_notas_totais.sort(reverse=True)
    posicao = todas_notas_totais.index(nota_total) + 1
    return posicao

def calcular_total_acertos(aluno):
    acertos = 0
    for questao in aluno:
        if questao != 0:
            acertos += 1

    return acertos