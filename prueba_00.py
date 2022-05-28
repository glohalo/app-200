# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 10:16:56 2022

@author: Administrador
"""
#importing the libreries
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
from bs4 import BeautifulSoup
import pandas as pd
#the main class: read de documents, and create the head of the xml file
class Pedido:
    def __init__(self, Data_init, Data_body, Data_final):
        self.Data_init = inicio
        self.Data_body = body
        self.Data_final = final
        
    def head(self):
        """Returns the head of the xml file: roots and childs and the 
        pretty-printed XML string for the Element
        """
        root = ET.Element("Importar")
        comment = ET.Comment("Prueba")
        root.append(comment)
        child_conexion = ET.SubElement(root, "NombreConexion")
        child_conexion.text = ("JAB")
        child_cia = ET.SubElement(root, "IdCia")
        child_cia.text = "1"
        child_usuario = ET.SubElement(root, "Usuario")
        child_usuario.text = "Jabm"
        child_clave = ET.SubElement(root,"Clave")
        child_clave.text = "944915530"
        child_datos = ET.SubElement(root, "Datos")
        ET.SubElement(child_datos, "Linea").text = "{}{}{}{}{}".format(str(inicio['Campo Fijo'][0]).zfill(7), 
                                    str(inicio['Campo Fijo'][1]).zfill(4),
                                    str(inicio['Campo Fijo'][2]).zfill(2), 
                                    str(inicio['Campo Fijo'][3]).zfill(2),
                                    str(inicio['Campo Fijo'][4]).zfill(3))
        #I used the number because I can't edit the document
        ET.SubElement(child_datos, "Linea").text = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{} {}{} {}".format("0000002", 
                                    str(body['Campo Fijo'][1]),
                                    str(body['Campo Fijo'][2]).zfill(2), 
                                    str(body['Campo Fijo'][3]).zfill(2),
                                    str(body['Campo Fijo'][4]).zfill(3),
                                    str(body['Campo Fijo'][5]), 
                                    str(body['Campo Fijo'][6]),
                                    str(body['Campo Fijo'][7]),
                                    str(body['Campo Fijo'][8]),
                                    str(body['Campo Fijo'][9]),
                                    str(body['Campo Fijo'][10]).zfill(8),
                                    str(body['Campo Fijo'][11]),
                                    str(body['Campo Fijo'][12]),
                                    str(body['Campo Fijo'][13]),
                                    str(body['Campo Fijo'][14]),
                                    str(body['Campo Fijo'][15]),
                                    str(body['Campo Fijo'][16]).zfill(3),
                                    str(body['Campo Fijo'][17]),
                                    str(body['Campo Fijo'][18]).zfill(3))
        tree = ET.ElementTree(root)
        tree.write("prueba_00.xml")
        

inicio = pd.read_excel("inicio.xlsx")
body = pd.read_excel("Pedidos versio╠ün 02.xlsx") 
final = pd.read_excel("final.xlsx")

t = Pedido(inicio, body, final)   
