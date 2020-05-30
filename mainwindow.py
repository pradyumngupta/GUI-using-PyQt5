# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from shortest import Ui_ShortestPath
from assembly import Ui_Assemblyline
from matrixchain import Ui_matrixmult
from sequence import Ui_Subsequence
from knapsack import Ui_Knapsack


class Ui_MainWindow(object):
    def openWindow(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_ShortestPath()
        self.ui.setupUi(self.window)
        self.window.show() 

    def openWindow1(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Assemblyline()
        self.ui.setupUi(self.window)
        self.window.show() 

    def openWindow2(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_matrixmult()
        self.ui.setupUi(self.window)
        self.window.show() 

    def openWindow3(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Subsequence()
        self.ui.setupUi(self.window)
        self.window.show() 

    def openWindow4(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Knapsack()
        self.ui.setupUi(self.window)
        self.window.show()   

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 831, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 220, 361, 411))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 310, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 240, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 180, 291, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 291, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 220, 461, 411))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.textBrowser_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(self.openWindow1)
        self.pushButton_3.clicked.connect(self.openWindow2)
        self.pushButton_4.clicked.connect(self.openWindow3)
        self.pushButton_5.clicked.connect(self.openWindow4)


        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans-serif\'; font-size:11pt; font-weight:600; color:#222222; background-color:#ffffff;\">Dynamic Programming</span><span style=\" font-family:\'arial,sans-serif\'; font-size:11pt; color:#222222; background-color:#ffffff;\"> is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans-serif\'; font-size:11pt; color:#222222; background-color:#ffffff;\">This GUI computes problem based on the selected algorithm.Select any algorithm to proceed.</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "0/1 Knapsack"))
        self.pushButton_4.setText(_translate("MainWindow", "Longest common subsequence"))
        self.pushButton_3.setText(_translate("MainWindow", "Matrix chain multiplication"))
        self.pushButton_2.setText(_translate("MainWindow", "Assembly line Scheduling"))
        self.pushButton.setText(_translate("MainWindow", "All Pair Shortest Path"))
        self.label.setText(_translate("MainWindow", "Design & Analysis of Algorithms"))
        self.label_2.setText(_translate("MainWindow", "Made By: Pradyumn Gupta,18103068"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/complexity/rsz_annotation_2020-04-30_220231.jpg\" /></p></body></html>"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
