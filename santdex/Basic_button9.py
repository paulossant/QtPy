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
        
        openEditor = QtWidgets.QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)
        
        openFile = QtWidgets.QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
           
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
        fileMenu.addAction(openFile)
        
        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)
        
        
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
    
        fontChoice = QtWidgets.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolbar = self.addToolBar('Font')
        self.toolbar.addAction(fontChoice)
    
        
        fontColor = QtWidgets.QAction('Font bg color', self)
        fontColor.triggered.connect(self.color_picker)
        self.toolbar.addAction(fontColor)
    
        checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
        checkBox.move(100,25)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)
        
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)
       
        self.btn = QtWidgets.QPushButton('Download', self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)
        
        print(self.style().objectName())
        self.styleChoice = QtWidgets.QLabel('Windows vista', self)
        
        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem('Fusion')
        comboBox.addItem('Breeze')
        comboBox.addItem('Plastik')
        comboBox.addItem('windows')
        
        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)
        
        cal = QtWidgets.QCalendarWidget(self)
        cal.move(250,250)
        cal.resize(350,350)
    
    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color: %s}' % color.name())
        
    def editor(self):
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
    
    def file_open(self):
         # need to make name an tupple otherwise i had an error and app crashed
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')
        self.editor()   #Call editor to show it
        with file:
            text = file.read()
            self.textEdit.setText(text)
        
        
    def font_choice(self):
        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
        
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))
        
       
    def download(self):
        self.completed = 0
        
        while self.completed <100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        
    
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)
    
    
    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract',
                                                'Get into the chopper?',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print('Extracting NOOOWWW!')
            sys.exit()
        else:
            pass
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_()) 