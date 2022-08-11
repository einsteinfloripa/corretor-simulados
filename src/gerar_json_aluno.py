from gerar_json_disciplina import *

def gerar_json_alunos(correcao, dados_alunos, gabarito):
    students_dataset = []
    for aluno in correcao:
        nome_aluno = aluno[0]
        nota_total = aluno[84]
        cpf = pegar_cpf(nome_aluno, dados_alunos)
        posicao = encontrar_posicao(correcao, nota_total)
        
    
        subjects = gerar_estrutura_disciplinas()
        subjects = gerar_detalhado_disciplina_estrutura(subjects, correcao, gabarito)
        
        students_dataset.append(
            {
                "info": {
                    "name": nome_aluno,
                    "cpf": cpf,
                    "total": nota_total,
                    "position": posicao 
                },
                "details": subjects 
                # TODO: Incluir redação no detalhado
                # TODO: Incluir msg do tutor
            }
        )

    return students_dataset

def pegar_cpf(nome_aluno, dados_alunos):
    cpf = ""
    nome_formatado = nome_aluno.lower()
    for aluno in dados_alunos:
        if nome_formatado in aluno[0].lower():
            cpf = aluno[1]
            break
    return cpf 

def encontrar_posicao(correcao, nota_total):
    todas_notas_totais = []
    for aluno in correcao:
        todas_notas_totais.append(aluno[84])
        
    todas_notas_totais.sort(reverse=True)
    posicao = todas_notas_totais.index(nota_total) + 1
    return posicao