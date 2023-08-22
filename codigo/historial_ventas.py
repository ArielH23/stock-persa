from PyQt5 import QtCore, QtGui, QtWidgets
from peewee import *

# ##############################################
# MODELO Y VISTA HISTORIAL VENTAS PRODUCTOS
# ##############################################

db = SqliteDatabase("historial_ventas.db")


class BaseModel(Model):
    class Meta:
        database = db


class productos_vendidos(BaseModel):  # Esta es la tabla_hv
    nombre = CharField()
    precio_dolar_total = DoubleField()
    precio_pesos_total = DoubleField()
    cantidad = IntegerField()
    lugarventa = CharField()
    fecha = CharField()


class Ui_VentanaHistorialVentas(object):
    def setupUi(self, VentanaHistorialVentas):
        self.VH = VentanaHistorialVentas
        self.VH.setObjectName("VentanaHistorialVentas")
        self.VH.resize(677, 614)
        self.centralwidget = QtWidgets.QWidget(self.VH)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 657, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabla_hv = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tabla_hv.setObjectName("tabla_hv")
        self.tabla_hv.setColumnCount(7)
        self.tabla_hv.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_hv.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_hv.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_hv.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_hv.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_hv.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_hv.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_hv.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tabla_hv)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_cerrar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cerrar.setFont(font)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout_2.addWidget(self.btn_cerrar)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.VH.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.VH)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menubar.setObjectName("menubar")
        self.VH.setMenuBar(self.menubar)

        self.retranslateUi(self.VH)
        QtCore.QMetaObject.connectSlotsByName(self.VH)
        self.tabla_hv.setSortingEnabled(True)

        self.cargar_datos()
        self.btn_cerrar.clicked.connect(lambda: self.VH.close())

    def cargar_datos(self):
        fila = 0
        self.tabla_hv.setRowCount(productos_vendidos.select().count())
        for producto_vendido in productos_vendidos.select().order_by(
            productos_vendidos.id.asc()
        ):
            self.tabla_hv.setItem(
                fila, 0, QtWidgets.QTableWidgetItem(str(producto_vendido.id))
            )  # ID
            self.tabla_hv.setItem(
                fila, 1, QtWidgets.QTableWidgetItem(producto_vendido.nombre)
            )  # NOMBRE
            self.tabla_hv.setItem(
                fila,
                2,
                QtWidgets.QTableWidgetItem(str(producto_vendido.cantidad)),
            )  # CANTIDAD
            self.tabla_hv.setItem(
                fila,
                3,
                QtWidgets.QTableWidgetItem(
                    "$ " + str(producto_vendido.precio_dolar_total)
                ),
            )  # PRECIO DOLAR
            self.tabla_hv.setItem(
                fila,
                4,
                QtWidgets.QTableWidgetItem(
                    "$ " + str(producto_vendido.precio_pesos_total)
                ),
            )  # PRECIO PESOS
            self.tabla_hv.setItem(
                fila, 5, QtWidgets.QTableWidgetItem(producto_vendido.lugarventa)
            )  # LUGAR VENTA
            self.tabla_hv.setItem(
                fila, 6, QtWidgets.QTableWidgetItem(producto_vendido.fecha)
            )  # FECHA
            fila += 1
        self.tabla_hv.setColumnWidth(0, 40)  # ID
        self.tabla_hv.setColumnWidth(1, 100)  # NOMBRE
        self.tabla_hv.setColumnWidth(2, 80)  # CANTIDAD
        self.tabla_hv.setColumnWidth(3, 130)  # PRECIO DOLAR
        self.tabla_hv.setColumnWidth(4, 100)  # PRECIO PESOS
        self.tabla_hv.setColumnWidth(5, 110)  # LUGAR VENTA
        self.tabla_hv.setColumnWidth(6, 80)  # FECHA

    def retranslateUi(self, VentanaHistorialVentas):
        _translate = QtCore.QCoreApplication.translate
        VentanaHistorialVentas.setWindowTitle(
            _translate("VentanaHistorialVentas", "MainWindow")
        )
        self.label.setText(_translate("VentanaHistorialVentas", "HISTORIAL VENTAS"))
        item = self.tabla_hv.horizontalHeaderItem(0)
        item.setText(_translate("VentanaHistorialVentas", "ID"))
        item = self.tabla_hv.horizontalHeaderItem(1)
        item.setText(_translate("VentanaHistorialVentas", "NOMBRE"))
        item = self.tabla_hv.horizontalHeaderItem(2)
        item.setText(_translate("VentanaHistorialVentas", "CANTIDAD"))
        item = self.tabla_hv.horizontalHeaderItem(3)
        item.setText(_translate("VentanaHistorialVentas", "PRECIO DOLAR"))
        item = self.tabla_hv.horizontalHeaderItem(4)
        item.setText(_translate("VentanaHistorialVentas", "PRECIO PESOS"))
        item = self.tabla_hv.horizontalHeaderItem(5)
        item.setText(_translate("VentanaHistorialVentas", "LUGAR VENTA"))
        item = self.tabla_hv.horizontalHeaderItem(6)
        item.setText(_translate("VentanaHistorialVentas", "FECHA"))
        self.btn_cerrar.setText(_translate("VentanaHistorialVentas", "CERRAR"))
