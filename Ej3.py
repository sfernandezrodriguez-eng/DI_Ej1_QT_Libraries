import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout,
    QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout
)
from PyQt6.QtGui import QColor, QPalette


class CaixaCor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)


class Ventanas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora del amor de Gabriela por Casal")
        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 400)

        layout0 = QVBoxLayout()

        layout_principal = QHBoxLayout()

        layout_col1 = QVBoxLayout()
        layout_col1.addWidget(QPushButton("--"))
        layout_col1.addWidget(QPushButton("7"))
        layout_col1.addWidget(QPushButton("4"))
        layout_col1.addWidget(QPushButton("1"))
        layout_col1.addWidget(QPushButton("0"))

        layout_col2 = QVBoxLayout()
        layout_col2.addWidget(QPushButton("("))
        layout_col2.addWidget(QPushButton("8"))
        layout_col2.addWidget(QPushButton("5"))
        layout_col2.addWidget(QPushButton("2"))
        layout_col2.addWidget(QPushButton(","))

        layout_col3 = QVBoxLayout()
        layout_col3.addWidget(QPushButton(")"))
        layout_col3.addWidget(QPushButton("9"))
        layout_col3.addWidget(QPushButton("6"))
        layout_col3.addWidget(QPushButton("3"))
        layout_col3.addWidget(QPushButton("%"))




        layout_col4 = QVBoxLayout()
        layout_col4.addWidget(QPushButton("mod"))
        layout_col4.addWidget(QPushButton("/"))
        layout_col4.addWidget(QPushButton("*"))
        layout_col4.addWidget(QPushButton("-"))
        layout_col4.addWidget(QPushButton("+"))

        layout_col5 = QVBoxLayout()
        layout_col5.addWidget(QPushButton("π"))
        layout_col5.addWidget(QPushButton("√"))
        layout_col5.addWidget(QPushButton("x²"))
        layout_col5.addWidget(QPushButton("="))
        layout_col5.addWidget(QPushButton(""))

        layout_principal.addLayout(layout_col1)
        layout_principal.addLayout(layout_col2)
        layout_principal.addLayout(layout_col3)
        layout_principal.addLayout(layout_col4)
        layout_principal.addLayout(layout_col5)


        layout_blanco = QVBoxLayout()
        layout_blanco.addWidget(CaixaCor("white"))

        layout0.addLayout(layout_blanco)
        layout0.addLayout(layout_principal)

        contedor = QWidget()
        contedor.setLayout(layout0)
        self.setCentralWidget(contedor)

        self.show()






if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = Ventanas()
    sys.exit(aplicacion.exec())