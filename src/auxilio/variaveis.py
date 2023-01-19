# Deve possuir o mesmo nome dos arquivo das provas
aplicacoes = ["respostas-alunos"]

areas_ufsc = [{"Primeira Língua": ["Português/Literatura"]},
              {"Segunda Língua": ["Inglês", "Espanhol"]},
              {"Matemática": ["Matemática"]},
              {"Biologia": ["Biologia"]},
              {"Ciências Humanas e Sociais": ["História",
                                              "Geografia", "Filosofia/Sociologia", "Português/Literatura"]},
              {"Física": ["Física"]},
              {"Química": ["Química"]}]

areas_enem = [{"Linguagens, códigos e suas tecnologias": ["$"]},
              {"Ciências Humanas e suas tecnologias": ["$"]},
              {"Ciências da Natureza e suas tecnologias": ["$"]},
              {"Matemática e suas tecnologias": ["$"]}]


# Nome em ordem das colunas dos arquivos csv SIMUENEM
nome_col_df_dados_alunos = ["Nome", "CPF", "2Lingua", "Curso", "Cota"]
nome_col_df_gabarito = ["Área", "Questão", "Gabarito", "Matéria"]
nome_col_df_respostas = ["Nome","CPF","2Lingua","Cota",
                         "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19",
                         "20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37",
                         "38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55",
                         "56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73",
                         "74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91",
                         "92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108",
                         "109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124",
                         "125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140",
                         "141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156",
                         "157","158","159","160","161","162","163","164","165","166","167","168","169","170","171","172",
                         "173","174","175","176","177","178","179","180"]

# Códigos para 2lingua e posição respostas
# ENEM
posicao_linguas_na_planilha = {
                              "Inglês":   {"Início": 0, "Fim": 5},
                              "Espanhol": {"Início": 5, "Fim": 10}
                              #"2LinguaZ": {"Início": 10,"Fim": 15}
                              }

codigo_2lingua_dicionario = {"2Lingua":
                                        {
                                        "Inglês":   {"Código": 0, "Posição": [posicao_linguas_na_planilha["Inglês"]["Início"],
                                                                              posicao_linguas_na_planilha["Inglês"]["Fim"]]},
                                        "Espanhol": {"Código": 1, "Posição": [posicao_linguas_na_planilha["Espanhol"]["Início"],
                                                                              posicao_linguas_na_planilha["Espanhol"]["Fim"]]},
                                        #"2LinguaZ":{"Código": 2, "Posição": [posicao_linguas_na_planilha["2LinguaZ"]["Início"],
                                        #                                     posicao_linguas_na_planilha["2LinguaZ"]["Fim"]]},
                                        "Quantidade": 5
                                        }
                            }