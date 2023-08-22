from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from s_dolar import dolar
from venta_m import Vender_producto
from s_tabla_m import TablaModelo

# ##############################################
# VISTA VENTA PRODUCTO
# ##############################################


class Ui_VentanaVenta(object):
    def __init__(self, id_sel, nombre_sel, precio_dolar_sel, cantidad_sel, tbl_stock):
        self.id = id_sel
        self.nombre = nombre_sel
        self.precio_dolar = float(precio_dolar_sel)
        self.cantidad_total = int(cantidad_sel)
        self.tabla = tbl_stock

    def setupUi(self, VentanaVenta):
        self.VV = VentanaVenta
        self.VV.setObjectName("VentanaVenta")
        self.VV.resize(652, 300)
        self.centralwidget = QtWidgets.QWidget(self.VV)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, -10, 631, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lbl_nombre = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.horizontalLayout.addWidget(self.lbl_nombre)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lbl_id = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_id.setFont(font)
        self.lbl_id.setObjectName("lbl_id")
        self.horizontalLayout.addWidget(self.lbl_id)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.le_cantidad = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cantidad.sizePolicy().hasHeightForWidth())
        self.le_cantidad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_cantidad.setFont(font)
        self.le_cantidad.setObjectName("le_cantidad")
        self.horizontalLayout_2.addWidget(self.le_cantidad)
        self.lbl_cantidadtotal = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_cantidadtotal.setFont(font)
        self.lbl_cantidadtotal.setObjectName("lbl_cantidadtotal")
        self.horizontalLayout_2.addWidget(self.lbl_cantidadtotal)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.cb_moneda = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_moneda.setFont(font)
        self.cb_moneda.setObjectName("cb_moneda")
        self.cb_moneda.addItem("")
        self.cb_moneda.addItem("")
        self.verticalLayout.addWidget(self.cb_moneda)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.le_preciototal = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_preciototal.setFont(font)
        self.le_preciototal.setObjectName("le_preciototal")
        self.horizontalLayout_3.addWidget(self.le_preciototal)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lbl_preciocadatotal = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_preciocadatotal.setFont(font)
        self.lbl_preciocadatotal.setObjectName("lbl_preciocadatotal")
        self.horizontalLayout_3.addWidget(self.lbl_preciocadatotal)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.cb_lugarventa = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_lugarventa.setFont(font)
        self.cb_lugarventa.setObjectName("cb_lugarventa")
        self.cb_lugarventa.addItem("")
        self.cb_lugarventa.addItem("")
        self.horizontalLayout_5.addWidget(self.cb_lugarventa)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem5)
        self.btn_concluirventa = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_concluirventa.setFont(font)
        self.btn_concluirventa.setObjectName("btn_concluirventa")
        self.horizontalLayout_7.addWidget(self.btn_concluirventa)
        self.btn_cancelar = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_7.addWidget(self.btn_cancelar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        VentanaVenta.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(VentanaVenta)
        self.d = dolar()
        self.tm = TablaModelo(self.tabla)

        self.lbl_id.setText(str(self.id))
        self.lbl_nombre.setText(str(self.nombre))
        self.lbl_cantidadtotal.setText("/" + str(self.cantidad_total))
        self.precios()
        self.moneda = "Dolar"
        self.cb_moneda.currentTextChanged.connect(self.precios)
        self.lugarventa = "Local"
        self.cb_lugarventa.currentIndexChanged.connect(self.lugar)
        self.btn_concluirventa.clicked.connect(self.concluirventa)

    def concluirventa(self):
        self.vm = Vender_producto(
            self.id,
            self.nombre,
            self.le_preciototal.text(),
            self.le_cantidad.text(),
            self.cantidad_total,
            self.lugarventa,
            self.moneda,
        )
        error = self.vm.comprobacion_venta()
        msg = QMessageBox()
        if error == "":
            self.vm.vender()
            self.tm.descontar_cantidad(self.id, int(self.le_cantidad.text()))
            msg.setWindowTitle("EXITO")
            msg.setText("¡Se ha concluido la venta del producto!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            self.VV.close()
        else:
            msg.setWindowTitle("ERROR")
            msg.setText("¡Error al vender el producto!")
            msg.setInformativeText(error)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def lugar(self):
        self.lugarventa = str(self.cb_lugarventa.currentText())

    def precios(self):
        if str(self.cb_moneda.currentText()) == "Peso":
            precio_peso = self.precio_dolar * self.d.consultar_precio()
            self.lbl_preciocadatotal.setText(
                "c/u: $ "
                + str(precio_peso)
                + " | "
                + "total: $ "
                + str(precio_peso * self.cantidad_total)
            )
            self.moneda = "Peso"
        else:
            self.lbl_preciocadatotal.setText(
                "c/u: $ "
                + str(self.precio_dolar)
                + " | "
                + "total: $ "
                + str(self.precio_dolar * self.cantidad_total)
            )
            self.moneda = "Dolar"
        self.centralwidget.update()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.VV.setWindowTitle(_translate("VentanaVenta", "MainWindow"))
        self.label.setText(_translate("VentanaVenta", "Venta"))
        self.label_2.setText(_translate("VentanaVenta", "Producto a vender:"))
        self.lbl_nombre.setText(_translate("VentanaVenta", "*nombre*"))
        self.label_4.setText(_translate("VentanaVenta", "ID:"))
        self.lbl_id.setText(_translate("VentanaVenta", "*ID*"))
        self.label_3.setText(_translate("VentanaVenta", "Cantidad a vender:"))
        self.lbl_cantidadtotal.setText(_translate("VentanaVenta", "/000"))
        self.label_9.setText(_translate("VentanaVenta", "Moneda"))
        self.cb_moneda.setItemText(0, _translate("VentanaVenta", "Dolar"))
        self.cb_moneda.setItemText(1, _translate("VentanaVenta", "Peso"))
        self.label_5.setText(_translate("VentanaVenta", "Precio total:"))
        self.label_6.setText(_translate("VentanaVenta", "Precio:"))
        self.lbl_preciocadatotal.setText(
            _translate("VentanaVenta", "*c/u:00000 | total:000000*")
        )
        self.label_7.setText(_translate("VentanaVenta", "Lugar de venta:"))
        self.cb_lugarventa.setItemText(0, _translate("VentanaVenta", "Local"))
        self.cb_lugarventa.setItemText(1, _translate("VentanaVenta", "Online"))
        self.btn_concluirventa.setText(_translate("VentanaVenta", "Concluir venta"))
        self.btn_cancelar.setText(_translate("VentanaVenta", "Cancelar"))
