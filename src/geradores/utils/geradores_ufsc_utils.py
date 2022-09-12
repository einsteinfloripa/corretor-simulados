def gerar_json_simufsc(correcao, respostas, dados_alunos, gabarito):
   for aluno in correcao:
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