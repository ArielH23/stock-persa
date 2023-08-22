from peewee import *
from PyQt5 import QtWidgets, QtGui, QtCore
from s_dolar import dolar

# ##############################################
# MODELO TABLA PRODUCTOS
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


class TablaModelo:
    def __init__(self, tabla) -> None:
        self.tabla = tabla
        self.d = dolar()

    def cargar_datos(self):
        fila = 0
        self.tabla.setRowCount(productos.select().count())
        precio_dolar = self.d.consultar_precio()
        for producto in productos.select().order_by(productos.id.asc()):
            self.tabla.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(producto.id)))
            # FOTO
            qimg = QtGui.QPixmap()
            foto_ = QtWidgets.QLabel()
            if qimg.loadFromData(producto.foto):
                foto_.setPixmap(qimg)
                foto_.setScaledContents(True)
                self.tabla.setCellWidget(fila, 1, foto_)
            #
            self.tabla.setItem(
                fila, 2, QtWidgets.QTableWidgetItem(producto.nombre)
            )  # NOMBRE
            self.tabla.setItem(
                fila, 3, QtWidgets.QTableWidgetItem(producto.descripcion)  # DESCRIPCION
            )
            self.tabla.setItem(
                fila, 4, QtWidgets.QTableWidgetItem(producto.categoria)
            )  # CATEGORIA
            if precio_dolar != 0:
                self.tabla.setItem(
                    fila,
                    5,
                    QtWidgets.QTableWidgetItem(
                        "$ "
                        + str(
                            round(producto.precio_pesos / self.d.consultar_precio(), 2)
                        )
                    ),  # PRECIO DOLAR
                )
            else:
                self.tabla.setItem(
                    fila,
                    5,
                    QtWidgets.QTableWidgetItem("Falta precio dólar"),  # PRECIO DOLAR
                )
            self.tabla.setItem(
                fila,
                6,
                QtWidgets.QTableWidgetItem(
                    "$ " + str(producto.precio_pesos)  # PRECIO PESOS
                ),
            )
            # CANTIDAD
            if producto.cantidad == 0:
                self.tabla.setItem(fila, 7, QtWidgets.QTableWidgetItem("AGOTADO"))
            else:
                self.tabla.setItem(
                    fila, 7, QtWidgets.QTableWidgetItem(str(producto.cantidad))
                )
            #
            self.tabla.setItem(
                fila, 8, QtWidgets.QTableWidgetItem(producto.fecha)
            )  # FECHA
            fila += 1

    def cargar_lbl_precio(self):
        return self.d.cargar_label()

    def actualizar_precios(self):
        lbl_actualizado = self.d.actualizar_precio()
        if lbl_actualizado:
            self.tabla.setRowCount(productos.select().count())
            fila = 0
            for producto in productos.select().order_by(productos.id.asc()):
                self.tabla.setItem(
                    fila,
                    6,
                    QtWidgets.QTableWidgetItem(
                        "$ "
                        + str(
                            round(producto.precio_dolar * self.d.consultar_precio(), 2)
                        )
                    ),
                )
                fila += 1
            return lbl_actualizado
        else:
            return ""

    def descontar_cantidad(self, id_modificar, cantidad_venta):
        prod = productos.get(productos.id == id_modificar)
        cantidad_restante = prod.cantidad - cantidad_venta
        prod.cantidad = cantidad_restante
        prod.save()
        self.cargar_datos()

    def borrar_producto(self, id_borrar):
        id_borrar
        borrar = productos.get(productos.id == id_borrar)
        borrar.delete_instance()  # borra el registro
        self.cargar_datos()

    def ver_nombre_foto(self, id_mod):
        for producto in productos.select().order_by(productos.id.asc()):
            if producto.id == int(id_mod):
                return str(producto.nombre_foto)
