from s_tabla_v import Ui_VentanaStock
from PyQt5 import QtWidgets

# ##############################################
# CONTROLADOR
# ##############################################

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    VentanaStock = QtWidgets.QMainWindow()
    ui = Ui_VentanaStock()
    ui.setupUi(VentanaStock)
    VentanaStock.show()
    sys.exit(app.exec_())
