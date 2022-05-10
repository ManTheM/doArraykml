# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:41:33 2022

@author: MSA
"""
from PyQt5 import QtWidgets
import sys
# from designerÇıktısı import Ui_MainWindow
#from createArrayUI2 import Ui_Form

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
        
    
def app():
        app = QtWidgets.QApplication(sys.argv)
        win = myApp()
        win.show()
        sys.exit(app.exec_())
        
app()