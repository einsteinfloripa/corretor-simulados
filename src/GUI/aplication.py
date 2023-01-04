import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget,
    QVBoxLayout,
    )


class Window(QMainWindow):

    font_style = QFont('Arial')

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        base_container = QWidget()
        base_container.setLayout(layout)

        label = QLabel('Janela genérica')
        label.setFont(Window.font_style)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(label)

        
        base_container.show()
        self.setCentralWidget(base_container)



app = QApplication()

janela = Window()
janela.show()

app.exec()