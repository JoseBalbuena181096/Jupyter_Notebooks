#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:36:47 2018

@author: jose
"""

"""
Aqui se explica como añadir argumentos avanzados a los scripts
"""
#los imports se añaden al principio del programa
import argparse
from modulo_importable import saludar_modulo,felicitar_modulo

def parsear_argumentos_avanzados():
    parser=argparse.ArgumentParser(description="Description del script")
    parser.add_argument("metodo",help="""Indica el metodo que se quiere usar.
                        Valores validos son saludar y felicitar
                        """,choices=["saludar","felicitar"])
    parser.add_argument("usuario",help="""Indica el usuario con el que se 
                        quiere interactuar
                        """)
    parser.add_argument("--capilizar",help="""capitalizar el nombre del usuario
                        """,action="store_true")
    argumentos=parser.parse_args()
    return argumentos
def main(argumentos):
    """
    Aqui ponemos la funcionalidad principal del script
    """
    nombre=argumentos.usuario
    if argumentos.capilizar:
        nombre=nombre.capitalize()
        print(nombre)
    if argumentos.metodo=="saludar":
        saludar_modulo(nombre)
    elif argumentos.metodo=="felicitar":
        felicitar_modulo(nombre)
        
if __name__=="__main__":
    #Esto solo se ejecuta con la ejecucion directa
    argumentos=parsear_argumentos_avanzados()
    print("Argumentos avanzados parseados al script",argumentos)
    main(argumentos)