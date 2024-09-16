from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class miventana(QMainWindow):
    def _init_(self):
        super().__init__()
       #LINEA PARA AGREGAR ARCHIVOS DE INTERFAZ
        uic.loadUi('ventana.ui',self)

app = QApplication(sys.argv)
ventana = miventana()
ventana.show()
app.exec()
