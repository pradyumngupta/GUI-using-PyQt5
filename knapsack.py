# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knapsack.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

def knapsack(W, wt, val, n):

           if(n==0 or W==0):

               return 0

           if(wt[n-1] > W):

               return knapsack(W, wt, val, n-1)

           else:

               return max(val[n-1]+knapsack(W-wt[n-1],wt,val,n-1),knapsack(W, wt, val, n-1))


class Ui_Knapsack(object):
    def say_hello(self,Knapsack):      
        _translate = QtCore.QCoreApplication.translate         
        
        
        n = int(self.lineEdit.text())
        arr1 = self.lineEdit_2.text() 
        val=list(map(int, arr1.split()))
        arr2 = self.lineEdit_3.text()
        wt=list(map(int, arr2.split())) 
        W = int(self.lineEdit_4.text())
              
        output = knapsack(W,wt,val,n)
        
        output = str(output)
        
        self.lineEdit_5.setText(_translate("Knapsack",output))
        

        

    

    def setupUi(self, Knapsack):
        Knapsack.setObjectName("Knapsack")
        Knapsack.resize(932, 452)
        self.label = QtWidgets.QLabel(Knapsack)
        self.label.setGeometry(QtCore.QRect(40, 10, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Knapsack)
        self.textBrowser.setGeometry(QtCore.QRect(40, 50, 861, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Knapsack)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 781, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Knapsack)
        self.label_3.setGeometry(QtCore.QRect(50, 230, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Knapsack)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Knapsack)
        self.label_5.setGeometry(QtCore.QRect(50, 290, 151, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Knapsack)
        self.label_6.setGeometry(QtCore.QRect(50, 320, 181, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Knapsack)
        self.label_7.setGeometry(QtCore.QRect(50, 350, 231, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(Knapsack)
        self.lineEdit.setGeometry(QtCore.QRect(290, 230, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        

        self.lineEdit_2 = QtWidgets.QLineEdit(Knapsack)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 260, 491, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        

        self.lineEdit_3 = QtWidgets.QLineEdit(Knapsack)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 290, 491, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")

        

        self.lineEdit_4 = QtWidgets.QLineEdit(Knapsack)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 320, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")

        

        self.lineEdit_5 = QtWidgets.QLineEdit(Knapsack)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 350, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.groupBox = QtWidgets.QGroupBox(Knapsack)
        self.groupBox.setGeometry(QtCore.QRect(40, 190, 861, 191))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_8 = QtWidgets.QLabel(Knapsack)
        self.label_8.setGeometry(QtCore.QRect(40, 390, 711, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Knapsack)
        self.pushButton.setGeometry(QtCore.QRect(810, 400, 93, 28))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")

        
        
        self.groupBox.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.label_8.raise_()
        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.say_hello)

        self.retranslateUi(Knapsack)
        QtCore.QMetaObject.connectSlotsByName(Knapsack)

    def retranslateUi(self, Knapsack):
        _translate = QtCore.QCoreApplication.translate
        Knapsack.setWindowTitle(_translate("Knapsack", "0/1 Knapsack"))
        self.label.setText(_translate("Knapsack", "0/1 Knapsack"))
        self.textBrowser.setHtml(_translate("Knapsack", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:8pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).</span></p></body></html>"))
        self.label_2.setText(_translate("Knapsack", "Enter the required inputs and press Output button to see Maximum profit earned, the elements in array must be separated by space."))
        self.label_3.setText(_translate("Knapsack", "No. of products available(n) "))
        self.label_4.setText(_translate("Knapsack", "Array of weights"))
        self.label_5.setText(_translate("Knapsack", "Array of profits"))
        self.label_6.setText(_translate("Knapsack", "Maximum weight of knapsack"))
        self.label_7.setText(_translate("Knapsack", "Maximum profit that can be earned"))
        self.label_8.setText(_translate("Knapsack", "Time Complexity of above algorithm is O(nW), where n is represented by no. of items and Wis the capacity of knapsack."))
        self.pushButton.setText(_translate("Knapsack", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Knapsack = QtWidgets.QDialog()
    ui = Ui_Knapsack()
    ui.setupUi(Knapsack)
    Knapsack.show()

    sys.exit(app.exec_())
    

    