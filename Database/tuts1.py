#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:41:05 2019

@author: pssantos
"""

from PyQt5 import QtWidgets, QtGui, QtCore
import json

with open('DB.json') as f:
    data = json.load(f)                         #Now data is a dictionary

#print(data)

#type(data['items'])      #is a list
#type(data['items'][0])   #is a dictionary

#
#for item in data['items']:  #All data in entry of the list
#    print(item)

data['items'].append({
  "name": "2n222d3",
  "type": "Transistor",
  "sub-type": "NPNa",
  "Quantity": 1031,
  "Location": "SMD1a",
  "Unit price": 0.1031,
  "Datasheet": "http://www.google.pta"
})



#for item in data['items']:  #The same subparameter of all elements in the list
##    print(item.get('name'))
#    print(item)
#    if ('23' in str(item.get('name'))):
#        print('Found it', item)
#        del item
##    item.get('type')
#    item.get('sub-type')
#    item.get('location')
#    item.get('name')
#    item.get('Datasheet')

#for item in data['items']:  #Delete subparameter of all elements
#    del(item['Datasheet'])

#new_string = json.dumps(data, indent = 2)   #indentation to increase visibility
#
#print(new_string)

#with open('DB.json', 'w') as f:         #write to file
#    data = json.dump(data, f, indent = 2)

    
#for (key,value) in data['items']:
#    print(key)
#    if value == '2n2223']
#print (listofK)


# equivalent version
# sorted_d
