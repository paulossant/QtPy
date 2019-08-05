#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:54:55 2019

@author: pssantos
"""

import sys, json, webbrowser
from PyQt5 import QtWidgets, QtGui, QtCore
from GUI_DB import Ui_MainWindow 

with open('DB.json') as f:
    data = json.load(f)                         #Now data is a dictionary

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
                
        self.ui.actionExit.triggered.connect(self.close_application)
        self.ui.actionAbout.triggered.connect(self.showInfo)
        self.ui.comboBox_cat.currentIndexChanged.connect(self.loadDB)
        self.ui.comboBox_Add_Cat.currentIndexChanged.connect(self.addCatToDB)
        self.ui.btn_rmItem.clicked.connect(self.removeItem)
        self.ui.btn_addItem.clicked.connect(self.addItem)
        self.ui.btn_editItem.clicked.connect(self.editItem)
        self.ui.btn_save.clicked.connect(self.saveDB)
        self.ui.btn_search.clicked.connect(self.searchDB)
        self.ui.line_search.returnPressed.connect(self.searchDB)

        self.ui.tableWidget.itemPressed.connect(self.pressed)
        self.ui.tableWidget.itemDoubleClicked.connect(self.OpenLink)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableWidget.setSortingEnabled(False)
        
        self.loadDB()
    
        w = QtWidgets.QLabel()
        path = r"file:///run/media/pssantos/HDD/Documentos/Datasheets/an8473.pdf"
        url = bytearray(QtCore.QUrl.fromLocalFile(path).toEncoded()).decode() # file:///C:/Users/Shaurya/Documents/To%20be%20saved/hello.pdf
        text = "<a href={}>Reference Link> </a>".format(url)
        w.setText(text)
        w.setOpenExternalLinks(True)
        w.show()
 
    def event(self, event):
            if isinstance(event, QtGui.QKeyEvent):
                if event.type() == QtCore.QEvent.KeyPress:
                    if event.key() == QtCore.Qt.Key_Escape:
                        self.close_application()
                        return True
                    if event.key() == QtCore.Qt.Key_Control and QtCore.Qt.Key_S:
                        print ('yes')
                        self.saveDB()
                        return True 
            return super().event(event) 
    
    def searchDB(self):
        self.r=0
        r2=0
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(data['items']))
        for item in data['items']:  #The same subparameter of all elements in the list
            if ( (self.ui.line_search.text() in (str(item.get('name'))))      |
                 (self.ui.line_search.text() in str(item.get('type')))        |
                 (self.ui.line_search.text() in str(item.get('sub-type')))    |
                 (self.ui.line_search.text() in str(item.get('Package')))    |
                 (self.ui.line_search.text() in str(item.get('Location')))):
                self.ui.tableWidget.setItem( self.r,0, QtWidgets.QTableWidgetItem(str(data['items'][r2]['name'])))
                self.ui.tableWidget.setItem( self.r,1, QtWidgets.QTableWidgetItem(str(data['items'][r2]['type'])))
                self.ui.tableWidget.setItem( self.r,2, QtWidgets.QTableWidgetItem(str(data['items'][r2]['sub-type'])))
                self.ui.tableWidget.setItem( self.r,3, QtWidgets.QTableWidgetItem(str('%04i' % data['items'][r2]['Quantity'])))
                self.ui.tableWidget.setItem( self.r,4, QtWidgets.QTableWidgetItem(str(data['items'][r2]['Location'])))
                self.ui.tableWidget.setItem( self.r,5, QtWidgets.QTableWidgetItem(str('%.03f' % data['items'][r2]['Unit price'])))
                self.ui.tableWidget.setItem( self.r,6, QtWidgets.QTableWidgetItem(str(data['items'][r2]['Package'])))
                self.r+=1
            r2+=1                
        self.ui.tableWidget.setRowCount(self.r)
        self.ui.comboBox_cat.setCurrentIndex(0)
        
    def removeItem(self):
        i = 0;
        for item in data['items']:  #The same subparameter of all elements in the list
            if (self.ui.tableWidget.item(self.pressedValue,0).text() == item['name'] and
                self.ui.tableWidget.item(self.pressedValue,1).text() == item['type']):
                del(data['items'][i])
            i+=1
        self.loadDB()
        
    def editItem(self):
        self.pressedItem["name"] = self.ui.txt_add_name.toPlainText()
        self.pressedItem['type']= self.addCat
        self.pressedItem['sub-type']= self.ui.txt_add_subtype.toPlainText()
        self.pressedItem['Quantity']= int(self.ui.txt_add_qty.toPlainText())
        self.pressedItem['Location']= self.ui.txt_add_location.toPlainText()
        self.pressedItem['Unit price']= float(self.ui.txt_add_price.toPlainText())
        self.pressedItem['Datasheet']= self.ui.txt_add_data.toPlainText()
        self.pressedItem['Package']= self.ui.txt_add_package.toPlainText()
        self.pressedItem['Info'] = self.ui.txt_add_info.toPlainText()
        self.loadDB()
        
    def addItem(self):
        data['items'].append({
          "name": self.ui.txt_add_name.toPlainText(),
          "type": self.addCat,
          "sub-type": self.ui.txt_add_subtype.toPlainText(),
          "Quantity": int(self.ui.txt_add_qty.toPlainText()),
          "Location": self.ui.txt_add_location.toPlainText(),
          "Unit price": float(self.ui.txt_add_price.toPlainText()),
          "Datasheet": self.ui.txt_add_data.toPlainText(),
          "Package": self.ui.txt_add_package.toPlainText(),
          "Info": self.ui.txt_add_info.toPlainText()
        })
        self.loadDB()
    
    def addCatToDB(self):
        self.addCat = str(self.ui.comboBox_Add_Cat.currentText())
        
    def pressed(self, item):
        self.pressedValue = item.row()        
        for item in data['items']:  #The same subparameter of all elements in the list
            if (self.ui.tableWidget.item(self.pressedValue,0).text() == item['name'] and
                self.ui.tableWidget.item(self.pressedValue,1).text() == item['type']):
                self.ui.txt_add_name.setPlainText(item['name'])
                self.ui.txt_add_location.setPlainText(item['Location'])
                self.ui.txt_add_package.setPlainText(item['Package'])
                self.ui.txt_add_subtype.setPlainText(item['sub-type'])
                self.ui.txt_add_qty.setPlainText(str('%04i' % item['Quantity']))
                self.ui.txt_add_price.setPlainText(str('%.03f' % item['Unit price']))
                self.ui.txt_add_data.setPlainText(str(item['Datasheet']))
                self.ui.txt_add_info.setPlainText(str(item['Info']))
                self.ui.lineEdit_info.setText(str(item['Info']))
                index = self.ui.comboBox_Add_Cat.findText(item['type'], QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.ui.comboBox_Add_Cat.setCurrentIndex(index)
                self.pressedItem=item

    def OpenLink(self,item):
        for item in data['items']:  
            if (self.ui.tableWidget.item(self.pressedValue,0).text() == item['name'] and
                self.ui.tableWidget.item(self.pressedValue,1).text() == item['type']):
                webbrowser.open(str(item['Datasheet']))
        
    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Close',
                                                'Do you want to exit?',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print('Closed')
            sys.exit()
        else:
            pass

    def showInfo(self):
        QtWidgets.QMessageBox.information(self, "About the program",
                    "\t\t DAMASYS \n\r                          \
                    Database management system \n\r             \
                    Developed by Paulo S. S. dos Santos \n\r    \
                    Version 0.1.")

    def saveDB(self):
        with open('DB.json', 'w') as f:         #write to file
            json.dump(data, f, indent = 2)
        
    def loadDB(self):
        self.ui.tableWidget.setSortingEnabled(False)
        self.r=0
        r2=0        #local index for subtype presentation
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(data['items'])+1)
        for item in data['items']:
            if (self.ui.comboBox_cat.currentText() =='All'):
                self.ui.tableWidget.setItem( self.r,0, QtWidgets.QTableWidgetItem(str(data['items'][ self.r]['name'])))
                self.ui.tableWidget.setItem( self.r,1, QtWidgets.QTableWidgetItem(str(data['items'][ self.r]['type'])))
                self.ui.tableWidget.setItem( self.r,2, QtWidgets.QTableWidgetItem(str(data['items'][ self.r]['sub-type'])))
                self.ui.tableWidget.setItem( self.r,3, QtWidgets.QTableWidgetItem(str('%04i' % data['items'][ self.r]['Quantity'])))
                self.ui.tableWidget.setItem( self.r,4, QtWidgets.QTableWidgetItem(str(data['items'][ self.r]['Location'])))
                self.ui.tableWidget.setItem( self.r,5, QtWidgets.QTableWidgetItem(str('%.03f' % data['items'][ self.r]['Unit price'])))
                self.ui.tableWidget.setItem( self.r,6, QtWidgets.QTableWidgetItem(str(data['items'][ self.r]['Package'])))
                self.r+=1
            if (self.ui.comboBox_cat.currentText() == item['type']):
                self.ui.tableWidget.setItem( self.r,0, QtWidgets.QTableWidgetItem(str(data['items'][r2]['name'])))
                self.ui.tableWidget.setItem( self.r,1, QtWidgets.QTableWidgetItem(str(data['items'][r2]['type'])))
                self.ui.tableWidget.setItem( self.r,2, QtWidgets.QTableWidgetItem(str(data['items'][r2]['sub-type'])))
                self.ui.tableWidget.setItem( self.r,3, QtWidgets.QTableWidgetItem(str('%04i' % data['items'][r2]['Quantity'])))
                self.ui.tableWidget.setItem( self.r,4, QtWidgets.QTableWidgetItem(str(data['items'][r2]['Location'])))
                self.ui.tableWidget.setItem( self.r,5, QtWidgets.QTableWidgetItem(str('%.03f' % data['items'][r2]['Unit price'])))
                self.ui.tableWidget.setItem( self.r,6, QtWidgets.QTableWidgetItem(str(data['items'][r2]['Package'])))
                self.r+=1
            r2+=1                
        self.ui.tableWidget.setRowCount(self.r)
        self.ui.tableWidget.setSortingEnabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_()) 