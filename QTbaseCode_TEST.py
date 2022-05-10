# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:41:33 2022

@author: MSA
"""
from PyQt5 import QtWidgets, QtGui
import sys
# from designerÇıktısı import Ui_MainWindow
from qtbase_TEST2 import Ui_Form

class myApp(QtWidgets.QWidget):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # 1 # self.ui.combob_degreeORutm.activated.connect(self.coortype)
        self.ui.rb_degree.toggled.connect(self.coortype)
        
    def coortype(self):
        rb = self.sender()
        if rb.isChecked():
            print('secilen: '+ rb.text())
        else:
            print('sss' + rb.text())
        
    # def dokml(self):
        
    #     return
    
    # def doarray(self):
        
    #     return
    
# 1 ===========================================================================
#     def coortype(self):
#         global coor_type
#         coor_type = self.ui.combob_degreeORutm.currentIndex()
#         # print(self.ui.combob_degreeORutm.currentText())
#         # print(self.ui.combob_degreeORutm.currentIndex())
# =============================================================================

# BU DA OLUR
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('myAppp')
    dialog = myApp() # Class ismini yaz
    dialog.show()
    sys.exit(app.exec_())
    
# BU DA OLUR    
# =============================================================================
# def app():
#         app = QtWidgets.QApplication(sys.argv)
#         win = myApp()  #Class ismini yaz
#         win.show()
#         sys.exit(app.exec_())
#         
# app()
# =============================================================================