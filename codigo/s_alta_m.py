from peewee import *
import re
from datetime import datetime
import os
import sys

# ##############################################
# MODELO ALTA PRODUCTO
# ##############################################

db = SqliteDatabase("listado_productos.db")


class BaseModel(Model):
    class Meta:
        database = db


class productos(BaseModel):  # Esta es la tabla
    foto = BlobField()
    nombre_foto = CharField()
    nombre = CharField()
    descripcion = CharField()
    categoria = CharField()
    precio_pesos = DoubleField()
    cantidad = IntegerField()
    fecha = CharField()


db.connect()  # se conecta a la base
db.create_tables([productos])  # se crea la tabla


class Alta_producto:
    # COMPROBACIONES
    def comprobacion_alta(
        self,
        nombre,
        descripcion,
        categoria,
        precio_dolar,
        cantidad,
    ):
        error = ""
        patron_nro = "^[0-9\.]*$"
        patron = "^[A-Za-záéíóú\s]*$"

        if (
            nombre == ""
            or descripcion == ""
            or categoria == ""
            or precio_dolar == ""
            or cantidad == ""
        ):
            if nombre == "":
                error += "Falta ingresar Nombre del producto\n"
            if descripcion == "":
                error += "Falta ingresar Descripción del producto\n"
            if precio_dolar == "":
                error += "Falta ingresar el precio en dolares del producto\n"
            if cantidad == "":
                error += "Falta ingresar la cantidad del producto\n"
            return error
        else:
            if not re.match(patron, str(nombre)):  # Comprobación Nombre producto
                error += "Nombre: solo letras\n"
            else:
                for (
                    fila
                ) in productos.select():  # que no se repita el nombre del producto
                    if nombre == fila.nombre:
                        error += "Nombre: repetido\n"
                        break

            if not re.match(patron, str(categoria)):  # Comprobación Categoria producto
                error += "Categoria: solo letras\n"

            if not re.match(
                patron_nro, str(precio_dolar)
            ):  # Comprobación Precio producto
                error += "Precio pesos: solo numeros\n"

            if not re.match(
                patron_nro, str(cantidad)
            ):  # Comprobación Cantidad producto
                error += "Cantidad: solo numeros\n"

        return error

    def alta(
        self,
        direccion_foto_p,
        nombre_foto_p,
        nombre_p,
        descripcion_p,
        categoria_p,
        precio_pesos_p,
        cantidad_p,
    ):
        error = ""
        error += self.comprobacion_alta(
            nombre_p,
            descripcion_p,
            categoria_p,
            precio_pesos_p,
            cantidad_p,
        )
        if not error:
            foto_p = open(
                direccion_foto_p,
                "rb",
            ).read()
            nombre = nombre_p
            descripcion = descripcion_p
            categoria = categoria_p
            precio_pesos = float(precio_pesos_p)
            cantidad = int(float(cantidad_p))
            producto = productos()
            producto.foto = foto_p
            producto.nombre_foto = nombre_foto_p
            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.categoria = categoria
            producto.precio_pesos = precio_pesos
            producto.fecha = (
                str(datetime.today().day)
                + "/"
                + str(datetime.today().month)
                + "/"
                + str(datetime.today().year)
            )
            producto.cantidad = cantidad
            producto.save()
        return error
