from PyQt5.QtWidgets import *
from PyQt5 import uic 
from baicanhan2 import Ui
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("login.ui",self)
        self.lineID = self.findChild(QLineEdit,"lineID")
        self.linePass = self.findChild(QLineEdit,"linePQ")
        self.buttonLogin = self.findChild(QPushButton,"button_login")
        self.buttonCancel = self.findChild(QPushButton,"button_cancel")
        self.show()
        self.buttonLogin.clicked.connect(self.login)
        self.buttonCancel.clicked.connect(self.cancel)
    def login(self):
        ID = self.lineID.text()
        Pass = self.linePass.text()
        if ID == "admin" and Pass == "admin":
            self.close()
            self.ui = Ui()
            self.ui.show()
        else:
            QMessageBox.warning(self,"Login","ID or Password is incorrect")

    def cancel(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
