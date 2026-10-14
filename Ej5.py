import ast
import operator
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QPushButton, QGridLayout, QTextEdit,
    QLineEdit,
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
    OPERADORES = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 600)

        self.num2 = ""

        maia = QGridLayout()

        self.pantalla = QTextEdit()
        self.pantalla.setReadOnly(True)
        self.pantalla.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        maia.addWidget(self.pantalla, 0, 0, 1, 5)

        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Escribe una operación")
        self.entrada.returnPressed.connect(self.calcular)
        maia.addWidget(self.entrada, 1, 0, 1, 5)

        btn_guion = QPushButton("--")
        btn_par_izq = QPushButton("(")
        btn_par_der = QPushButton(")")
        btn_mod = QPushButton("mod")
        btn_pi = QPushButton("π")

        maia.addWidget(btn_guion, 2, 0)
        maia.addWidget(btn_par_izq, 2, 1)
        maia.addWidget(btn_par_der, 2, 2)
        maia.addWidget(btn_mod, 2, 3)
        maia.addWidget(btn_pi, 2, 4)

        btn_7 = QPushButton("7")
        btn_8 = QPushButton("8")
        btn_9 = QPushButton("9")
        btn_div = QPushButton("/")
        btn_raiz = QPushButton("√")

        maia.addWidget(btn_7, 3, 0)
        maia.addWidget(btn_8, 3, 1)
        maia.addWidget(btn_9, 3, 2)
        maia.addWidget(btn_div, 3, 3)
        maia.addWidget(btn_raiz, 3, 4)

        btn_4 = QPushButton("4")
        btn_5 = QPushButton("5")
        btn_6 = QPushButton("6")
        btn_mult = QPushButton("*")
        btn_cuadrado = QPushButton("x²")

        maia.addWidget(btn_4, 4, 0)
        maia.addWidget(btn_5, 4, 1)
        maia.addWidget(btn_6, 4, 2)
        maia.addWidget(btn_mult, 4, 3)
        maia.addWidget(btn_cuadrado, 4, 4)

        btn_1 = QPushButton("1")
        btn_2 = QPushButton("2")
        btn_3 = QPushButton("3")
        btn_resta = QPushButton("-")
        btn_igual = QPushButton("=")
        btn_igual.setFixedSize(70, 70)

        maia.addWidget(btn_1, 5, 0)
        maia.addWidget(btn_2, 5, 1)
        maia.addWidget(btn_3, 5, 2)
        maia.addWidget(btn_resta, 5, 3)
        maia.addWidget(btn_igual, 5, 4, 2, 1)

        btn_0 = QPushButton("0")
        btn_coma = QPushButton(",")
        btn_porcentaje = QPushButton("%")
        btn_suma = QPushButton("+")

        maia.addWidget(btn_0, 6, 0)
        maia.addWidget(btn_coma, 6, 1)
        maia.addWidget(btn_porcentaje, 6, 2)
        maia.addWidget(btn_suma, 6, 3)

        botones_numericos = [
            btn_0, btn_1, btn_2, btn_3, btn_4,
            btn_5, btn_6, btn_7, btn_8, btn_9
        ]
        for btn in botones_numericos:
            btn.clicked.connect(self.onNumero)

        for boton, simbolo in (
            (btn_suma, "+"),
            (btn_resta, "-"),
            (btn_mult, "*"),
            (btn_div, "/"),
        ):
            boton.clicked.connect(
                lambda checked=False, operador=simbolo: self.insertar(operador)
            )
        btn_coma.clicked.connect(lambda: self.insertar("."))
        btn_igual.clicked.connect(self.calcular)
        btn_mod.clicked.connect(self.borrar)

        contenedor = QWidget()
        contenedor.setLayout(maia)
        self.setCentralWidget(contenedor)
        for boton in contenedor.findChildren(QPushButton):
            boton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.show()
        self.entrada.setFocus()

    def borrar(self):
        self.entrada.clear()
        self.pantalla.clear()

    def onNumero(self):
        boton = self.sender()
        self.insertar(boton.text())

    def insertar(self, texto):
        expresion = self.entrada.text()
        if expresion == "Error":
            expresion = ""
        self.entrada.setText(expresion + texto)

    @classmethod
    def evaluar(cls, nodo):
        if isinstance(nodo, ast.Expression):
            return cls.evaluar(nodo.body)
        if isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
            return nodo.value
        if isinstance(nodo, ast.BinOp) and type(nodo.op) in cls.OPERADORES:
            return cls.OPERADORES[type(nodo.op)](
                cls.evaluar(nodo.left),
                cls.evaluar(nodo.right),
            )
        if isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, (ast.UAdd, ast.USub)):
            valor = cls.evaluar(nodo.operand)
            return valor if isinstance(nodo.op, ast.UAdd) else -valor
        raise ValueError("Expresión no válida")

    def calcular(self):
        expresion = self.entrada.text().strip().replace(",", ".")
        try:
            resultado = self.evaluar(ast.parse(expresion, mode="eval"))
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            self.pantalla.setPlainText(str(resultado))
            self.entrada.setText(str(resultado))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError, OverflowError):
            self.pantalla.setPlainText("Error")
            self.entrada.setText("Error")


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = Ventanas()
    sys.exit(aplicacion.exec())