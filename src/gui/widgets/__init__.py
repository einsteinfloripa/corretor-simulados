from os import path

from PySide6.QtCore import Slot, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
                               QFileDialog, QRadioButton, QLayout, QButtonGroup, QScrollArea,
                               QGroupBox, QSizePolicy, QSpacerItem, QWidget, QMessageBox)

from gui import constantes as gui_cons


### WIDGETS AUXILIARES ###

class DirLabel(QGroupBox):

    def __init__(self, texto, widget_patent):
        super().__init__()

        # Vars
        self.widget_patent = widget_patent

        # Config
        self.setMinimumHeight(gui_cons.ALTURA_CAIXA_COM_OS_CAMINHOS)
        self.setMaximumHeight(gui_cons.ALTURA_CAIXA_COM_OS_CAMINHOS)

        # layout
        self.layout = QHBoxLayout(self)

        # label
        self.label = QLabel(texto)
        self.label.setMaximumWidth(gui_cons.LARGURA_MAXIMA_LABEL_CAMINHO)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.label)

    def get_texto(self):
        return self.label.text()


class WidgetConteinerDir(QFrame):

    def __init__(self):
        super().__init__()
        # Config
        self.layout = QVBoxLayout(self)
        self.label = DirLabel("Não selecionado", self)
        self.layout.addWidget(self.label)


    def adiciona_novo_caminho(self, novo_caminho):

        if self.layout.count() > 0:
            self.remove_caminho(self.layout.itemAt(0).widget())

        self.label = DirLabel(novo_caminho, self)
        self.layout.addWidget(self.label)

    def remove_caminho(self, dirlabel):
        dirlabel.deleteLater()
    
    def get_data(self):
        if self.label is not None:
            return self.label.get_texto()
        else: return ''

### WIDGETS PRINCIPAIS ###

class FrameSelecaoCaminhoDeEntrada(QFrame):

    def __init__(self):
        super().__init__()

        # layout
        self.layout = QVBoxLayout(self)
        
        # WIDGETS
        # Botoes
        self.btn_select = QPushButton("Selecione o diretório dos dados")
        self.btn_select.setMinimumHeight(gui_cons.ALTURA_BOTAO_PROCURAR)
        # Widgets que contem os caminhos de entrada
        self.container_dir = WidgetConteinerDir()


        self.btn_select.clicked.connect(self.procura_caminho)

        self.layout.addWidget(self.btn_select)
        self.layout.addWidget(self.container_dir)


    @Slot()
    def procura_caminho(self):
        caminho_arquivo = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.container_dir.adiciona_novo_caminho(caminho_arquivo)


    def get_data(self):
        caminhos_dados = self.container_dir.get_data()
        return {
            'dir_entrada': caminhos_dados,
        }


class FrameSelecaoTipoDeCorrecao(QFrame):

    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        # Widgets
        self.grupo_botoes = QButtonGroup(self)

        self.label = QLabel("Escolha o tipo de correção: ")
        font = self.label.font()
        font.setPointSize(gui_cons.TAMANHO_FONTE_LABEL)
        self.label.setFont(font)

        self.simuenem_radio_btn = QRadioButton("SIMUENEM")
        self.simufsc_radio_btn = QRadioButton("SIMUFSC")
        self.simulinho_radio_btn = QRadioButton("SIMULINHO")
        self.ps_radio_btn = QRadioButton("PS")

        self.grupo_botoes.addButton(self.simuenem_radio_btn)
        self.grupo_botoes.addButton(self.simufsc_radio_btn)
        self.grupo_botoes.addButton(self.simulinho_radio_btn)
        self.grupo_botoes.addButton(self.ps_radio_btn)
        self.grupo_botoes.setId(self.simuenem_radio_btn, 0)
        self.grupo_botoes.setId(self.simufsc_radio_btn, 1)
        self.grupo_botoes.setId(self.simulinho_radio_btn, 2)
        self.grupo_botoes.setId(self.ps_radio_btn, 3)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.simuenem_radio_btn)
        self.layout.addWidget(self.simufsc_radio_btn)
        self.layout.addWidget(self.simulinho_radio_btn)
        self.layout.addWidget(self.ps_radio_btn)

    def get_data(self):
        btn_id = self.grupo_botoes.checkedId()

        if btn_id == 0:
            return {'tipo_de_correcao': 'simuenem'}
        elif btn_id == 1:
            return {'tipo_de_correcao': 'simufsc'}
        elif btn_id == 2:
            return {'tipo_de_correcao': 'simulinho'}
        elif btn_id == 3:
            return {'tipo_de_correcao': 'ps'}
        else:
            return {'tipo_de_correcao': 'Não selecionado'}


class FrameSelecaoCaminhoDeSaida(QFrame):

    def __init__(self):
        super().__init__()

        # layout
        self.layout = QVBoxLayout(self)

        # WIDGETS
        # Botoes
        self.btn_select = QPushButton("Selecione o diretório de saida")
        self.btn_select.setMinimumHeight(gui_cons.ALTURA_BOTAO_PROCURAR)
        # Widgets que contem os caminhos de entrada
        self.container_dir = WidgetConteinerDir()


        self.btn_select.clicked.connect(self.procura_caminho)

        self.layout.addWidget(self.btn_select)
        self.layout.addWidget(self.container_dir)


    @Slot()
    def procura_caminho(self):
        caminho_arquivo = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.container_dir.adiciona_novo_caminho(caminho_arquivo)


    def get_data(self):
        caminhos_dados = self.container_dir.get_data()
        return {
            'dir_saida': caminhos_dados,
        }
