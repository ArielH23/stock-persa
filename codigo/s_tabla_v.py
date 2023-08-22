from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QSizePolicy
from s_tabla_m import TablaModelo
from s_alta_v import Ui_VentanaAlta
from s_modificar_v import Ui_VentanaModificar
from venta_v import Ui_VentanaVenta
from historial_ventas import Ui_VentanaHistorialVentas


class Ui_VentanaStock(object):
    def setupUi(self, VentanaStock):
        self.VS = VentanaStock
        self.VS.setObjectName("VentanaStock")
        self.VS.resize(959, 795)
        self.centralwidget = QtWidgets.QWidget(self.VS)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 959, 771))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_dolar = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dolar.setFont(font)
        self.lbl_dolar.setObjectName("lbl_dolar")
        self.verticalLayout.addWidget(self.lbl_dolar)
        self.tbl_stock = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tbl_stock.setObjectName("tbl_stock")
        self.tbl_stock.setColumnCount(9)
        self.tbl_stock.setRowCount(0)
        font.setPointSize(12)
        self.tbl_stock.setFont(font)  #
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_stock.setHorizontalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.tbl_stock)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_vender = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.btn_vender.setFont(font)
        self.btn_vender.setObjectName("btn_vender")
        self.horizontalLayout_2.addWidget(self.btn_vender)
        self.btn_historialventas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.btn_historialventas.setFont(font)
        self.btn_historialventas.setObjectName("btn_historialventas")
        self.horizontalLayout_2.addWidget(self.btn_historialventas)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_agregar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout_2.addWidget(self.btn_agregar)
        self.btn_modificar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.btn_modificar.setFont(font)
        self.btn_modificar.setObjectName("btn_modificar")
        self.horizontalLayout_2.addWidget(self.btn_modificar)
        self.btn_eliminar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout_2.addWidget(self.btn_eliminar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.VS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.VS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 21))
        self.menubar.setObjectName("menubar")
        self.menuModificar_precio_d_lar = QtWidgets.QMenu(self.menubar)
        self.menuModificar_precio_d_lar.setObjectName("menuModificar_precio_d_lar")
        self.VS.setMenuBar(self.menubar)
        self.actionPrecio_dolar = QtWidgets.QAction(self.VS)
        self.actionPrecio_dolar.setObjectName("actionPrecio_dolar")
        self.menuModificar_precio_d_lar.addAction(self.actionPrecio_dolar)
        self.menubar.addAction(self.menuModificar_precio_d_lar.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.VS)

        # TABLA
        self.tbl_stock.verticalHeader().setDefaultSectionSize(110)
        self.tbl_stock.setColumnWidth(0, 40)  # ID
        # self.tbl_stock.setColumnWidth(1, 150)  # FOTO
        self.tbl_stock.setColumnWidth(2, 150)  # NOMBRE
        self.tbl_stock.setColumnWidth(3, 150)  # DESCRIPCION
        self.tbl_stock.setColumnWidth(4, 100)  # CATEGORIA
        # self.tbl_stock.setColumnWidth(5, 110)  # DOLAR
        # self.tbl_stock.setColumnWidth(6, 100)  # PESOS
        # self.tbl_stock.setColumnWidth(7, 65)  # CANTIDAD
        # self.tbl_stock.setColumnWidth(7, 65)  # FECHA

        # CLASE MODELO
        self.tm = TablaModelo(self.tbl_stock)

        self.lbl_dolar.setText(self.tm.cargar_lbl_precio())
        self.tm.cargar_datos()  # CARGA DE DATOS EN TABLA
        self.tbl_stock.cellClicked.connect(self.HabilitarBotones)  # CLICK EN LA TABLA
        self.tbl_stock.setSortingEnabled(True)

        # BOTONES
        self.btn_agregar.clicked.connect(self.AbrirVentanaAlta)
        self.btn_modificar.clicked.connect(self.AbrirVentanaModificar)
        self.btn_eliminar.clicked.connect(self.EliminarProducto)
        self.btn_vender.clicked.connect(self.AbrirVentantaVenta)
        self.btn_historialventas.clicked.connect(self.AbrirVentanaHistorialVentas)
        self.btn_modificar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self.btn_vender.setEnabled(False)
        # MENU
        self.actionPrecio_dolar.triggered.connect(self.p)

    def p(self):
        lbl_actualizado = self.tm.actualizar_precios()
        if lbl_actualizado:
            self.lbl_dolar.setText(self.tm.actualizar_precios())
            self.centralwidget.update()
        else:
            self.btn_vender.setEnabled(False)

    def HabilitarBotones(self, row):
        self.tbl_stock.selectRow(row)
        self.btn_modificar.setEnabled(True)
        self.btn_eliminar.setEnabled(True)
        self.btn_vender.setEnabled(True)
        item = self.tbl_stock.item(row, 0)
        self.id_sel = item.text()
        self.nombre_foto_sel = self.tm.ver_nombre_foto(self.id_sel)
        self.nombre_sel = self.tbl_stock.item(row, 2).text()
        self.descripcion_sel = self.tbl_stock.item(row, 3).text()
        self.categoria_sel = self.tbl_stock.item(row, 4).text()
        self.precio_dolar_sel = self.tbl_stock.item(row, 5).text().lstrip(" $")
        self.precio_pesos_sel = self.tbl_stock.item(row, 6).text().lstrip(" $")
        if self.tbl_stock.item(row, 7).text() == "AGOTADO":
            self.cantidad_sel = "0"
        else:
            self.cantidad_sel = self.tbl_stock.item(row, 7).text()

    def AbrirVentanaAlta(self):  # ALTA
        self.vent_alta = QtWidgets.QMainWindow()
        self.ui_a = Ui_VentanaAlta(self.tbl_stock)
        self.ui_a.setupUi(self.vent_alta)
        self.vent_alta.setWindowModality(QtCore.Qt.ApplicationModal)
        self.vent_alta.show()

    def AbrirVentanaModificar(self):  # MODIFICACION
        self.vent_modificar = QtWidgets.QMainWindow()
        self.ui_m = Ui_VentanaModificar(
            self.id_sel,
            self.nombre_foto_sel,
            self.nombre_sel,
            self.descripcion_sel,
            self.categoria_sel,
            self.precio_pesos_sel,
            self.cantidad_sel,
            self.tbl_stock,
        )
        self.ui_m.setupUi(self.vent_modificar)
        self.vent_modificar.setWindowModality(QtCore.Qt.ApplicationModal)
        self.vent_modificar.show()

    def EliminarProducto(self):  # BAJA
        self.tm.borrar_producto(self.id_sel)

    def AbrirVentantaVenta(self):  # VENTA
        msg = QMessageBox()
        if not self.cantidad_sel == "0":
            self.vent_venta = QtWidgets.QMainWindow()
            self.ui_v = Ui_VentanaVenta(
                self.id_sel,
                self.nombre_sel,
                self.precio_dolar_sel,
                self.cantidad_sel,
                self.tbl_stock,
            )
            self.ui_v.setupUi(self.vent_venta)
            self.vent_venta.setWindowModality(QtCore.Qt.ApplicationModal)
            self.vent_venta.show()
        else:
            msg.setWindowTitle("ERROR")
            msg.setText("¡Error al vender el producto!")
            msg.setInformativeText("La cantidad del producto está agotada")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def AbrirVentanaHistorialVentas(self):  # HISTORIAL
        self.vent_historial_venta = QtWidgets.QMainWindow()
        self.ui_hv = Ui_VentanaHistorialVentas()
        self.ui_hv.setupUi(self.vent_historial_venta)
        self.vent_historial_venta.setWindowModality(QtCore.Qt.ApplicationModal)
        self.vent_historial_venta.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.VS.setWindowTitle(_translate("VentanaStock", "MainWindow"))
        self.lbl_dolar.setText(
            _translate("VentanaStock", "Precio dólar blue:0.0 Actualizado:00/00/2000")
        )
        item = self.tbl_stock.horizontalHeaderItem(0)
        item.setText(_translate("VentanaStock", "ID"))
        item = self.tbl_stock.horizontalHeaderItem(1)
        item.setText(_translate("VentanaStock", "FOTO"))
        item = self.tbl_stock.horizontalHeaderItem(2)
        item.setText(_translate("VentanaStock", "NOMBRE"))
        item = self.tbl_stock.horizontalHeaderItem(3)
        item.setText(_translate("VentanaStock", "DESCRIPCIÓN"))
        item = self.tbl_stock.horizontalHeaderItem(4)
        item.setText(_translate("VentanaStock", "CATEGORIA"))
        item = self.tbl_stock.horizontalHeaderItem(5)
        item.setText(_translate("VentanaStock", "PRECIO DÓLAR"))
        item = self.tbl_stock.horizontalHeaderItem(6)
        item.setText(_translate("VentanaStock", "PRECIO PESOS"))
        item = self.tbl_stock.horizontalHeaderItem(7)
        item.setText(_translate("VentanaStock", "CANTIDAD"))
        item = self.tbl_stock.horizontalHeaderItem(8)
        item.setText(_translate("VentanaStock", "FECHA"))
        self.btn_vender.setText(_translate("VentanaStock", "VENDER"))
        self.btn_historialventas.setText(_translate("VentanaStock", "HISTORIAL VENTAS"))
        self.btn_agregar.setText(_translate("VentanaStock", "AGREGAR PRODUCTO"))
        self.btn_modificar.setText(_translate("VentanaStock", "MODIFICAR PRODUCTO"))
        self.btn_eliminar.setText(_translate("VentanaStock", "ELIMINAR PRODUCTO"))
        self.menuModificar_precio_d_lar.setTitle(_translate("VentanaStock", "Menú"))
        self.actionPrecio_dolar.setText(_translate("VentanaStock", "Actualizar dólar"))
