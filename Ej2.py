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
        self.setWindowTitle("Ventanas")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        layout_principal = QHBoxLayout()

        layout_col1 = QVBoxLayout()
        layout_col1.addWidget(CaixaCor("red"))
        layout_col1.addWidget(CaixaCor("yellow"))
        layout_col1.addWidget(CaixaCor("purple"))

        caixa_verde = CaixaCor("green")

        layout_col3 = QVBoxLayout()
        layout_col3.addWidget(CaixaCor("red"))
        layout_col3.addWidget(CaixaCor("purple"))

        layout_principal.addLayout(layout_col1)
        layout_principal.addWidget(caixa_verde)
        layout_principal.addLayout(layout_col3)

        contedor = QWidget()
        contedor.setLayout(layout_principal)
        self.setCentralWidget(contedor)

        self.show()






if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = Ventanas()
    sys.exit(aplicacion.exec())