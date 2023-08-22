from PyQt5 import QtCore, QtGui, QtWidgets
from s_alta_m import Alta_producto
from PyQt5.QtWidgets import QMessageBox
from s_tabla_m import TablaModelo
from seleccion_foto import SeleccionImagen

# ##############################################
# VISTA ALTA PRODUCTO
# ##############################################


class Ui_VentanaAlta(object):
    def __init__(self, tabla):
        self.tabla = tabla

    def setupUi(self, VentanaAlta):
        self.VA = VentanaAlta
        self.VA.setObjectName("VentanaAlta")
        self.VA.resize(433, 358)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VA.sizePolicy().hasHeightForWidth())
        self.VA.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(self.VA)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_nombre = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_nombre.setFont(font)
        self.le_nombre.setText("")
        self.le_nombre.setObjectName("le_nombre")
        self.horizontalLayout.addWidget(self.le_nombre)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.te_descripcion = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.te_descripcion.setFont(font)
        self.te_descripcion.setObjectName("te_descripcion")
        self.horizontalLayout_3.addWidget(self.te_descripcion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.le_categoria = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_categoria.setFont(font)
        self.le_categoria.setObjectName("le_categoria")
        self.horizontalLayout_2.addWidget(self.le_categoria)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
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
        self.horizontalLayout_6.addWidget(self.le_cantidad)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
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
        self.horizontalLayout_4.addWidget(self.le_precio_pesos)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_guardar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_guardar.setFont(font)
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout_5.addWidget(self.btn_guardar)
        self.btn_cancelar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_5.addWidget(self.btn_cancelar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.VA.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.VA)

        self.btn_cancelar.clicked.connect(lambda: self.VA.close())
        self.btn_seleccionar_foto.clicked.connect(self.seleccion_foto)
        self.btn_guardar.setEnabled(False)
        self.btn_guardar.clicked.connect(self.guardar_producto)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.VA.setWindowTitle(_translate("VentanaAlta", "MainWindow"))
        self.label_7.setText(_translate("VentanaAlta", "Nuevo Producto"))
        self.lbl_nombre_foto.setText(_translate("VentanaAlta", "*nombre foto*"))
        self.btn_seleccionar_foto.setText(_translate("VentanaAlta", "Seleccionar foto"))
        self.label.setText(_translate("VentanaAlta", "Nombre:      "))
        self.label_3.setText(_translate("VentanaAlta", "Descripción: "))
        self.label_2.setText(_translate("VentanaAlta", "Categoria:    "))
        self.label_6.setText(_translate("VentanaAlta", "Cantidad:     "))
        self.label_4.setText(_translate("VentanaAlta", "Precio Pesos :"))
        self.label_5.setText(_translate("VentanaAlta", "$"))
        self.btn_guardar.setText(_translate("VentanaAlta", "Guardar"))
        self.btn_cancelar.setText(_translate("VentanaAlta", "Cancelar"))

    def seleccion_foto(self):
        f = SeleccionImagen()
        direccion_foto = ""
        direccion_foto += f.foto()
        self.nombre_imagen = direccion_foto[direccion_foto.rfind("/") + 1 :]
        self.lbl_nombre_foto.setText(self.nombre_imagen)
        if direccion_foto:
            self.direccion_foto = direccion_foto
            self.btn_guardar.setEnabled(True)

    def guardar_producto(self):
        ap = Alta_producto()
        error = ap.alta(
            self.direccion_foto,
            self.nombre_imagen,
            self.le_nombre.text(),
            self.te_descripcion.toPlainText(),
            self.le_categoria.text(),
            self.le_precio_pesos.text(),
            self.le_cantidad.text(),
        )
        msg = QMessageBox()
        if error == "":
            msg.setWindowTitle("EXITO")
            msg.setText("¡Se ha agregado un nuevo producto!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            self.VA.close()
            tm = TablaModelo(self.tabla)
            tm.cargar_datos()
        else:
            msg.setWindowTitle("ERROR")
            msg.setText("¡Error al agregar un nuevo producto!")
            msg.setInformativeText(error)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
