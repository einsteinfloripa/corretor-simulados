from os import path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QFrame, QLabel,
                               QFileDialog, QRadioButton, QLayout, QButtonGroup)



class Frame_seleçao_caminhos_de_entrada(QFrame):

    def __init__(self, parent = None):
        super().__init__()

        self.layout = QVBoxLayout(self)
        # WIDGETS
        self.btn_gabarito = QPushButton("Gabarito")
        self.label_gabarito = QLabel("Não selecionado")
        self.btn_respostas = QPushButton("Resposta")
        self.label_respostas = QLabel("Não selecionado")
        
    
        self.btn_gabarito.clicked.connect(lambda : self.procura_caminho("gabarito"))
        self.btn_respostas.clicked.connect(lambda : self.procura_caminho("respostas"))


        self.layout.addWidget(self.btn_gabarito)
        self.layout.addWidget(self.label_gabarito)
        self.layout.addWidget(self.btn_respostas)
        self.layout.addWidget(self.label_respostas)
      

    @Slot()
    def procura_caminho(self, tipo_arquivo):
        
        caminho_arquivo = QFileDialog.getOpenFileName( 
            self,
            "Arquivo de " + tipo_arquivo,
            path.pardir,
            "Arquivo de dados (*.xlsx *.csv)",
            )
        
        if caminho_arquivo[0] != '':
            if tipo_arquivo == "gabarito":
                self.label_gabarito.setText(caminho_arquivo[0])
            elif tipo_arquivo == "respostas":
                self.label_respostas.setText(caminho_arquivo[0])


    def get_data(self):
        caminho_gabarito = self.label_gabarito.text()
        caminho_respostas = self.label_respostas.text()
        return {
                    'caminho_gabarito':caminho_gabarito,
                    'caminho_resposta':caminho_respostas,
               }  


class Frame_seleçao_tipo_de_correçao(QFrame):
    
    def __init__(self, parent=None):
        super().__init__()

        self.layout = QVBoxLayout(self)

        #WIDGESTS
        self.grupo_botoes = QButtonGroup(self)

        self.label_topo = QLabel("Escolha o tipo de correção: ")
        self.simuenem_radio_btn = QRadioButton("SIMUENEM")
        self.simufsc_radio_btn = QRadioButton("SIMUFSC")
        self.simulinho_radio_btn = QRadioButton("SIMULINHO")

        self.grupo_botoes.addButton(self.simuenem_radio_btn)
        self.grupo_botoes.addButton(self.simufsc_radio_btn)
        self.grupo_botoes.addButton(self.simulinho_radio_btn)
        self.grupo_botoes.setId(self.simuenem_radio_btn, 0)
        self.grupo_botoes.setId(self.simufsc_radio_btn, 1)
        self.grupo_botoes.setId(self.simulinho_radio_btn, 2)

        self.layout.addWidget(self.label_topo)
        self.layout.addWidget(self.simuenem_radio_btn)
        self.layout.addWidget(self.simufsc_radio_btn)
        self.layout.addWidget(self.simulinho_radio_btn)


    def get_data(self):
        btn_id = self.grupo_botoes.checkedId()

        if btn_id == 0:
            return { 'tipo_de_correcao' : 'simuenem'}
        elif btn_id == 1:
            return { 'tipo_de_correcao' : 'simufsc'}
        elif btn_id == 2:
            return { 'tipo_de_correcao' : 'simulinho'}
        else:
            return {'tipo_de_correcao' : 'nao selecioando'}


class Frame_seleçao_caminho_de_saida(QFrame):

    def __init__(self, parent = None):
        super().__init__()

        self.layout = QVBoxLayout(self)
        # WIDGETS
        self.btn_salvar = QPushButton("Salvar Como")
        self.label_salvar = QLabel("Não selecionado")

        self.btn_salvar.clicked.connect(self.procura_caminho)
    
        self.layout.addWidget(self.btn_salvar)
        self.layout.addWidget(self.label_salvar)
       

    @Slot()
    def procura_caminho(self):
        
        caminho_arquivo = QFileDialog.getSaveFileName(self)
        
        if caminho_arquivo[0] != '':
            self.label_salvar.setText(caminho_arquivo[0])
    

    def get_data(self):
        caminho_de_saida = self.label_salvar.text()
        return { 'caminho_de_saida' : caminho_de_saida }

