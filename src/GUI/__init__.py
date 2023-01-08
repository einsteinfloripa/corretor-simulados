import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QVBoxLayout, QMainWindow, QPushButton, QWidget,
    QFrame)


from GUI.widgets import (Frame_seleçao_caminhos_de_entrada,
                             Frame_seleçao_tipo_de_correçao,
                             Frame_seleçao_caminho_de_saida)




class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        # Frame princimal
        self.mainframe = QFrame()
        #layout do frame principal
        self.layout = QVBoxLayout(self.mainframe)

        # Adiciona os widgets filhos
        self.frame_caminhos_entrada = Frame_seleçao_caminhos_de_entrada(self)
        self.frame_correçao = Frame_seleçao_tipo_de_correçao(self)
        self.frame_caminho_saida = Frame_seleçao_caminho_de_saida(self)
        self.btn_corrigir = QPushButton('Corrigir')
        
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

        self.funçao_corrigir(dados)
    



class Aplication(QApplication):
    
    def __init__(self):
        super().__init__(sys.argv)
        self.window = Window()

    def Run(self):
        self.window.show()
        sys.exit(self.exec())