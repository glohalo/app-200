# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:52:20 2022

@author: Administrador
"""


import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
from collections import Counter
#reading the xml file

tree = ET.parse(r'DOCUMENTO_CONTABLE.txt')
to_count = ET.parse('DOCUMENTO_CONTABLE.txt') #count the document
root = tree.getroot()
tag = root.tag
att = root.attrib
#print(root,'\n',tag,'\n',att)
  

#obtener las línes del xml
lineas = [] 
for child in root:
    print(child.tag, '\n', child.attrib)
    for subchild in child:
        if subchild.tag == "Linea":
            lineas.append(subchild)            
        #print("I am La verga")
        #print(subchild.tag, subchild.attrib, subchild.text)
       # for subsubchild in subchild:
          #  print(subsubchild.tag, subsubchild.attrib, subsubchild.text)

#almacenar los consecutvos de las lines 

# class Contable:
#     def __init__(self, consecutivo, tipo, sub_tipo, version):
#         self.consecutivo = consecutivo
#         self.tipo = tipo
#         self.sub_tipo = sub_tipo
#         self.version = version
#     def __str__(self):
        
#         return ("consecutivo: " + consecutivo 
#                 + ", tipo: " + tipo + ". sub tipo: " + sub_tipo 
#                 + ", version: " + version)

# class ContableV1(Contable):
#      def __init__(self, sub_tipo, version):
#          self.sub_tipo = sub_tipo
#          self.version = version
         
#      def V1_row(self):
#          '''
#          1. reading the excel file
#          2. import the rows from sheet 01

#          Returns rows name
#          -------
#          None.

#          '''
    
         
#          Data = pd.ExcelFile("contable.xls")
#          Data.sheet_names
         
#          for i in Data.sheet_names:
#              if i== 0:
#                  file = pd.read_excel(Data, sheet_name= i)
#                  filtered_file = file[7:38] 
#                # filtered_file.iloc[7:38, 0] for some weird reason
#                #I don't understand why don't works

              
        
#      def ValuesV1(self):
#          '''
#          Get the value of each item with the call
#          variables:
#              keys_list= values from filtered-file
#              values_list = list of values from the xml file

#          Returns a dict with the name + value
#          -------
#          None.

#          '''
#            #problema
#          values_list = [self.consecutivo, self.tipo, self.sub_tipo, self.version] #¿Los valores que tengo
#          #desde el xml?
#          #dict_V1 = dict()
         
            
        
        
# #def almacer_elem(item):
#     #print(item)
# #def trans_linea(linea):
    
    
# for linea in lineas:
#     consecutivo = linea.text[:7]
#     tipo = linea.text[7:10]
#     #contable1 = Contable(consecutivo, tipo, sub_tipo, version)
#     #print(contable1)
    
#     if tipo == "350":
#         sub_tipo = linea.text[11:13]
#         version = linea.text[13:15]
#         sheet1 = ContableV1(sub_tipo, version)
#         if sub_tipo == "00" and version == "01":
#             sheet1.V1_row()
#             sheet1.ValuesV1()
        
 
    

    #trans_linea(linea)
    

    
# for elem in to_count.iter():
#      print(elem)
            
# #Counting the tags. To the a dictionary with key the name and number of times 
# #as value
# def count_tags(to_count):
#     '''
#     With the function belows this will get a dictionary 
#     with the tag names as the key and number of times this tag 
#     is encountered in the XML file
    
#     '''
    
#     my_tags = []
#     for event in to_count.iter():
#         for element in event:
#             #print(event, '\n', element)
#             my_tags.append(element.tag)
#     my_keys = Counter(my_tags).keys()
#     my_values = Counter(my_tags).values()
#     #build the dict
#     my_dict = dict(zip(my_keys, my_values))
#     return my_dict 

# count_tags(to_count)

# tag = root.tag
# att = root.attrib
# #Flatten XML to CSV
# for child in root:
#     mainlevel = child.tag
#     xmltocsv = ''
#     for elem in root.iter():
#         if elem.tag == root.tag:
#             continue
#         if elem.tag == mainlevel:
#             xmltocsv = xmltocsv + '\n'
#         xmltocsv = xmltocsv + str(elem.tag).rstrip() + str(elem.attrib).rstrip() + ';' + str(elem.text).rstrip() + ';'
# #print(xmltocsv)

x = 30

if x<10:
    print('smaller')
if x>20:
    print('big number')
print('finished')
