from PyQt5.QtWidgets import (QApplication,QWidget
                             ,QApplication)
import sys

class vprincipal(QApplication):
    def _init_(self):
        super().__init__()
        boton = QPushButton("Haz click")
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_click)
        self.setWindowTitle("Mi primera ventana hijos de la madre")
        self.setGeometry(100,100,200,200)
        self.setCentralWidget(boton)

    def boton_click(self):
        print("Haz hecho click")

app = QApplication(sys.argv)
ventana = QWidget()
ventana.show()
app.exec()
