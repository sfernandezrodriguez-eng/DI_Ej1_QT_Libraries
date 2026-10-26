import random
import sys

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class CasillaButton(QPushButton):
    rightClicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            self.rightClicked.emit()
            event.accept()
            return
        super().mousePressEvent(event)


class Minesweeper(QMainWindow):
    FILAS = 8
    COLUMNAS = 8
    NUM_MINAS = 10

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MineSweeper")
        self.setMinimumSize(700, 500)

        self.botones = {}
        cuadrilla = QGridLayout()
        cuadrilla.setContentsMargins(16, 16, 16, 16)
        cuadrilla.setSpacing(4)

        for fila in range(self.FILAS):
            cuadrilla.setRowStretch(fila, 1)
            cuadrilla.setColumnStretch(fila, 1)
            for columna in range(self.COLUMNAS):
                boton = CasillaButton("")
                boton.setSizePolicy(
                    QSizePolicy.Policy.Expanding,
                    QSizePolicy.Policy.Expanding,
                )
                boton.rightClicked.connect(
                    lambda f=fila, c=columna: self.alternar_banderilla(f, c)
                )
                boton.clicked.connect(
                    lambda checked=False, f=fila, c=columna:
                    self.revelar_casilla(f, c)
                )
                self.botones[(fila, columna)] = boton
                cuadrilla.addWidget(boton, fila, columna)

        bloqueTablero = QWidget()
        bloqueTablero.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        bloqueTablero.setLayout(cuadrilla)

        bloqueDerecho = QWidget()
        bloqueDerecho.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        layoutDerecho = QVBoxLayout(bloqueDerecho)
        layoutDerecho.setContentsMargins(24, 24, 24, 24)
        self.lblEstado = QLabel()
        self.lblEstado.setWordWrap(True)
        layoutDerecho.addWidget(QLabel("MineSweeper"))
        layoutDerecho.addWidget(self.lblEstado)
        btnNuevaPartida = QPushButton("Nueva partida")
        btnNuevaPartida.clicked.connect(self.nueva_partida)
        layoutDerecho.addWidget(btnNuevaPartida)
        layoutDerecho.addStretch()

        layoutPrincipal = QHBoxLayout()
        layoutPrincipal.setContentsMargins(12, 12, 12, 12)
        layoutPrincipal.setSpacing(12)
        layoutPrincipal.addWidget(bloqueTablero, 3)
        layoutPrincipal.addWidget(bloqueDerecho, 2)

        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)

        self.nueva_partida()

    def nueva_partida(self):
        self.minas = set()
        self.casillas_reveladas = set()
        self.casillas_marcadas = set()
        self.minas_colocadas = False
        self.partida_terminada = False
        self.lblEstado.setText("Pulsa una casilla para empezar.")
        for boton in self.botones.values():
            boton.setText("")
            boton.setEnabled(True)

    def alternar_banderilla(self, fila, columna):
        posicion = (fila, columna)
        if (
            self.partida_terminada
            or posicion in self.casillas_reveladas
        ):
            return

        boton = self.botones[posicion]
        if posicion in self.casillas_marcadas:
            self.casillas_marcadas.remove(posicion)
            boton.setText("")
        else:
            self.casillas_marcadas.add(posicion)
            boton.setText("🚩")

    def vecinos(self, fila, columna):
        return [
            (f, c)
            for f in range(max(0, fila - 1), min(self.FILAS, fila + 2))
            for c in range(max(0, columna - 1), min(self.COLUMNAS, columna + 2))
            if (f, c) != (fila, columna)
        ]

    def colocar_minas(self, primera_fila, primera_columna):
        zonas_seguras = set(self.vecinos(primera_fila, primera_columna))
        zonas_seguras.add((primera_fila, primera_columna))
        posibles = [
            (fila, columna)
            for fila in range(self.FILAS)
            for columna in range(self.COLUMNAS)
            if (fila, columna) not in zonas_seguras
        ]
        self.minas = set(random.sample(posibles, self.NUM_MINAS))
        self.minas_colocadas = True

    def revelar_casilla(self, fila, columna):
        posicion = (fila, columna)
        if (
            self.partida_terminada
            or posicion in self.casillas_reveladas
            or posicion in self.casillas_marcadas
        ):
            return

        if not self.minas_colocadas:
            self.colocar_minas(fila, columna)

        if posicion in self.minas:
            self.botones[posicion].setText("💣")
            for ubicacion in self.minas:
                self.botones[ubicacion].setText("💣")
            for boton in self.botones.values():
                boton.setEnabled(False)
            self.partida_terminada = True
            self.lblEstado.setText("¡Has encontrado una bomba! Fin de la partida.")
            return

        pendientes = [posicion]
        while pendientes:
            actual = pendientes.pop()
            if (
                actual in self.casillas_reveladas
                or actual in self.casillas_marcadas
                or actual in self.minas
            ):
                continue

            self.casillas_reveladas.add(actual)
            num_vecinas = sum(vecino in self.minas for vecino in self.vecinos(*actual))
            boton = self.botones[actual]
            boton.setText(str(num_vecinas) if num_vecinas else "")
            boton.setEnabled(False)

            if num_vecinas == 0:
                pendientes.extend(self.vecinos(*actual))

        if len(self.casillas_reveladas) == self.FILAS * self.COLUMNAS - self.NUM_MINAS:
            self.partida_terminada = True
            for boton in self.botones.values():
                boton.setEnabled(False)
            self.lblEstado.setText("¡Has ganado!")
        else:
            self.lblEstado.setText(
                f"Casillas seguras: {len(self.casillas_reveladas)}"
            )


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Minesweeper()
    ventana.show()
    sys.exit(aplicacion.exec())
