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
        
        extractAction = QtWidgets.QAction('EXIT NOW!!!', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)
        
        extractAction2 = QtWidgets.QAction('EXIT NOW2!!!', self)
        extractAction2.setShortcut('Ctrl+W')
        extractAction2.setStatusTip('also used to leave the app')
        extractAction2.triggered.connect(self.close_application)
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction2)
        
        self.home()
        
        
    def home(self):
        btn = QtWidgets.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        
        extractAction = QtWidgets.QAction(QtGui.QIcon('trilobit.jpg'), 'flee the scene', self)
        extractAction.triggered.connect(self.close_application)
    
        self.toolbar = self.addToolBar('Extraction')
        self.toolbar.addAction(extractAction)
    
    def close_application(self):
        print(' whooaaaa so custom!')
        sys.exit()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
#    app.aboutToQuit.connect(app.deleteLater)
    GUI = Window()
    GUI.show()
    app.exec_()
    sys.exit(0) 