from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_Main_PT(object):

        def play_game(self):
                from play_pt import Ui_Play_PT
                self.game = QtWidgets.QMainWindow()
                self.ui = Ui_Play_PT()
                self.ui.setupUi(self.game)
                self.game.show()

        def back_main_menu(self):
                from main_menu import Ui_Main_Menu
                self.menu = QtWidgets.QMainWindow()
                self.ui = Ui_Main_Menu()
                self.ui.setupUi(self.menu)
                self.menu.show()

        def setupUi(self, Main_PT):
                Main_PT.setObjectName("Main_PT")
                Main_PT.resize(1920, 1080)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/image/Picture/cards.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                Main_PT.setWindowIcon(icon)
                Main_PT.setStyleSheet("background-image: url(:/image/Picture/p_t.jpg);")
                self.centralwidget = QtWidgets.QWidget(Main_PT)
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
                Main_PT.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(Main_PT)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
                self.menubar.setObjectName("menubar")
                Main_PT.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(Main_PT)
                self.statusbar.setObjectName("statusbar")
                Main_PT.setStatusBar(self.statusbar)

                self.btn_show.clicked.connect(self.show)
                self.btn_search.clicked.connect(self.search)
                self.btn_delete.clicked.connect(self.delete)
                self.btn_save.clicked.connect(self.save)
                self.textbox_search.returnPressed.connect(self.search)
                self.textbox_save.returnPressed.connect(self.save)
                self.textbox_delete.returnPressed.connect(self.delete)
                self.btn_back.clicked.connect(self.back_main_menu)
                self.btn_back.clicked.connect(Main_PT.hide)
                self.btn_play.clicked.connect(self.play_game)
                self.btn_play.clicked.connect(Main_PT.hide)

                self.retranslateUi(Main_PT)
                QtCore.QMetaObject.connectSlotsByName(Main_PT)

        def retranslateUi(self, Main_PT):
                _translate = QtCore.QCoreApplication.translate
                Main_PT.setWindowTitle(_translate("Main_PT", "หมวด P-T"))
                self.btn_play.setToolTip(_translate("Main_PT", "<html><head/><body><p>กดปุ่มเพื่อเล่นสุ่มคำศัพท์</p></body></html>"))
                self.btn_save.setToolTip(_translate("Main_PT", "<html><head/><body><p>กดปุ่มเพื่อบันทึกคำศัพท์</p></body></html>"))
                self.btn_delete.setToolTip(_translate("Main_PT", "<html><head/><body><p>กดปุ่มเพื่อลบคำศัพท์</p></body></html>"))
                self.btn_play2.setText(_translate("Main_PT", "PLAY"))
                self.btn_save2.setText(_translate("Main_PT", "ADD&&SAVE"))
                self.btn_delete2.setText(_translate("Main_PT", "DELETE"))
                self.label.setText(_translate("Main_PT", "หมวด P-T"))
                self.btn_show.setText(_translate("Main_PT", "SHOW"))
                self.textbox_delete.setPlaceholderText(_translate("Main_PT", "ตัวอย่าง ant=มด **ใส่=ด้วย"))
                self.btn_search.setToolTip(_translate("Main_PT", "<html><head/><body><p>กดปุ่มเพื่อค้นหา</p></body></html>"))
                self.textbox_save.setPlaceholderText(_translate("Main_PT", "ตัวอย่าง ant=มด **ใส่=ด้วย"))
                self.textbox_search.setPlaceholderText(_translate("Main_PT", "SEARCH"))
                self.btn_back.setToolTip(_translate("Main_PT", "<html><head/><body><p>กดปุ่มเพื่อกลับหน้าแรก</p></body></html>"))

        def show(self):
                self.plainTextEdit.clear()
                file = "p_t.txt"
                msg = QMessageBox()
                msg.setWindowTitle("ไม่พบคำศัพท์")
                msg.setIcon(QMessageBox.Information)

                with open(file, "a", encoding="UTF-8") as f:
                        pass
                with open(file,encoding="UTF-8") as f:
                        filesize = os.path.getsize("p_t.txt")
                        if filesize == 0:
                                msg.setText("กรุณาบันทึกคำศัพท์")
                                x = msg.exec_()
                        else:
                                for line in f:
                                        line = line.replace('\n','')
                                        line = line.replace('_',' ')
                                        (Vocab1,Vocab2) = line.split('=')
                                        self.plainTextEdit.appendPlainText(" {:<50}\t{}".format(Vocab1,Vocab2))

        def save(self):
                file = "p_t.txt"
                vocab = self.textbox_save.text().lower()
                vocab = vocab.replace(' ','')
                list_vocab = []
                msg = QMessageBox()
                msg.setWindowTitle("บันทึกคำศัพท์")
                msg.setIcon(QMessageBox.Information)
                if vocab == "":
                        msg.setText("กรุณาป้อนคำศัพท์")
                else:
                        with open(file, "a", encoding="UTF-8") as f:
                                pass
                        with open(file, encoding="UTF-8") as f:
                                for line in f:
                                        line = line.replace('\n','')
                                        list_vocab.append(line)
                        if vocab in list_vocab:
                                msg.setText("มีคำศัพท์นี้ในระบบแล้ว")
                        else:
                                if str("=") in vocab:
                                        with open(file, "a", encoding="UTF-8") as f:
                                                f.write(f"{vocab}\n")
                                                vocab = vocab.replace('_',' ')
                                                msg.setText(f"บันทึกคำศัพท์ {vocab} แล้ว")
                                                self.textbox_save.clear()
                                else:
                                        msg.setText("ป้อนเครื่องหมาย = ด้วย")
                x = msg.exec_()

        def search(self):
                file = "p_t.txt"
                p_t = {}
                vocab = self.textbox_search.text().lower()
                vocab = vocab.replace(' ','')
                msg = QMessageBox()
                msg.setWindowTitle("ค้นหาคำศัพท์")
                msg.setIcon(QMessageBox.Information)
                if vocab == "":
                        msg.setText("กรุณาป้อนคำศัพท์")
                else:
                        with open(file, "a", encoding="UTF-8") as f:
                                filesize = os.path.getsize("p_t.txt")
                                if filesize == 0:
                                        msg.setText("ไม่พบคำศัพท์")
                                else:
                                        with open(file,encoding="UTF-8") as f:
                                                for line in f:
                                                        line = line.replace('\n','')
                                                        (Vocab1,Vocab2) = line.split('=')
                                                        p_t.setdefault(Vocab1,[])
                                                        p_t[Vocab1].append(Vocab2)

                                                if vocab in p_t:
                                                        Vocab1 = vocab
                                                        Vocab2 = p_t[Vocab1]
                                                        Vocab1 = Vocab1.replace('_',' ')
                                                        ans = ", "
                                                        msg.setText("".join("คำศัพท์ที่คุณค้นหาคือ {} = {} ".format(Vocab1,ans.join(Vocab2))))
                                                else:
                                                        msg.setText("ไม่พบคำศัพท์")
                x = msg.exec_()

        def delete(self):
                file = "p_t.txt"
                list_vocab = []
                list_vocab2 = []
                vocab = self.textbox_delete.text().lower()
                vocab = vocab.replace(' ','')
                msg = QMessageBox() 
                msg.setWindowTitle("ลบคำศัพท์")
                msg.setIcon(QMessageBox.Information)
                if vocab == "":
                        msg.setText("กรุณาป้อนคำศัพท์")
                else:
                        if str("=") in vocab:
                                with open(file, "a",encoding="UTF-8") as f:
                                        filesize = os.path.getsize("p_t.txt")
                                        if filesize == 0:
                                                msg.setText("ไม่พบคำศัพท์ในระบบ")
                                        else:
                                                with open(file, encoding="UTF-8") as f:
                                                        for line in f:
                                                                line = line.replace('\n','')
                                                                list_vocab2.append(line)
                                                                if vocab == line:
                                                                        pass
                                                                else:
                                                                        list_vocab.append(line)

                                                        if vocab in list_vocab2:
                                                                with open(file,"w", encoding="UTF-8") as f:
                                                                        for line in list_vocab:
                                                                                f.write(f"{line}\n")
                                                                vocab = vocab.replace('_',' ')
                                                                msg.setText(f"ลบคำศัพท์ {vocab} แล้ว")
                                                                self.textbox_delete.clear()
                                                        else:
                                                                msg.setText("ไม่พบคำศัพท์ในระบบ")
                        else:
                                msg.setText("กรุณาป้อนเครื่องหมาย = ความหมาย")
                x = msg.exec_()
                
import vocab_pic1_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_PT = QtWidgets.QMainWindow()
    ui = Ui_Main_PT()
    ui.setupUi(Main_PT)
    Main_PT.show()
    sys.exit(app.exec_())
