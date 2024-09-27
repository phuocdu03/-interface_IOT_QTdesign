from login import Ui
from PyQt5 import QtCore, QtGui, QtWidgets
# class login_handle(Ui_MainWindow):
#     def __init__(self, mainwindow):
#         super().__init__()
#         self.setupUi(mainwindow)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        