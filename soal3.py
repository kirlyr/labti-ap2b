# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_karyawan.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 904)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 410, 1081, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 170, 201, 61))
        self.label.setObjectName("label")
        self.lineEditNama = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNama.setGeometry(QtCore.QRect(120, 180, 431, 41))
        self.lineEditNama.setObjectName("lineEditNama")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 531, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButtonSimpan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSimpan.setGeometry(QtCore.QRect(570, 350, 531, 51))
        self.pushButtonSimpan.setObjectName("pushButtonSimpan")
        self.pushButtonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(570, 290, 531, 51))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(20, 290, 531, 51))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 170, 201, 61))
        self.label_2.setObjectName("label_2")
        self.lineEditKelas = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKelas.setGeometry(QtCore.QRect(660, 180, 441, 41))
        self.lineEditKelas.setObjectName("lineEditKelas")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 220, 201, 61))
        self.label_3.setObjectName("label_3")
        self.lineEditMatprak = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMatprak.setGeometry(QtCore.QRect(660, 230, 441, 41))
        self.lineEditMatprak.setObjectName("lineEditMatprak")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 201, 61))
        self.label_4.setObjectName("label_4")
        self.lineEditNpm = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNpm.setGeometry(QtCore.QRect(120, 230, 431, 41))
        self.lineEditNpm.setObjectName("lineEditNpm")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(310, 0, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setItalic(False)
        font.setUnderline(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.lineEditNpm_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNpm_2.setGeometry(QtCore.QRect(120, 130, 431, 41))
        self.lineEditNpm_2.setObjectName("lineEditNpm_2")
        self.lineEditNama_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNama_2.setGeometry(QtCore.QRect(120, 80, 431, 41))
        self.lineEditNama_2.setObjectName("lineEditNama_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 120, 201, 61))
        self.label_6.setObjectName("label_6")
        self.lineEditMatprak_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMatprak_2.setGeometry(QtCore.QRect(660, 130, 441, 41))
        self.lineEditMatprak_2.setObjectName("lineEditMatprak_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 201, 61))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 70, 201, 61))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 201, 61))
        self.label_9.setObjectName("label_9")
        self.lineEditKelas_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKelas_2.setGeometry(QtCore.QRect(660, 80, 441, 41))
        self.lineEditKelas_2.setObjectName("lineEditKelas_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAMA"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NIK"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "JABATAN"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DEPARTEMEN"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ALAMAT"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EMAIL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SOCIAL MEDIA"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "GITHUB"))
        self.label.setText(_translate("MainWindow", "JABATAN"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButtonSimpan.setText(_translate("MainWindow", "CREATE"))
        self.pushButtonDelete.setText(_translate("MainWindow", "HAPUS"))
        self.pushButtonUpdate.setText(_translate("MainWindow", "UPDATE"))
        self.label_2.setText(_translate("MainWindow", "SOCIAL MEDIA"))
        self.label_3.setText(_translate("MainWindow", "GITHUB"))
        self.label_4.setText(_translate("MainWindow", "DEPARTEMEN"))
        self.label_5.setText(_translate("MainWindow", "INPUT DATA KARYAWAN"))
        self.label_6.setText(_translate("MainWindow", "EMAIL"))
        self.label_7.setText(_translate("MainWindow", "NIK"))
        self.label_8.setText(_translate("MainWindow", "ALAMAT"))
        self.label_9.setText(_translate("MainWindow", "NAMA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
