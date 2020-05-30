# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrixchain.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

def MatrixChainOrder(p, i, j): 

    if i == j: 
        return 0

    _min = sys.maxsize 
    
     
    for k in range(i, j): 
    
        count = (MatrixChainOrder(p, i, k) 
            + MatrixChainOrder(p, k+1, j) 
                + p[i-1] * p[k] * p[j]) 

        if count < _min: 
            _min = count; 
    

    # Return minimum count 
    return _min; 



class Ui_matrixmult(object):
    def say_hello(self,matrixmult):
        _translate = QtCore.QCoreApplication.translate
        n = int(self.lineEdit.text())
        arr1 = self.lineEdit_2.text()
        arr=list(map(int, arr1.split()))
        output=MatrixChainOrder(arr, 1, n-1)
        output=str(output)
        self.lineEdit_3.setText(_translate("matrixmult",output))



    def setupUi(self, matrixmult):
        matrixmult.setObjectName("matrixmult")
        matrixmult.resize(899, 434)
        self.label = QtWidgets.QLabel(matrixmult)
        self.label.setGeometry(QtCore.QRect(30, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(matrixmult)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 811, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(matrixmult)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 191, 16))
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(matrixmult)
        self.label_1.setGeometry(QtCore.QRect(40, 270, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.groupBox = QtWidgets.QGroupBox(matrixmult)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 831, 271))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 140, 391, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 191, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(290, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 210, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(matrixmult)
        self.pushButton.setGeometry(QtCore.QRect(720, 390, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(matrixmult)
        self.label_6.setGeometry(QtCore.QRect(10, 340, 501, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_1.raise_()
        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.say_hello)
        self.label_6.raise_()

        self.retranslateUi(matrixmult)
        QtCore.QMetaObject.connectSlotsByName(matrixmult)

    def retranslateUi(self, matrixmult):
        _translate = QtCore.QCoreApplication.translate
        matrixmult.setWindowTitle(_translate("matrixmult", "Matrix Chain Multiplication"))
        self.label.setText(_translate("matrixmult", "Matrix Chain Multiplication"))
        self.label_2.setText(_translate("matrixmult", "Enter an array representing the chain of matrices such that ith matrix is of dimension p[i-1] x p[i] and p. Separate elements with space."))
        self.label_3.setText(_translate("matrixmult", "Number of elements in array"))
        self.label_1.setText(_translate("matrixmult", "Minimum number of multiplications required"))
        self.label_4.setText(_translate("matrixmult", "Array representing dimensions"))
        self.pushButton.setText(_translate("matrixmult", "Output"))
        self.label_6.setText(_translate("matrixmult", "Time Complexity of above algorithm is O(n), n represents the size of array entered."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    matrixmult = QtWidgets.QDialog()
    ui = Ui_matrixmult()
    ui.setupUi(matrixmult)
    matrixmult.show()
    sys.exit(app.exec_())
