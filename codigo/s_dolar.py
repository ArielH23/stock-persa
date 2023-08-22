from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import requests
from PyQt5.QtWidgets import QMessageBox

# ##############################################
# PRECIO DOLAR
# ##############################################


class dolar:
    def __init__(self):
        self._archi = "precio_dolar.txt"
        try:
            with open(self._archi, "r") as archi:
                desechable = archi.read()
                self.fechaprecio = desechable[
                    desechable.rfind(" ") + 1 : len(desechable)
                ]
                self.precio = float(desechable[0 : desechable.rfind(" ")])
        except FileNotFoundError:
            try:
                request = requests.get("https://www.google.com", timeout=5)
            except (requests.ConnectionError, requests.Timeout):
                msg = QMessageBox()
                msg.setWindowTitle("ERROR")
                msg.setText("¡No hay conexión a internet!")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                self.precio = 0
                self.fechaprecio = "0 / 00 / 0000"
            else:
                web_url = "https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB"
                s = Service()
                options = webdriver.ChromeOptions()
                driver = webdriver.Chrome(service=s, options=options)
                driver.get(web_url)
                driver.implicitly_wait(2)
                precio_dolar_hoy = driver.find_element(By.CLASS_NAME, "buy-value").text
                precio_dolar_hoy = precio_dolar_hoy.lstrip("$").replace(",", ".")
                self.precio = float(precio_dolar_hoy)
                fechaprecio_hoy = (
                    str(datetime.today().day)
                    + "/"
                    + str(datetime.today().month)
                    + "/"
                    + str(datetime.today().year)
                )
                self.fechaprecio = fechaprecio_hoy
                with open(self._archi, "w+") as archi:
                    archi.write(str(self.precio) + " " + str(self.fechaprecio))

    def actualizar_precio(self):
        try:
            request = requests.get("https://www.google.com", timeout=5)
        except (requests.ConnectionError, requests.Timeout):
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("¡No hay conexión a internet!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return ""
        else:
            web_url = "https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB"
            s = Service()
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=s, options=options)
            driver.get(web_url)
            driver.implicitly_wait(2)

            precio_dolar_hoy = driver.find_element(By.CLASS_NAME, "buy-value").text
            precio_dolar_hoy = precio_dolar_hoy.lstrip("$").replace(",", ".")
            self.precio = float(precio_dolar_hoy)
            fechaprecio_hoy = (
                str(datetime.today().day)
                + "/"
                + str(datetime.today().month)
                + "/"
                + str(datetime.today().year)
            )
            self.fechaprecio = fechaprecio_hoy
            with open(self._archi, "w") as archi:
                archi.write(str(self.precio) + " " + str(self.fechaprecio))
            return (
                "Precio dólar blue: $"
                + str(float(precio_dolar_hoy))
                + " Actualizado: "
                + str(fechaprecio_hoy)
            )

    def consultar_precio(self):
        return round(self.precio, 2)

    def cargar_label(self):
        label = (
            "Precio dólar blue: $"
            + str(self.precio)
            + " Actualizado: "
            + str(self.fechaprecio)
        )
        return label
