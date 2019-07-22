# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:36:07 2019

@author: Paulo Santos
"""

from PyQt5 import QtWidgets, uic
 
import sys
 
app = QtWidgets.QApplication([])
 
win = uic.loadUi("tutorial0.ui") #specify the location of your .ui file
 
win.show()
 
sys.exit(app.exec())