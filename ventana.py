import sys
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class FiestraPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QStackedLayout")

        caixaV = QVBoxLayout()

        self.cmbTipo = QComboBox()
        self.cmbTipo.addItem("Alumno")
        self.cmbTipo.addItems(("Profesor","Pas"))
        self.cmbTipo.setCurrentIndex(-1)

        caixaV.addWidget(self.cmbTipo)

        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    sys.exit(app.exec())