# -- coding: utf-8 --

# Form implementation generated from reading ui file 'sequence.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 


class Ui_Subsequence(object):
    def say_hello(self, Subsequence):
        _translate = QtCore.QCoreApplication.translate
        string1 = self.lineEdit.text()
        string2 = self.lineEdit_2.text()
        
        output = lcs(string1,string2,len(string1),len(string2))
        
        output = str(output)
        self.lineEdit_3.setText(_translate("Subsequence", output))
        

    def setupUi(self, Subsequence):
        Subsequence.setObjectName("Subsequence")
        Subsequence.resize(782, 382)
        self.label = QtWidgets.QLabel(Subsequence)
        self.label.setGeometry(QtCore.QRect(30, 10, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Subsequence)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 711, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Subsequence)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 671, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Subsequence)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Subsequence)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Subsequence)
        self.label_5.setGeometry(QtCore.QRect(50, 260, 281, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.lineEdit = QtWidgets.QLineEdit(Subsequence)
        self.lineEdit.setGeometry(QtCore.QRect(160, 180, 551, 22))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Subsequence)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 220, 551, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(Subsequence)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 260, 121, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.groupBox = QtWidgets.QGroupBox(Subsequence)
        self.groupBox.setGeometry(QtCore.QRect(30, 130, 711, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(Subsequence)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 711, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Subsequence)
        self.pushButton.setGeometry(QtCore.QRect(620, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.groupBox.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.say_hello)

        self.retranslateUi(Subsequence)
        QtCore.QMetaObject.connectSlotsByName(Subsequence)
  #      Subsequence.connect(self.pushButton, SIGNAL("clicked()"),self.button_click)

    def retranslateUi(self, Subsequence):
        _translate = QtCore.QCoreApplication.translate
        Subsequence.setWindowTitle(_translate("Subsequence", "Longest Common Subsequence"))
        self.label.setText(_translate("Subsequence", "Longest Common Subsequence Algorithm"))
        self.textBrowser.setHtml(_translate("Subsequence", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Given two sequences, find the length of longest subusequence present in both of them. A subsequence is a sequennce that appears in same relative order, but not necessarily contiguous.</p></body></html>"))
        self.label_2.setText(_translate("Subsequence", "Enter the two sequences without spaces and press Output button to see the length of longest common subsequence"))
        self.label_3.setText(_translate("Subsequence", "Sequence 1"))
        self.label_4.setText(_translate("Subsequence", "Sequence 2"))
        self.label_5.setText(_translate("Subsequence", "Length of Longest common subsequence"))
        self.label_6.setText(_translate("Subsequence", "Time Complexity of the above algorithm is O(mn), where m an d n represent the length 2 sequences entered by the user."))
        self.pushButton.setText(_translate("Subsequence", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Subsequence = QtWidgets.QDialog()
    ui = Ui_Subsequence()
    ui.setupUi(Subsequence)
    Subsequence.show()
    sys.exit(app.exec_())