# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:07:12 2022

@author: Administrador
"""

#creating a xlm file from .xlsm
#First, I need to import modules
#Openpyxl helps to interacting with excel files
#yattag, allows me to convert to HTML and xlm
from yattag import Doc, indent
import xlrd
from lxml import etree as et
import pandas as pd

#reading the excel file
raw_data = pd.read_excel(r"contable.xls")
#sheet = raw_data.sheet_by_index(0)
########################################
#starting to build the xml structure

##conver the columns to 

#1. Defining the root

root = et.Element('Importar')

#2. Define tag name

for row in raw_data.iterrows():
    root_tags = et.SubElement(root, 'Linea')
    #writting the tag names for each section













    
    #adding the row values
    
    Column_heading_1.text = str(row[1]["F_NUMERO_REG"])
    Column_heading_2.text = str(row[1]["F_TIPO_REG"])
    Column_heading_3.text = str(row[1]["F_SUBTIPO_REG"])
    Column_heading_4.text = str(row[1]["F_VERSION_REG"])
    Column_heading_5.text = str(row[1]["F_CIA"])
    Column_heading_6.text = str(row[1]["F_CONSEC_AUTO_REG"])
    Column_heading_7.text = str(row[1]["F350_ID_CO"])
    Column_heading_8.text = str(row[1]["F350_ID_TIPO_DOCTO"])
    Column_heading_9.text = str(row[1]["F350_CONSEC_DOCTO"])
    Column_heading_10.text = str(row[1]["F350_FECHA"])
    Column_heading_11.text = str(row[1]["F350_ID_TERCERO"])
    Column_heading_12.text = str(row[1]["F350_ID_CLASE_DOCTO"])
    Column_heading_13.text = str(row[1]["F350_IND_ESTADO"])
    Column_heading_14.text = str(row[1]["F350_IND_IMPRESION"])
    Column_heading_15.text = str(row[1]["F350_NOTAS"])

tree = et.ElementTree(root)
et.indent(tree, space="\t", level=0)
tree.write('trabajo_1.xml', encoding="utf-8")