# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assembly.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

def carAssembly (a, t, e, x): 
      
    NUM_STATION = len(a[0]) 
    T1 = [0 for i in range(NUM_STATION)] 
    T2 = [0 for i in range(NUM_STATION)] 
      
    T1[0] = e[0] + a[0][0] # time taken to leave 
                           # first station in line 1 
    T2[0] = e[1] + a[1][0] # time taken to leave 
                           # first station in line 2 
  
    # Fill tables T1[] and T2[] using 
    # above given recursive relations 
    for i in range(1, NUM_STATION): 
        T1[i] = min(T1[i-1] + a[0][i], 
                    T2[i-1] + t[1][i] + a[0][i]) 
        T2[i] = min(T2[i-1] + a[1][i], 
                    T1[i-1] + t[0][i] + a[1][i] ) 
  
    # consider exit times and return minimum 
    return min(T1[NUM_STATION - 1] + x[0], 
               T2[NUM_STATION - 1] + x[1]) 
 



class Ui_Assemblyline(object):
    def say_hello(self, Assemblyline):
        _translate = QtCore.QCoreApplication.translate
        print ("button")
        C=int(self.lineEdit.text())
        
        arre=self.lineEdit_2.text()
        
        e=list(map(int, arre.split()))
        
        
        arrx=self.lineEdit_3.text()
        x=list(map(int, arrx.split()))
        
        
        arr1=self.lineEdit_5.text()
        
        entries1=list(map(int, arr1.split()))
         
        a=np.array(entries1).reshape(2, C)
        
        

        arr2=self.lineEdit_6.text()
        entries2=list(map(int, arr2.split())) 
        t=np.array(entries2).reshape(2, C)
        
        

        output=carAssembly(a, t, e, x)
        output=str(output)

        self.lineEdit_4.setText(_translate("Assemblyline",output))

    

    def setupUi(self, Assemblyline):
        Assemblyline.setObjectName("Assemblyline")
        Assemblyline.resize(944, 590)
        self.label = QtWidgets.QLabel(Assemblyline)
        self.label.setGeometry(QtCore.QRect(30, 10, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Assemblyline)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 881, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label_1 = QtWidgets.QGroupBox(Assemblyline)
        self.label_1.setGeometry(QtCore.QRect(30, 260, 881, 261))
        self.label_1.setTitle("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.label_1)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 181, 21))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.label_1)
        self.label_6.setGeometry(QtCore.QRect(330, 90, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.label_1)
        self.label_7.setGeometry(QtCore.QRect(330, 130, 61, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.label_1)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.label_1)
        self.label_4.setGeometry(QtCore.QRect(10, 138, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.label_1)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.label_1)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 61, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.label_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 90, 181, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.label_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 130, 181, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.label_1)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 180, 141, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.label_1)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 90, 381, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.label_1)
        self.lineEdit_6.setGeometry(QtCore.QRect(390, 130, 381, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.label_1)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 321, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Assemblyline)
        self.pushButton.setGeometry(QtCore.QRect(760, 550, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Assemblyline)
        self.label_8.setGeometry(QtCore.QRect(30, 530, 561, 16))
        self.label_8.setObjectName("label_8")
        self.label_1.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.say_hello)
        self.label_8.raise_()

        self.retranslateUi(Assemblyline)
        QtCore.QMetaObject.connectSlotsByName(Assemblyline)

    def retranslateUi(self, Assemblyline):
        _translate = QtCore.QCoreApplication.translate
        Assemblyline.setWindowTitle(_translate("Assemblyline", "Dialog"))
        self.label.setText(_translate("Assemblyline", "Assembly Line Scheduling"))
        self.textBrowser.setHtml(_translate("Assemblyline", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:8pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">A car factory has two assembly lines, each with n stations. A station is denoted by Si,j where i is either 1 or 2 and indicates the assembly line the station is on, and j indicates the number of the station. The time taken per station is denoted by ai,j. Each station is dedicated to some sort of work like engine fitting, body fitting, painting and so on. So, a car chassis must pass through each of the n stations in order before exiting the factory. The parallel stations of the two assembly lines perform the same task. After it passes through station Si,j, it will continue to station Si,j+1 unless it decides to transfer to the other line. Continuing on the same line incurs no extra cost, but transferring from line i at station j – 1 to station j on the other line takes time ti,j. Each assembly line takes an entry time ei and exit time xi which may be different for the two lines. Give an algorithm for computing the minimum time it will take to build a car chassis.</span></p></body></html>"))
        self.label_2.setText(_translate("Assemblyline", "No. of Station/Assembly line"))
        self.label_6.setText(_translate("Assemblyline", "Matrix a"))
        self.label_7.setText(_translate("Assemblyline", "Matrix t"))
        self.label_3.setText(_translate("Assemblyline", "Array e"))
        self.label_4.setText(_translate("Assemblyline", "Array x"))
        self.label_5.setText(_translate("Assemblyline", "Minimum time"))
        self.label_9.setText(_translate("Assemblyline", "Enter Arrays and matrices separated by spaces:"))
        self.pushButton.setText(_translate("Assemblyline", "Output"))
        self.label_8.setText(_translate("Assemblyline", "Time Complexity of above algorithm is O(n), n represents the no. of stations in the assembly line"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Assemblyline = QtWidgets.QDialog()
    ui = Ui_Assemblyline()
    ui.setupUi(Assemblyline)
    Assemblyline.show()
    sys.exit(app.exec_())
