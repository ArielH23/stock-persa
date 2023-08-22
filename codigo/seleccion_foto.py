from PyQt5.QtWidgets import QMainWindow, QFileDialog
import os
import sys


class SeleccionImagen(QMainWindow):
    def foto(self):
        if os.name == "nt":
            if getattr(sys, "frozen", False):
                anombre = QFileDialog.getOpenFileName(
                    self,
                    "Abrir foto",
                    str(os.path.dirname(sys.argv[0]) + "\\fotos\\"),
                    "Imagen (*.png *.jpg *.jpeg)",
                )
            elif __file__:
                anombre = QFileDialog.getOpenFileName(
                    self,
                    "Abrir foto",
                    str(os.path.dirname(os.path.abspath(__file__)) + "\\fotos\\"),
                    "Imagen (*.png *.jpg *.jpeg)",
                )
            if anombre:
                return anombre[0]
        else:
            if getattr(sys, "frozen", False):
                anombre = QFileDialog.getOpenFileName(
                    self,
                    "Abrir foto",
                    str(os.path.dirname(sys.argv[0]) + "/fotos/"),
                    "Imagen (*.png *.jpg *.jpeg)",
                )
            elif __file__:
                anombre = QFileDialog.getOpenFileName(
                    self,
                    "Abrir foto",
                    str(os.path.dirname(os.path.abspath(__file__)) + "/fotos/"),
                    "Imagen (*.png *.jpg *.jpeg)",
                )
            if anombre:
                return anombre[0]
