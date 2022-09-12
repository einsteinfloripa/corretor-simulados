# Deve possuir o mesmo nome dos arquivo das provas
aplicacoes = ["d1-i", "d1-e", "d1-i-ae", "d1-e-ae", "d2", "d2-ae"]

areas_ufsc = [{"Primeira Língua": ["Português/Literatura"]},
              {"Segunda Língua": ["Inglês", "Espanhol"]},
              {"Matemática": ["Matemática"]},
              {"Biologia": ["Biologia"]},
              {"Ciências Humanas e Sociais": ["História",
                                              "Geografia", "Filosofia/Sociologia", "Português/Literatura"]},
              {"Física": ["Física"]},
              {"Química": ["Química"]}]

areas_enem = [{"Linguagens, códigos e suas tecnologias": ["Literatura e Artes", "Português", "Inglês", "Espanhol"]},
              {"Ciências Humanas e suas tecnologias": ["História", "Geografia", "Filosofia/Sociologia"]},
              {"Ciências da Natureza e suas tecnologias": ["Biologia", "Física", "Química"]},
              {"Matemática e suas tecnologias": ["Matemática"]}
              ]

total_questoes = 181 # Total de questões da prova + 1 para a lingua
max_questoes_por_dia = 90
lista_base_alunos = [0]*total_questoes


