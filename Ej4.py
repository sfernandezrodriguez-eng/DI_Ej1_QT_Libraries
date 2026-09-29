import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout,
    QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QTextEdit
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
        self.setWindowTitle("Calculadora")
        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 400)

        maia = QGridLayout()
        btnboton1 = QPushButton("1")
        btnboton2 = QPushButton("2")
        txtCadroTexto = QTextEdit()
        btnboton3 = QPushButton("3")
        btnboton4 = QPushButton("4")
        btnboton5 = QPushButton("5")
        btnboton6 = QPushButton("6")

        maia.addWidget(btnboton1)
        maia.addWidget(btnboton2,0,1,1,2)
        maia.addWidget(txtCadroTexto,1,0,2,1)
        maia.addWidget(btnboton4,1,1,1,2)
        maia.addWidget(btnboton5,2,1,1,1)
        maia.addWidget(btnboton6,2,2,1,1)

        contenedor = QWidget()

        contenedor.setLayout(maia)


        self.setCentralWidget(contenedor)

        self.show()






if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = Ventanas()
    sys.exit(aplicacion.exec())