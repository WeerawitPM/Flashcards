# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Flashcards\Flashcards\ui\menu_ae.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_AE(object):
    def setupUi(self, Main_AE):
        Main_AE.setObjectName("Main_AE")
        Main_AE.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/Picture/cards.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main_AE.setWindowIcon(icon)
        Main_AE.setStyleSheet("background-image: url(:/image/Picture/a_e.jpg);")
        self.centralwidget = QtWidgets.QWidget(Main_AE)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setGeometry(QtCore.QRect(1200, 220, 88, 88))
        self.btn_play.setStyleSheet("background-image: url(:/image/Picture/play.png);")
        self.btn_play.setText("")
        self.btn_play.setIconSize(QtCore.QSize(20, 20))
        self.btn_play.setAutoDefault(False)
        self.btn_play.setDefault(False)
        self.btn_play.setFlat(True)
        self.btn_play.setObjectName("btn_play")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(1200, 400, 85, 96))
        self.btn_save.setStyleSheet("background-image: url(:/image/Picture/add.png);")
        self.btn_save.setText("")
        self.btn_save.setIconSize(QtCore.QSize(20, 20))
        self.btn_save.setAutoDefault(False)
        self.btn_save.setDefault(False)
        self.btn_save.setFlat(True)
        self.btn_save.setObjectName("btn_save")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(1200, 660, 79, 96))
        self.btn_delete.setStyleSheet("background-image: url(:/image/Picture/bin.png);")
        self.btn_delete.setText("")
        self.btn_delete.setIconSize(QtCore.QSize(20, 20))
        self.btn_delete.setAutoDefault(False)
        self.btn_delete.setDefault(False)
        self.btn_delete.setFlat(True)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_play2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play2.setGeometry(QtCore.QRect(1300, 230, 161, 81))
        self.btn_play2.setStyleSheet("font: 35pt \"Mitr SemiBold\";\n"
"background: transparent;")
        self.btn_play2.setAutoRepeat(False)
        self.btn_play2.setDefault(False)
        self.btn_play2.setFlat(True)
        self.btn_play2.setObjectName("btn_play2")
        self.btn_save2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save2.setGeometry(QtCore.QRect(1310, 430, 311, 81))
        self.btn_save2.setStyleSheet("font: 35pt \"Mitr SemiBold\";\n"
"background: transparent;")
        self.btn_save2.setDefault(False)
        self.btn_save2.setFlat(True)
        self.btn_save2.setObjectName("btn_save2")
        self.btn_delete2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete2.setGeometry(QtCore.QRect(1310, 680, 211, 81))
        self.btn_delete2.setStyleSheet("font: 35pt \"Mitr SemiBold\";\n"
"background: transparent;")
        self.btn_delete2.setDefault(False)
        self.btn_delete2.setFlat(True)
        self.btn_delete2.setObjectName("btn_delete2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 110, 241, 71))
        self.label.setStyleSheet("font: 30pt \"Mitr SemiBold\";\n"
"background: transparent;")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 330, 951, 491))
        self.plainTextEdit.setStyleSheet("font: 15pt \"Mitr SemiBold\";\n"
"background: #dedede;")
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setBackgroundVisible(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_show = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show.setGeometry(QtCore.QRect(500, 840, 171, 61))
        self.btn_show.setStyleSheet("font: 25pt \"Mitr SemiBold\";\n"
"color: rgb(255, 255, 255);\n"
"background: #e84c89;")
        self.btn_show.setObjectName("btn_show")
        self.textbox_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_delete.setGeometry(QtCore.QRect(1185, 813, 591, 60))
        self.textbox_delete.setStyleSheet("font: 20pt \"Mitr SemiBold\";\n"
"background: transparent")
        self.textbox_delete.setText("")
        self.textbox_delete.setFrame(False)
        self.textbox_delete.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textbox_delete.setObjectName("textbox_delete")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(983, 210, 69, 69))
        self.btn_search.setStyleSheet("background-image: url(:/image/Picture/search.png);")
        self.btn_search.setText("")
        self.btn_search.setIconSize(QtCore.QSize(20, 20))
        self.btn_search.setAutoDefault(False)
        self.btn_search.setDefault(False)
        self.btn_search.setFlat(True)
        self.btn_search.setObjectName("btn_search")
        self.textbox_save = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_save.setGeometry(QtCore.QRect(1185, 550, 591, 60))
        self.textbox_save.setStyleSheet("font: 20pt \"Mitr SemiBold\";\n"
"background: transparent")
        self.textbox_save.setText("")
        self.textbox_save.setFrame(False)
        self.textbox_save.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textbox_save.setObjectName("textbox_save")
        self.textbox_search = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_search.setGeometry(QtCore.QRect(160, 220, 791, 60))
        self.textbox_search.setStyleSheet("font: 20pt \"Mitr SemiBold\";\n"
"background: transparent")
        self.textbox_search.setText("")
        self.textbox_search.setFrame(False)
        self.textbox_search.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textbox_search.setObjectName("textbox_search")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(110, 90, 93, 93))
        self.btn_back.setStyleSheet("background-image: url(:/image/Picture/back.png);")
        self.btn_back.setText("")
        self.btn_back.setFlat(True)
        self.btn_back.setObjectName("btn_back")
        Main_AE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_AE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        Main_AE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_AE)
        self.statusbar.setObjectName("statusbar")
        Main_AE.setStatusBar(self.statusbar)

        self.retranslateUi(Main_AE)
        QtCore.QMetaObject.connectSlotsByName(Main_AE)

    def retranslateUi(self, Main_AE):
        _translate = QtCore.QCoreApplication.translate
        Main_AE.setWindowTitle(_translate("Main_AE", "หมวด A-E"))
        self.btn_play.setToolTip(_translate("Main_AE", "<html><head/><body><p>กดปุ่มเพื่อเล่นสุ่มคำศัพท์</p></body></html>"))
        self.btn_save.setToolTip(_translate("Main_AE", "<html><head/><body><p>กดปุ่มเพื่อบันทึกคำศัพท์</p></body></html>"))
        self.btn_delete.setToolTip(_translate("Main_AE", "<html><head/><body><p>กดปุ่มเพื่อลบคำศัพท์</p></body></html>"))
        self.btn_play2.setText(_translate("Main_AE", "PLAY"))
        self.btn_save2.setText(_translate("Main_AE", "ADD&&SAVE"))
        self.btn_delete2.setText(_translate("Main_AE", "DELETE"))
        self.label.setText(_translate("Main_AE", "หมวด A-E"))
        self.btn_show.setText(_translate("Main_AE", "SHOW"))
        self.textbox_delete.setPlaceholderText(_translate("Main_AE", "ตัวอย่าง ant=มด **ใส่=ด้วย"))
        self.btn_search.setToolTip(_translate("Main_AE", "<html><head/><body><p>กดปุ่มเพื่อค้นหา</p></body></html>"))
        self.textbox_save.setPlaceholderText(_translate("Main_AE", "ตัวอย่าง ant=มด **ใส่=ด้วย"))
        self.textbox_search.setPlaceholderText(_translate("Main_AE", "SEARCH"))
        self.btn_back.setToolTip(_translate("Main_AE", "<html><head/><body><p>กดปุ่มเพื่อกลับหน้าแรก</p></body></html>"))
import vocab_pic1_rc
