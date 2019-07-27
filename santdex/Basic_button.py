#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:46:01 2019

@author: pssantos
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('BasicGui!')
        self.setWindowIcon(QtGui.QIcon('trilobit.jpg'))     
        self.setWindowIconText('Trilobit')
        self.home()
        
    def home(self):
        btn = QtWidgets.QPushButton('Quit', self)
#        btn.clicked.connect(QtCore.QCoreApplication.exit)
        btn.clicked.connect(self.close_application)
#        btn.resize(100,100)
        btn.move(100,100)
    
    def close_application(self):
#        print(' whooaaaa so custom!')
        sys.exit()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
#    app.aboutToQuit.connect(app.deleteLater)
    GUI = Window()
    GUI.show()
    app.exec_()
    sys.exit(0) 