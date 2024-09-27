from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("baicanhan2.ui",self)
        
        self.button_exit = self.findChild(QPushButton,"button_Exit")
        self.button_offAir = self.findChild(QPushButton,"button_OffAir")
        self.button_onAir = self.findChild(QPushButton,"button_OnAir")
        self.button_Off_Full = self.findChild(QPushButton,"button_Off_full")
        self.button_On_full = self.findChild(QPushButton,"buttton_On_Full")
        self.button_logout = self.findChild(QPushButton,"button_logout")
        self.horizontalSlider_AirCon = self.findChild(QSlider, "horizontalSlider_AirCon")
        self.horizontalSlider_Led = self.findChild(QSlider, "horizontalSlider_Led")
        self.label_logoUTE = self.findChild(QLabel, "label_logoUTE")


        self.label_imgAirCon = self.findChild(QLabel, "label_imgAirCon")
        self.label_img_led = self.findChild(QLabel, "label_img_led")
        self.label_valueAirCon = self.findChild(QLabel, "label_valueAirCon")


        self.button_exit.clicked.connect(self.exit)
        self.button_offAir.clicked.connect(self.offAir)
        self.button_onAir.clicked.connect(self.onAir)
        self.button_Off_Full.clicked.connect(self.Off_full)
        self.button_On_full.clicked.connect(self.On_full)
        self.button_logout.clicked.connect(self.logout)
        self.horizontalSlider_AirCon.valueChanged.connect(self.valueAirCon)
        self.horizontalSlider_Led.valueChanged.connect(self.valueLed)

        self.label_logoUTE.setStyleSheet("image: url(logo.png);")
        self.Off_full()
        self.show()


    def valueAirCon(self):
        self.label_valueAirCon.setText(str(self.horizontalSlider_AirCon.value()))

    def valueLed(self):
        value = self.horizontalSlider_Led.value()
        if(value==1): 
            self.label_img_led.setStyleSheet("image: url(1.png);")
        if(value==2): 
            self.label_img_led.setStyleSheet("image: url(2.png);")
        if(value==3): 
            self.label_img_led.setStyleSheet("image: url(3.png);")
        if(value==4): 
            self.label_img_led.setStyleSheet("image: url(4.png);")


    def logout(self):
        from login_2 import MyWindow
        self.close()
        self.ui = MyWindow()
        self.ui.show()
        # uic.loadUi("login.ui",self)
        # self.show()
    
    def exit(self):
        self.close()
        
    def offAir(self):
        self.label_imgAirCon.setStyleSheet("image: url(fan_off.png);")

    def onAir(self):
        self.label_imgAirCon.setStyleSheet("image: url(fan_running.png);")

    def Off_full(self):
        self.label_imgAirCon.setStyleSheet("image: url(fan_off.png);")
        self.label_img_led.setStyleSheet("image: url(1.png);")
        self.button_offAir.setEnabled(False)
        self.button_onAir.setEnabled(False)
        self.horizontalSlider_AirCon.setEnabled(False)
        self.horizontalSlider_Led.setEnabled(False)

    def On_full(self):
        self.label_imgAirCon.setStyleSheet("image: url(fan_running.png);")
        self.label_img_led.setStyleSheet("image: url(2.png);")
        self.button_offAir.setEnabled(True)
        self.button_onAir.setEnabled(True)
        self.horizontalSlider_AirCon.setEnabled(True)
        self.horizontalSlider_Led.setEnabled(True)
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui()
#     app.exec_()
