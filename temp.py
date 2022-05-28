# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#this s the file for conver to cvs
import pandas as pd
import csv
#read the file ussing pandas
x1 = pd.ExcelFile('contable.xls')
#reading the sheet names
x1.sheet_names
#loop for all the sheet names into the xlsx file
for i in x1.sheet_names:
    #reading the sheet wise with pd.read_excel
    file = pd.read_excel(x1, sheet_name=i)
    filtered_file = file[7:38]
    #by giving a .csv extension
    #hoja = filtered_file.to_csv(i+'.csv', index=False, header=False)
    
    
    
    
    
    #file.to_csv (r'Hoja 1.txt', index = None, header=True)
    # Column_heading_1 = et.SubElement(root_tags, "F_NUMERO_REG")
    # Column_heading_2 = et.SubElement(root_tags, "F_TIPO_REG")
    # Column_heading_3 = et.SubElement(root_tags, "F_SUBTIPO_REG")
    # Column_heading_4 = et.SubElement(root_tags, "F_VERSION_REG")
    # Column_heading_5 = et.SubElement(root_tags, "F_CIA")
    # Column_heading_6 = et.SubElement(root_tags, "F_CONSEC_AUTO_REG")
    # Column_heading_7 = et.SubElement(root_tags, "F350_ID_CO")
    # Column_heading_8 = et.SubElement(root_tags, "F350_ID_TIPO_DOCTO")
    # Column_heading_9 = et.SubElement(root_tags, "F350_CONSEC_DOCTO")
    # Column_heading_10 = et.SubElement(root_tags, "F350_FECHA")
    # Column_heading_11 = et.SubElement(root_tags, "F350_ID_TERCERO")
    # Column_heading_12 = et.SubElement(root_tags, "F350_ID_CLASE_DOCTO")
    # Column_heading_13 = et.SubElement(root_tags, "F350_IND_ESTADO")
    # Column_heading_14 = et.SubElement(root_tags, "F350_IND_IMPRESION")
    # Column_heading_15 = et.SubElement(root_tags, "F350_NOTAS")