# -*- coding: utf-8 -*-
"""
Created on Mon May  2 03:01:23 2022

@author: MSA
"""
import sys

from PyQt5 import QtWidgets, QtGui

class pencere(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLabel("bana henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("bana tıkla")
        self.say = 0
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        
        self.setLayout(v_box)
        
        self.show

app = QtWidgets.QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())