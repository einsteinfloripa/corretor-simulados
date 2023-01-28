import sys
from os import path

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QMainWindow,
    QPushButton,
    QWidget,
    QFrame,
    QMenu,
    QMessageBox,
)


from gui.widgets import (
    FrameSelecaoCaminhosDeEntrada,
    FrameSelecaoTipoDeCorrecao,
    FrameSelecaoCaminhoDeSaida,
)

from gui import constantes as gui_cons
import gui.auxiliar as aux


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        # variavais
        self.debug_mode = False
        self.funcao_corrigir = None

        # config
        self.setFixedSize(gui_cons.LARGURA_DA_JANELA, gui_cons.ALTURA_DA_JANELA)
        self.setWindowTitle("Corretor de provas")

        # menu principal
        self.main_menu = self.menuBar()
        # menu opcoes
        self.options_menu = QMenu("Opcoes", self.main_menu)
        self.options_menu.addAction("Debug mode").setCheckable(True)
        self.options_menu.triggered.connect(self.set_opcao)

        self.main_menu.addMenu(self.options_menu)

        # Frame principal
        self.mainframe = QFrame()
        # layout do frame principal
        self.layout = QVBoxLayout(self.mainframe)

        # Adiciona os widgets filhos
        self.frame_caminhos_entrada = FrameSelecaoCaminhosDeEntrada()
        self.frame_correcao = FrameSelecaoTipoDeCorrecao()
        self.frame_caminho_saida = FrameSelecaoCaminhoDeSaida()
        self.btn_corrigir = QPushButton("Corrigir")
        self.btn_corrigir.setMinimumHeight(gui_cons.ALTURA_BOTAO_CORRIGIR)

        self.layout.addWidget(self.frame_caminhos_entrada)
        self.layout.addWidget(self.frame_correcao)
        self.layout.addWidget(self.frame_caminho_saida)
        self.layout.addWidget(self.btn_corrigir)

        self.btn_corrigir.clicked.connect(self.corrigir)

        self.setCentralWidget(self.mainframe)

    def set_corrigir_callback(self, func):
        self.funcao_corrigir = func

    @Slot()
    def corrigir(self):

        dados = {}
        dados.update(self.frame_caminhos_entrada.get_data())
        dados.update(self.frame_correcao.get_data())
        dados.update(self.frame_caminho_saida.get_data())

        valores_nao_selecionados = aux.confere_se_nao_nulo(dados)

        if self.debug_mode:
            aux.print_dados(dados)
        elif valores_nao_selecionados is not None:

            texto = "Os seguintes campos não estão preenchidos: "
            for valor in valores_nao_selecionados:
                texto = texto + valor + ", "
            texto = texto.strip(", ")
            texto = texto + "."

            message_box = QMessageBox(QMessageBox.Warning, "Valores nulos!", texto)
            message_box.exec()

        else:
            self.funcao_corrigir(dados)

    @Slot()
    def set_opcao(self, action):
        if action.text() == "Debug mode":
            self.debug_mode = action.isChecked()


class Aplication(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.icone = QIcon(gui_cons.CAMINHO_ICONE)
        self.setWindowIcon(self.icone)
        self.window = Window()

    def Run(self):
        self.window.show()
        sys.exit(self.exec())
