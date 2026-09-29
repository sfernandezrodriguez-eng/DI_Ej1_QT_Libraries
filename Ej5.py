import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QPushButton, QGridLayout, QTextEdit
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
        self.setMaximumSize(400, 600)

        self.num2 = ""

        maia = QGridLayout()

        self.pantalla = QTextEdit()
        maia.addWidget(self.pantalla, 0, 0, 1, 5)

        btn_guion = QPushButton("--")
        btn_par_izq = QPushButton("(")
        btn_par_der = QPushButton(")")
        btn_mod = QPushButton("mod")
        btn_pi = QPushButton("π")

        maia.addWidget(btn_guion, 1, 0)
        maia.addWidget(btn_par_izq, 1, 1)
        maia.addWidget(btn_par_der, 1, 2)
        maia.addWidget(btn_mod, 1, 3)
        maia.addWidget(btn_pi, 1, 4)

        btn_7 = QPushButton("7")
        btn_8 = QPushButton("8")
        btn_9 = QPushButton("9")
        btn_div = QPushButton("/")
        btn_raiz = QPushButton("√")

        maia.addWidget(btn_7, 2, 0)
        maia.addWidget(btn_8, 2, 1)
        maia.addWidget(btn_9, 2, 2)
        maia.addWidget(btn_div, 2, 3)
        maia.addWidget(btn_raiz, 2, 4)

        btn_4 = QPushButton("4")
        btn_5 = QPushButton("5")
        btn_6 = QPushButton("6")
        btn_mult = QPushButton("*")
        btn_cuadrado = QPushButton("x²")

        maia.addWidget(btn_4, 3, 0)
        maia.addWidget(btn_5, 3, 1)
        maia.addWidget(btn_6, 3, 2)
        maia.addWidget(btn_mult, 3, 3)
        maia.addWidget(btn_cuadrado, 3, 4)

        btn_1 = QPushButton("1")
        btn_2 = QPushButton("2")
        btn_3 = QPushButton("3")
        btn_resta = QPushButton("-")
        btn_igual = QPushButton("=")
        btn_igual.setFixedSize(70, 70)

        maia.addWidget(btn_1, 4, 0)
        maia.addWidget(btn_2, 4, 1)
        maia.addWidget(btn_3, 4, 2)
        maia.addWidget(btn_resta, 4, 3)
        maia.addWidget(btn_igual, 4, 4, 2, 1)

        btn_0 = QPushButton("0")
        btn_coma = QPushButton(",")
        btn_porcentaje = QPushButton("%")
        btn_suma = QPushButton("+")

        maia.addWidget(btn_0, 5, 0)
        maia.addWidget(btn_coma, 5, 1)
        maia.addWidget(btn_porcentaje, 5, 2)
        maia.addWidget(btn_suma, 5, 3)

        botones_numericos = [
            btn_0, btn_1, btn_2, btn_3, btn_4,
            btn_5, btn_6, btn_7, btn_8, btn_9
        ]
        for btn in botones_numericos:
            btn.clicked.connect(self.onNumero)

        contenedor = QWidget()
        contenedor.setLayout(maia)
        self.setCentralWidget(contenedor)

        self.show()

    def onNumero(self):
        boton = self.sender()
        num = boton.text()
        self.num2 = self.num2 + num
        self.pantalla.setText(self.num2)


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = Ventanas()
    sys.exit(aplicacion.exec())