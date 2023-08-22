import re
from peewee import *
from s_dolar import dolar
from datetime import datetime

# ##############################################
# MODELO VENTA PRODUCTO
# ##############################################

db = SqliteDatabase("historial_ventas.db")


class BaseModel(Model):
    class Meta:
        database = db


class productos_vendidos(BaseModel):  # Esta es la tabla
    nombre = CharField()
    precio_dolar_total = DoubleField()
    precio_pesos_total = DoubleField()
    cantidad = IntegerField()
    lugarventa = CharField()
    fecha = CharField()


db.connect()  # se conecta a la base
db.create_tables([productos_vendidos])


class Vender_producto:
    def __init__(
        self,
        id,
        nombre,
        precio_total,
        cantidad_venta,
        cantidad_total,
        lugarventa,
        moneda,
    ):
        self.id = id
        self.nombre = nombre
        self.precio_total = precio_total
        self.cantidad_venta = cantidad_venta
        self.cantidad_total = cantidad_total
        self.lugarventa = lugarventa
        self.moneda = moneda
        self.d = dolar()

    def comprobacion_venta(self):
        error = ""
        patron_nro = "^-?[0-9]\d*(\.\d+)?$"
        if self.cantidad_venta == "":
            error += "Falta ingresar la cantidad\n"
        else:
            if not re.match(patron_nro, str(self.cantidad_venta)):
                error += "Cantidad invalida solo numeros\n"
            else:
                self.cantidad_venta = int(float(self.cantidad_venta))
                if self.cantidad_venta < 0:
                    error += "Cantidad invalida (" + str(self.cantidad_venta) + "<0)\n"
                if self.cantidad_venta == 0:
                    error += "Cantidad invalida (" + str(self.cantidad_venta) + "==0)\n"
                if self.cantidad_venta > self.cantidad_total:
                    error += "Cantidad exede la cantidad del producto disponible\n"
        if self.precio_total == "":
            error += "Falta ingresar el precio total\n"
        else:
            if not re.match(patron_nro, str(self.precio_total)):
                error += "Precio total invalido solo numeros\n"
            else:
                self.precio_total = float(self.precio_total)
                if self.precio_total < 0:
                    error += (
                        "Precio total invalido (" + str(self.precio_total) + "<0)\n"
                    )
                if self.precio_total == 0:
                    error += (
                        "Precio total invalido (" + str(self.precio_total) + "==0)\n"
                    )
        return error

    def vender(self):
        producto_vendido = productos_vendidos()
        producto_vendido.nombre = self.nombre
        if self.moneda == "Dolar":
            producto_vendido.precio_dolar_total = self.precio_total
            producto_vendido.precio_pesos_total = round(
                self.precio_total * self.d.consultar_precio(), 2
            )
        else:
            producto_vendido.precio_pesos_total = self.precio_total
            producto_vendido.precio_dolar_total = round(
                self.precio_total / self.d.consultar_precio(), 2
            )
        producto_vendido.cantidad = self.cantidad_venta
        producto_vendido.lugarventa = self.lugarventa
        producto_vendido.fecha = (
            str(datetime.today().day)
            + "/"
            + str(datetime.today().month)
            + "/"
            + str(datetime.today().year)
        )
        producto_vendido.save()
