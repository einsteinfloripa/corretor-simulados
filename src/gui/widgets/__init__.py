from os import path

from PySide6.QtCore import Slot, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
                               QFileDialog, QRadioButton, QLayout, QButtonGroup, QScrollArea,
                               QGroupBox, QSizePolicy, QSpacerItem, QWidget, QMessageBox)

from gui import constantes as gui_cons


### WIDGETS AUXILIARES ###

class CaminhoLabelBtnPair(QGroupBox):

    def __init__(self, texto, scroll_widget_patent):
        super().__init__()

        # vars
        self.scroll_widget_patent = scroll_widget_patent

        # config
        self.setMinimumHeight(gui_cons.ALTURA_CAIXA_COM_OS_CAMINHOS)
        self.setMaximumHeight(gui_cons.ALTURA_CAIXA_COM_OS_CAMINHOS)

        # layout
        self.layout = QHBoxLayout(self)

        # label
        self.label = QLabel(texto)
        self.label.setMaximumWidth(gui_cons.LARGURA_MAXIMA_LABEL_CAMINHO)
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        # botao
        self.btn_remover = QPushButton("Remover")
        self.btn_remover.setMinimumSize(
            gui_cons.LARGURA_BOTAO_REMOVER,
            gui_cons.ALTURA_BOTAO_REMOVER
        )
        self.btn_remover.setMaximumSize(
            gui_cons.LARGURA_BOTAO_REMOVER, gui_cons.ALTURA_BOTAO_REMOVER)
        self.layout.addWidget(self.btn_remover)
        self.btn_remover.clicked.connect(self.remover)

    def get_texto(self):
        return self.label.text()

    @Slot()
    def remover(self):
        self.scroll_widget_patent.remove_caminho(self)


class ScrollWidgetConteinerCaminhos(QScrollArea):

    def __init__(self):
        super().__init__()

        # config
        self.setWidgetResizable(True)
        self.layout = QVBoxLayout(self)

        # main widget
        self.main_widget = QWidget(self)
        self.main_widget_layout = QVBoxLayout(self.main_widget)

        self.setWidget(self.main_widget)

    def adiciona_novo_caminho(self, novo_caminho):

        # valida se o caminho ja existe
        for caminho in self.get_data():
            if caminho == novo_caminho:
                message_box = QMessageBox(QMessageBox.Warning,
                                          "Ops!",
                                          "Arquivo já adicionado.")
                message_box.exec()
                return

        novo_caminho_widget = CaminhoLabelBtnPair(novo_caminho, self)
        self.main_widget_layout.addWidget(novo_caminho_widget)

    def remove_caminho(self, caminho):
        caminho.deleteLater()

    def get_data(self):
        data = []

        count = self.main_widget_layout.count()
        for index in range(count):
            item = self.main_widget_layout.itemAt(index)
            caminho = item.widget().get_texto()
            data.append(caminho)

        return data


### WIDGETS PRINCIPAIS ###

class FrameSelecaoCaminhosDeEntrada(QFrame):

    def __init__(self):
        super().__init__()

        # layout
        self.layout = QVBoxLayout(self)

        # WIDGETS
        # botoes
        self.btn_dados = QPushButton("Selecione o diretório dos dados")
        # Widgets que contem os caminhos de entrada
        self.scroll_dados = ScrollWidgetConteinerCaminhos()


        self.btn_dados.clicked.connect(
            lambda: self.procura_caminho("gabarito"))

        self.layout.addWidget(self.btn_dados)
        self.layout.addWidget(self.scroll_dados)


    @Slot()
    def procura_caminho(self, tipo_arquivo):
        caminho_arquivo = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.scroll_dados.adiciona_novo_caminho(caminho_arquivo)


    def get_data(self):
        caminhos_dados = self.scroll_dados.get_data()
        return {
            'dir_entrada': caminhos_dados,
        }


class FrameSelecaoTipoDeCorrecao(QFrame):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # WIDGESTS
        self.grupo_botoes = QButtonGroup(self)

        self.label_topo = QLabel("Escolha o tipo de correção: ")
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

        self.layout.addWidget(self.label_topo)
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

        self.layout = QVBoxLayout(self)
        # WIDGETS
        self.btn_salvar = QPushButton("Salvar na pasta:")
        self.label_salvar = QLabel("Não selecionado")
        self.label_salvar.setWordWrap(True)

        self.btn_salvar.clicked.connect(self.procura_caminho)
        self.layout.addWidget(self.btn_salvar)
        self.layout.addWidget(self.label_salvar)

    @Slot()
    def procura_caminho(self):

        caminho_arquivo = QFileDialog.getExistingDirectory(self,
                                                           "Escolha o diretório",
                                                           "",  # <- Diretorio inicial
                                                           QFileDialog.ShowDirsOnly
                                                           )
        if caminho_arquivo != '':
            self.label_salvar.setText(caminho_arquivo)

    def get_data(self):
        caminho_de_saida = self.label_salvar.text()
        return {'dir_saida': caminho_de_saida}
