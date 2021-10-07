from PyQt5 import QtCore, QtGui, QtWidgets
from menu_ae import Ui_Main_AE
from menu_fj import Ui_Main_FJ
from menu_ko import Ui_Main_KO
from menu_pt import Ui_Main_PT
from menu_uz import Ui_Main_UZ

class Ui_Main_Menu(object):

        def open_ae(self):
                self.ae = QtWidgets.QMainWindow()
                self.ui = Ui_Main_AE()
                self.ui.setupUi(self.ae)
                self.ae.show()
        
        def open_fj(self):
                self.fj = QtWidgets.QMainWindow()
                self.ui = Ui_Main_FJ()
                self.ui.setupUi(self.fj)
                self.fj.show()
        
        def open_ko(self):
                self.ko = QtWidgets.QMainWindow()
                self.ui = Ui_Main_KO()
                self.ui.setupUi(self.ko)
                self.ko.show()
        
        def open_pt(self):
                self.pt = QtWidgets.QMainWindow()
                self.ui = Ui_Main_PT()
                self.ui.setupUi(self.pt)
                self.pt.show()
        
        def open_uz(self):
                self.uz = QtWidgets.QMainWindow()
                self.ui = Ui_Main_UZ()
                self.ui.setupUi(self.uz)
                self.uz.show()

        def setupUi(self, Main_Menu):
                Main_Menu.setObjectName("Main_Menu")
                Main_Menu.resize(1920, 1080)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/image/Picture/cards.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                Main_Menu.setWindowIcon(icon)
                Main_Menu.setStyleSheet("background-image: url(:/image/Picture/main_menu.jpg);")
                self.centralwidget = QtWidgets.QWidget(Main_Menu)
                self.centralwidget.setObjectName("centralwidget")
                self.btn_AE = QtWidgets.QPushButton(self.centralwidget)
                self.btn_AE.setGeometry(QtCore.QRect(760, 320, 296, 181))
                self.btn_AE.setStyleSheet("QPushButton{\n"
        "    background:transparent;\n"
        "    background-image: url(:/image/Picture/btn_ae.png);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #8DC68F;\n"
        "}")
                self.btn_AE.setText("")
                self.btn_AE.setObjectName("btn_AE")
                self.btn_FJ = QtWidgets.QPushButton(self.centralwidget)
                self.btn_FJ.setGeometry(QtCore.QRect(1100, 320, 296, 181))
                self.btn_FJ.setStyleSheet("QPushButton{\n"
        "    background:transparent;\n"
        "    background-image: url(:/image/Picture/btn_fj.png);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #8DC68F;\n"
        "}")
                self.btn_FJ.setText("")
                self.btn_FJ.setObjectName("btn_FJ")
                self.btn_KO = QtWidgets.QPushButton(self.centralwidget)
                self.btn_KO.setGeometry(QtCore.QRect(1440, 320, 296, 181))
                self.btn_KO.setStyleSheet("QPushButton{\n"
        "    background:transparent;\n"
        "    background-image: url(:/image/Picture/btn_ko.png);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #8DC68F;\n"
        "}")
                self.btn_KO.setText("")
                self.btn_KO.setObjectName("btn_KO")
                self.btn_PT = QtWidgets.QPushButton(self.centralwidget)
                self.btn_PT.setGeometry(QtCore.QRect(940, 620, 296, 181))
                self.btn_PT.setStyleSheet("QPushButton{\n"
        "    background:transparent;\n"
        "    background-image: url(:/image/Picture/btn_pt.png);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #8DC68F;\n"
        "}")
                self.btn_PT.setText("")
                self.btn_PT.setObjectName("btn_PT")
                self.btn_UZ = QtWidgets.QPushButton(self.centralwidget)
                self.btn_UZ.setGeometry(QtCore.QRect(1300, 620, 296, 181))
                self.btn_UZ.setStyleSheet("QPushButton{\n"
        "    background:transparent;\n"
        "    background-image: url(:/image/Picture/btn_uz.png);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #8DC68F;\n"
        "}")
                self.btn_UZ.setText("")
                self.btn_UZ.setObjectName("btn_UZ")
                Main_Menu.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(Main_Menu)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
                self.menubar.setObjectName("menubar")
                Main_Menu.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(Main_Menu)
                self.statusbar.setObjectName("statusbar")
                Main_Menu.setStatusBar(self.statusbar)

                self.btn_AE.clicked.connect(self.open_ae)
                self.btn_AE.clicked.connect(Main_Menu.hide)
                self.btn_FJ.clicked.connect(self.open_fj)
                self.btn_FJ.clicked.connect(Main_Menu.hide)
                self.btn_KO.clicked.connect(self.open_ko)
                self.btn_KO.clicked.connect(Main_Menu.hide)
                self.btn_PT.clicked.connect(self.open_pt)
                self.btn_PT.clicked.connect(Main_Menu.hide)
                self.btn_UZ.clicked.connect(self.open_uz)
                self.btn_UZ.clicked.connect(Main_Menu.hide)

                self.retranslateUi(Main_Menu)
                QtCore.QMetaObject.connectSlotsByName(Main_Menu)

        def retranslateUi(self, Main_Menu):
                _translate = QtCore.QCoreApplication.translate
                Main_Menu.setWindowTitle(_translate("Main_Menu", "MainMenu"))
                
import vocab_pic1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Menu = QtWidgets.QMainWindow()
    ui = Ui_Main_Menu()
    ui.setupUi(Main_Menu)
    Main_Menu.show()
    sys.exit(app.exec_())
