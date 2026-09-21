import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout,
    QPushButton, QWidget, QLabel, QLineEdit
)
from PyQt6.QtGui import QColor, QPalette


class CaixaCor(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.getPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("blue"))
        self.setPalette(paleta)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera aplicación QL")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        # Color de fondo
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("lightblue"))
        self.setPalette(paleta)

        # Creación de widgets
        boton = QPushButton("Principal")
        self.etiqueta = QLabel("ola a todos")
        self.cuadroTexto = QLineEdit()
        self.cuadroTexto.setPlaceholderText("Introduce o teu nome")

        # Conectamos TANTO el botón COMO la tecla Enter (returnPressed) a la misma función
        boton.clicked.connect(self.on_boton_clicked)
        self.cuadroTexto.returnPressed.connect(self.on_boton_clicked)

        # Configuración del layout
        caixaV = QVBoxLayout()
        caixaV.addWidget(self.etiqueta)
        caixaV.addWidget(self.cuadroTexto)
        caixaV.addWidget(boton)

        # Creación del contenedor principal
        contedor = QWidget()
        contedor.setLayout(caixaV)

        # Establecer el contenedor único como widget central
        self.setCentralWidget(contedor)

        self.show()

    def on_boton_clicked(self):
        nome = self.cuadroTexto.text()
        if len(nome) != 0 :
            self.etiqueta.setText("Ola "+ nome +". Encantado de terte por aqui.")
        else:
            self.etiqueta.setText("Por favor, insira tu nombre")

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()