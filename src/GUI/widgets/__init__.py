from os import path

from PySide6.QtCore import Slot, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
                               QFileDialog, QRadioButton, QLayout, QButtonGroup, QScrollArea,
                               QGroupBox, QSizePolicy, QSpacerItem, QWidget, QMessageBox)

from GUI import variaveis as guiVars


### WIDGETS AUXILIARES ###

class Caminho_label_btn_pair(QGroupBox):

    def __init__(self, text, scroll_widget_patent):
        super().__init__()
        
        #vars
        self.scroll_widget_patent = scroll_widget_patent

        #config
        self.setMinimumHeight(guiVars.altura_caixa_com_os_caminhos)
        self.setMaximumHeight(guiVars.altura_caixa_com_os_caminhos)

        #layout
        self.layout = QHBoxLayout(self)

        #label
        self.label = QLabel(text)
        self.label.setMaximumWidth(guiVars.largura_maxima_label_caminho)
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        #botao
        self.btn_remover = QPushButton("Remover")
        self.btn_remover.setMinimumSize(guiVars.largura_botao_remover,guiVars.altura_botao_remover)
        self.btn_remover.setMaximumSize(guiVars.largura_botao_remover,guiVars.altura_botao_remover)
        self.layout.addWidget(self.btn_remover)
        self.btn_remover.clicked.connect(self.remover)


    def text(self):
        return self.label.text()
    

    def set_text(self, text):
        self.label.setText(text)
    

    @Slot()
    def remover(self):
        self.scroll_widget_patent.remove_caminho(self)
    

class Scroll_Widget_conteiner_caminhos(QScrollArea):
    
    def __init__(self):
        super().__init__()
        
        #config
        self.setWidgetResizable(True)
        self.layout = QVBoxLayout(self)

        #main widget
        self.main_widget = QWidget(self)
        self.main_widget_layout = QVBoxLayout(self.main_widget)

        self.setWidget(self.main_widget)


    def adiciona_novo_caminho(self, novo_caminho):
        
        # valida se o caminho ja existe
        for caminho in self.get_data():
            if caminho == novo_caminho:
                #precisa de um icone
                message_box = QMessageBox(QMessageBox.Warning, 
                                          "Ops!",
                                          "Arquivo já adicionado.")
                message_box.exec()
                return

        novo_caminho_widget = Caminho_label_btn_pair(novo_caminho, self)
        self.main_widget_layout.addWidget(novo_caminho_widget)
        

    def remove_caminho(self, caminho):
        caminho.deleteLater()
    

    def get_data(self):
        data = []

        count = self.main_widget_layout.count()
        for index in range(count):
            item = self.main_widget_layout.itemAt(index)
            caminho = item.widget().text()
            data.append(caminho)
        
        return data


### WIDGETS PRINCIPAIS ###

class Frame_seleçao_caminhos_de_entrada(QFrame):


    def __init__(self, parent = None):
        super().__init__()
        
        #layout
        self.layout = QVBoxLayout(self)

        #WIDGETS
        #botoes
        self.btn_gabarito = QPushButton("Adicionar Gabarito")
        self.btn_respostas = QPushButton("Adicionar Resposta")
        #lista de pares labels-botoes
        self.scroll_gabarito = Scroll_Widget_conteiner_caminhos()
        self.scroll_respostas = Scroll_Widget_conteiner_caminhos()
        
    
        self.btn_gabarito.clicked.connect(lambda : self.procura_caminho("gabarito"))
        self.btn_respostas.clicked.connect(lambda : self.procura_caminho("respostas"))


        self.layout.addWidget(self.btn_gabarito)
        self.layout.addWidget(self.scroll_gabarito)
        self.layout.addWidget(self.btn_respostas)
        self.layout.addWidget(self.scroll_respostas)
      

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
                self.scroll_gabarito.adiciona_novo_caminho(caminho_arquivo[0])

            elif tipo_arquivo == "respostas":
                self.scroll_respostas.adiciona_novo_caminho(caminho_arquivo[0])


    def get_data(self):
        caminhos_gabaritos = self.scroll_gabarito.get_data()
        caminhos_respostas = self.scroll_respostas.get_data()
        return {
                    'caminhos_gabaritos':caminhos_gabaritos,
                    'caminhos_respostas':caminhos_respostas,
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
        self.label_salvar.setWordWrap(True)

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

