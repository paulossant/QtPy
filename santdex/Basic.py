#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:46:01 2019

@author: pssantos
"""

import sys
from PyQt5 import QtWidgets, QtGui



class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('BasicGui!')
        self.setWindowIcon(QtGui.QIcon('trilobit.jpg'))     
        self.setWindowIconText('Trilobit')
        self.show()
#        self.home()
        
#    def home(self):
#        btn = 
#        self.
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_()) 