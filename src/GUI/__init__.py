import sys
from os import path

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication,
    QVBoxLayout, QMainWindow, QPushButton, QWidget,
    QFrame, QMenu, QMessageBox)


from GUI.widgets import (FrameSelecaoCaminhosDeEntrada,
                         FrameSelecaoTipoDeCorrecao,
                         FrameSelecaoCaminhoDeSaida, )

from GUI import constantes as gui_cons
import GUI.auxiliar as aux




class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        #variavais
        self.DEBUG_MODE = False

        #config
        self.setFixedSize(gui_cons.largura_da_janela, gui_cons.altura_da_janela)
        self.setWindowTitle("Corretor de provas")

        #menu principal
        self.main_menu = self.menuBar()
        # menu opçoes
        self.options_menu = QMenu("Opçoes", self.main_menu)
        self.options_menu.addAction("Debug mode").setCheckable(True)
        self.options_menu.triggered.connect(self.set_opcao)

        self.main_menu.addMenu(self.options_menu)

        # Frame principal
        self.mainframe = QFrame()
        #layout do frame principal
        self.layout = QVBoxLayout(self.mainframe)

        # Adiciona os widgets filhos
        self.frame_caminhos_entrada = FrameSelecaoCaminhosDeEntrada(self)
        self.frame_correçao = FrameSelecaoTipoDeCorrecao(self)
        self.frame_caminho_saida = FrameSelecaoCaminhoDeSaida(self)
        self.btn_corrigir = QPushButton('Corrigir')
        self.btn_corrigir.setMinimumHeight(gui_cons.altura_botao_corrigir)
        
        self.layout.addWidget(self.frame_caminhos_entrada)
        self.layout.addWidget(self.frame_correçao)
        self.layout.addWidget(self.frame_caminho_saida)
        self.layout.addWidget(self.btn_corrigir)

        self.btn_corrigir.clicked.connect(self.corrigir)

        self.setCentralWidget(self.mainframe)
    

    def set_corrigir_callback(self, func):
        self.funçao_corrigir = func


    @Slot()
    def corrigir(self):        

        dados = dict()
        dados.update( self.frame_caminhos_entrada.get_data() )
        dados.update( self.frame_correçao.get_data() )
        dados.update( self.frame_caminho_saida.get_data() )

        valores_nao_selecionados = aux.confere_se_nao_nulo(dados)

        if self.DEBUG_MODE:
            aux.print_dados(dados)
        elif valores_nao_selecionados != None:
            
            texto = 'Os seguintes campos não estão preenchidos: '
            for valor in valores_nao_selecionados:
                texto = texto + valor + ', '
            texto = texto.strip(', ')
            texto = texto + '.'

            message_box = QMessageBox( QMessageBox.Warning, "Valores nulos!" ,texto)
            message_box.exec()

        else:
            self.funçao_corrigir(dados)
    

    @Slot()
    def set_opcao(self, action):
        if action.text() == "Debug mode":
            self.DEBUG_MODE = action.isChecked()


class Aplication(QApplication):
    
    def __init__(self):
        super().__init__(sys.argv)
        self.icone = QIcon(gui_cons.caminho_icone)
        self.setWindowIcon(self.icone)
        self.window = Window()

    def Run(self):
        self.window.show()
        sys.exit(self.exec())