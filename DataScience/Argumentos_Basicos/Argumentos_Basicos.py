#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:41:53 2018

@author: jose
"""
#Los imports se añaden al principio de un script
import sys 
from modulo_importable import saludar_modulo

def parsear_argumentos_basicos():
    argumentos=sys.argv[1:]
    return argumentos

def main(argumentos):
    """
    Aqui ponemos la funcionalidad principal de nuestro
    script
    """
    #Si el primer argumento pasado es saludar
    if argumentos[0]=="saludar":
        #Tomamos el segundo argumento pasado 
        nombre=argumentos[1]
        saludar_modulo(nombre)
if __name__=="__main__":
    #Este codigo solo se ejecutara si ejecutamos ejecutamos directamente
    argumentos=parsear_argumentos_basicos()
    print("Argumentos pasados al script",argumentos)
    main(argumentos)