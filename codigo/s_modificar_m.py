from peewee import *
import re
from datetime import datetime
import os
import sys

# ##############################################
# MODELO MODIFICACIÓN PRODUCTO
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


class Modificar_producto:
    def comprobacion_modificar(
        self,
        nombre,
        descripcion,
        categoria,
        precio_pesos,
        cantidad,
        id_mod,
    ):
        error = ""
        patron_nro = "^[0-9\.]*$"
        patron = "^[A-Za-záéíóú\s]*$"

        if (
            nombre == ""
            or descripcion == ""
            or categoria == ""
            or precio_pesos == ""
            or cantidad == ""
        ):
            if nombre == "":
                error += "Falta ingresar Nombre del producto\n"
            if descripcion == "":
                error += "Falta ingresar Descripción del producto\n"
            if precio_pesos == "":
                error += "Falta ingresar el precio en dolares del producto\n"
            if cantidad == "":
                error += "Falta ingresar la cantidad del producto\n"
            return error
        else:
            if not re.match(patron, str(nombre)):  # Comprobación Nombre producto
                error += "Nombre: solo letras\n"
            else:
                for fila in productos.select():
                    if nombre == fila.nombre and fila.id == id_mod:
                        error += "Nombre repetido\n"
                        break

            if not re.match(patron, str(categoria)):  # Comprobación Categoria producto
                error += "Categoria: solo numeros\n"

            if not re.match(patron_nro, str(precio_pesos)):
                error += "Precio dólar: solo numeros\n"

            if not re.match(patron_nro, str(cantidad)):
                error += "Cantidad: solo numeros\n"

        return error

    def modificar(
        self,
        direccion_foto_p,
        nombre_foto_p,
        nombre_p,
        descripcion_p,
        categoria_p,
        precio_pesos_p,
        cantidad_p,
        id_mod,
    ):
        error = self.comprobacion_modificar(
            nombre_p,
            descripcion_p,
            categoria_p,
            precio_pesos_p,
            cantidad_p,
            id_mod,
        )
        if not error:
            if direccion_foto_p:
                actualizar = productos.update(
                    foto=open(
                        direccion_foto_p,
                        "rb",
                    ).read(),
                    nombre_foto=nombre_foto_p,
                    nombre=nombre_p,
                    descripcion=descripcion_p,
                    categoria=categoria_p,
                    precio_pesos=float(precio_pesos_p),
                    cantidad=int(float(cantidad_p)),
                    fecha=(
                        str(datetime.today().day)
                        + "/"
                        + str(datetime.today().month)
                        + "/"
                        + str(datetime.today().year)
                    ),
                ).where(productos.id == id_mod)
                actualizar.execute()
            else:
                actualizar = productos.update(
                    nombre_foto=nombre_foto_p,
                    nombre=nombre_p,
                    descripcion=descripcion_p,
                    categoria=categoria_p,
                    precio_pesos=float(precio_pesos_p),
                    cantidad=int(float(cantidad_p)),
                    fecha=(
                        str(datetime.today().day)
                        + "/"
                        + str(datetime.today().month)
                        + "/"
                        + str(datetime.today().year)
                    ),
                ).where(productos.id == id_mod)
                actualizar.execute()
            return error
        else:
            return error
