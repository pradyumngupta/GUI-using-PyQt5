# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shortest.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

  
INF  = 99999
  
def floydWarshall(graph,V): 

    dist = list(map(lambda i :list( map(lambda j : j , i)) , graph) )
    
    for k in range(V): 
  
        for i in range(V): 
  
            for j in range(V): 
  
                dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j] )
    
    
    print(dist)
    return dist 
  
 


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShortestPath(object):
    def say_hello(self, ShortestPath):
        _translate = QtCore.QCoreApplication.translate
        v = self.lineEdit.text()
        v = int(v)
        string = self.textEdit.toPlainText()
        lines = string.split("\n")
        
        print(len(lines))
        
        if len(lines) < v:
             self.textEdit_2.setText(_translate("ShortestPath", "Input Error! \n Matrix is incorrect"))
             return
        graph = []
        for i in range(0,v):
            print(i)
            graph.insert(i,lines[i].split(" "))
            print(lines[i].split(" "))
        
        print(graph)
        for i in range(0,v):
            for j in range(0,v):
                graph[i][j] = int(graph[i][j])
                if graph[i][j]==-1:
                    graph[i][j] = INF
                if i == j:
                    graph[i][j] = 0
        print(graph,v)
        print("Button Clicked")
        
        mat = floydWarshall(graph,v)
        sol = ""
        for i in range(0,v):
            for j in range(0,v):
                sol = sol + " "+ str(mat[i][j])
            sol = sol + "\n"
        
            
            
            
            
        
  
        
        self.textEdit_2.setText(_translate("ShortestPath", sol))
       
    
    
    def setupUi(self, ShortestPath):
        ShortestPath.setObjectName("ShortestPath")
        ShortestPath.resize(881, 574)
        self.label = QtWidgets.QLabel(ShortestPath)
        self.label.setGeometry(QtCore.QRect(20, 10, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(ShortestPath)
        self.textBrowser.setGeometry(QtCore.QRect(90, 60, 641, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_1 = QtWidgets.QGroupBox(ShortestPath)
        self.label_1.setGeometry(QtCore.QRect(40, 190, 791, 331))
        self.label_1.setTitle("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.label_1)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.label_1)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        
        self.textEdit = QtWidgets.QTextEdit(self.label_1)
        self.textEdit.setGeometry(QtCore.QRect(50, 100, 231, 201))
        self.textEdit.setObjectName("textEdit")
        

        self.textEdit_2 = QtWidgets.QTextEdit(self.label_1)
        self.textEdit_2.setGeometry(QtCore.QRect(500, 100, 231, 201))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.label_1)
        self.label_3.setGeometry(QtCore.QRect(120, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.label_1)
        self.label_4.setGeometry(QtCore.QRect(530, 70, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.label_1)
        self.pushButton.setGeometry(QtCore.QRect(340, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(ShortestPath)
        self.label_5.setGeometry(QtCore.QRect(40, 530, 481, 16))
        self.label_5.setObjectName("label_5")
        self.label_1.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        self.label_5.raise_()
        self.pushButton.clicked.connect(self.say_hello)


        self.retranslateUi(ShortestPath)
        QtCore.QMetaObject.connectSlotsByName(ShortestPath)

    def retranslateUi(self, ShortestPath):
        _translate = QtCore.QCoreApplication.translate
        ShortestPath.setWindowTitle(_translate("ShortestPath", "All Pair Shortest Path"))
        self.label.setText(_translate("ShortestPath", "All Pair Shortest Path"))
        self.textBrowser.setHtml(_translate("ShortestPath", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\">The </span><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#ffffff;\">all pair shortest path</span><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\"> algorithm is also known as Floyd-Warshall algorithm is used to find </span><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#ffffff;\">all pair shortest path</span><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\"> problem from a given weighted graph. As a result of this algorithm, it will generate a matrix, which will represent the minimum distance from any node to</span><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#ffffff;\"> all</span><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\"> other nodes in the graph.</span></p></body></html>"))
        self.label_2.setText(_translate("ShortestPath", "No. of Vertices (V):"))
        self.label_3.setText(_translate("ShortestPath", "Input Matrix"))
        self.label_4.setText(_translate("ShortestPath", "Shortest Distance Matrix"))
        self.pushButton.setText(_translate("ShortestPath", "Output"))
        self.label_5.setText(_translate("ShortestPath", "Time complexity of above algorithm is O(v^3), v represents the no. of vertices."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShortestPath = QtWidgets.QDialog()
    ui = Ui_ShortestPath()
    ui.setupUi(ShortestPath)
    ShortestPath.show()
    sys.exit(app.exec_())

 


