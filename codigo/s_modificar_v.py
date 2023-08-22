from PyQt5 import QtCore, QtGui, QtWidgets
from s_modificar_m import Modificar_producto
from PyQt5.QtWidgets import QMessageBox
from s_tabla_m import TablaModelo
from seleccion_foto import SeleccionImagen

# ##############################################
# VISTA MODIFICACIÓN PRODUCTO
# ##############################################


class Ui_VentanaModificar(object):
    def __init__(
        self,
        id_mod,
        foto_mod,
        nombre_mod,
        descripcion_mod,
        categoria_mod,
        precio_dolar_mod,
        cantidad_mod,
        tabla,
    ):
        self.id_mod = id_mod
        self.tabla = tabla
        self.foto_mod = foto_mod
        self.nombre_mod = nombre_mod
        self.descripcion_mod = descripcion_mod
        self.categoria_mod = categoria_mod
        self.precio_dolar_mod = precio_dolar_mod
        self.cantidad_mod = cantidad_mod

    def setupUi(self, VentanaModificar):
        self.VM = VentanaModificar
        self.VM.setObjectName("VentanaModificar")
        self.VM.resize(429, 351)  # 685, 482
        self.centralwidget = QtWidgets.QWidget(VentanaModificar)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 411, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_8.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_nombre_foto = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_nombre_foto.setFont(font)
        self.lbl_nombre_foto.setObjectName("lbl_nombre_foto")
        self.horizontalLayout_7.addWidget(self.lbl_nombre_foto)
        self.btn_seleccionar_foto = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_seleccionar_foto.setFont(font)
        self.btn_seleccionar_foto.setObjectName("btn_seleccionar_foto")
        self.horizontalLayout_7.addWidget(self.btn_seleccionar_foto)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.le_nombre = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_nombre.setFont(font)
        self.le_nombre.setText("")
        self.le_nombre.setObjectName("le_nombre")
        self.horizontalLayout_9.addWidget(self.le_nombre)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.te_descripcion = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.te_descripcion.setFont(font)
        self.te_descripcion.setObjectName("te_descripcion")
        self.horizontalLayout_10.addWidget(self.te_descripcion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.le_categoria = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_categoria.setFont(font)
        self.le_categoria.setObjectName("le_categoria")
        self.horizontalLayout_11.addWidget(self.le_categoria)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.le_cantidad = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cantidad.sizePolicy().hasHeightForWidth())
        self.le_cantidad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_cantidad.setFont(font)
        self.le_cantidad.setObjectName("le_cantidad")
        self.horizontalLayout_12.addWidget(self.le_cantidad)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_12.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.le_precio_pesos = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.le_precio_pesos.sizePolicy().hasHeightForWidth()
        )
        self.le_precio_pesos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_precio_pesos.setFont(font)
        self.le_precio_pesos.setObjectName("le_precio_pesos")
        self.horizontalLayout_13.addWidget(self.le_precio_pesos)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btn_guardar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_guardar.setFont(font)
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout_14.addWidget(self.btn_guardar)
        self.btn_cancelar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_14.addWidget(self.btn_cancelar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        VentanaModificar.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.direccion_foto = ""
        QtCore.QMetaObject.connectSlotsByName(VentanaModificar)
        self.lbl_nombre_foto.setText(self.foto_mod)
        self.le_nombre.setText(self.nombre_mod)
        self.te_descripcion.setText(self.descripcion_mod)
        self.le_categoria.setText(self.categoria_mod)
        self.le_precio_pesos.setText(self.precio_dolar_mod)
        self.le_cantidad.setText(self.cantidad_mod)
        self.btn_seleccionar_foto.clicked.connect(self.seleccion_foto)
        self.btn_guardar.clicked.connect(self.guardar_producto)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.VM.setWindowTitle(_translate("VentanaModificar", "MainWindow"))
        self.label_7.setText(_translate("VentanaModificar", "Modificar Producto"))
        self.lbl_nombre_foto.setText(_translate("VentanaModificar", "*nombre foto*"))
        self.btn_seleccionar_foto.setText(
            _translate("VentanaModificar", "seleccionar foto")
        )
        self.label_10.setText(_translate("VentanaModificar", "Nombre:      "))
        self.label_11.setText(_translate("VentanaModificar", "Descripción: "))
        self.label_12.setText(_translate("VentanaModificar", "Categoria:    "))
        self.label_13.setText(_translate("VentanaModificar", "Cantidad:     "))
        self.label_14.setText(_translate("VentanaModificar", "Precio Pesos :"))
        self.label_15.setText(_translate("VentanaModificar", "$"))
        self.btn_guardar.setText(_translate("VentanaModificar", "Guardar"))
        self.btn_cancelar.setText(_translate("VentanaModificar", "Cancelar"))

    def seleccion_foto(self):
        f = SeleccionImagen()
        direccion_foto = ""
        direccion_foto += f.foto()
        self.nombre_imagen = direccion_foto[direccion_foto.rfind("/") + 1 :]
        self.lbl_nombre_foto.setText(self.nombre_imagen)
        if direccion_foto:
            self.direccion_foto = direccion_foto
            self.btn_guardar.setEnabled(True)
        else:
            self.btn_guardar.setEnabled(False)

    def guardar_producto(self):
        mp = Modificar_producto()
        error = mp.modificar(
            self.direccion_foto,
            self.foto_mod,
            self.le_nombre.text(),
            self.te_descripcion.toPlainText(),
            self.le_categoria.text(),
            self.le_precio_pesos.text(),
            self.le_cantidad.text(),
            self.id_mod,
        )
        msg = QMessageBox()
        if error == "":
            msg.setWindowTitle("EXITO")
            msg.setText("¡Se ha modificado el producto!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            self.VM.close()
            tm = TablaModelo(self.tabla)
            tm.cargar_datos()
        else:
            msg.setWindowTitle("ERROR")
            msg.setText("¡Error al modificar el producto!")
            msg.setInformativeText(error)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
