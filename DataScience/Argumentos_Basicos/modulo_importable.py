#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:50:57 2018

@author: jose
"""
#Modulo importable
"""
Aqui se puede poner codigo que se importa desde 
otro script que se hace mas largo, conviene agrupar
distintos trozos de logica en diversos archivos(modulos)
"""
def saludar_modulo(nombre):
    print("Hola {}, esta funcion se ha importado del modulo {} , {}".format(nombre,__file__,__name__))
def felicitar_modulo(nombre):
    print("Felicidades {}".format(nombre))
def main():
    saludar_modulo("Tu")
if __name__=="__main__":
    main()
    