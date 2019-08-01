#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 02:01:31 2018

@author: jose
"""
#Inputs/Outputs
"""
Aqui se explica como leer y escribir archivos
"""
"""
Creacion de carpetas
"""
#Podemos crear directorios con  el metodo os.makedirs()
import os
#crear directorios en la carpeta actual
os.makedirs("./data/nombres/",exist_ok=True)
#%%%
"""
Listado de archivos
"""
#Crear una lista de los directorios en el que esta este archivo
archivos_carpeta_actual=os.listdir(".")
print(archivos_carpeta_actual)
#%%
"""
Escritura de archivos
"""
"""
Podemos usar open() para abrir archivos si un archivo no exixte marcara un error
"""
archivo_inexistente=open("./data/nombres/usuarios.txt")
#%%
"""
Si queremos crear un archivo para escribir podemos espesificar el metodo de 
escritura "w"
"""
archivo_para_escribir=open("./data/nombres/usuarios.txt","w")
archivo_para_escribir.write("Hola")
archivo_para_escribir.write("Mundo")
#%%No se escribe nada hasta cerrar el archivo
archivo_para_escribir.close()
#%% Podemos usar el metodo "w" para sobrescribir el archivo
archivo_para_escritura=open("./data/nombres/usuarios.txt","w")
archivo_para_escritura.write("Hola")
archivo_para_escritura.write("Mundo2")
archivo_para_escritura.close()
#%%
#Podemo utilizar el metodo "a" de escritura sin borrar el contenido del archivo 
#original
archivo_para_escribir=open("./data/nombres/usuarios.txt","a")
archivo_para_escribir.write("Hola")
archivo_para_escribir.write("Mundo3")
archivo_para_escribir.close()
#%%
"""
El metodo open, close no es ideal, basicamente porque si ocurre un error entre 
los dos metodos podemos perder el archivo
"""
usuarios=["Manual","Juan","Pedro","Jose"]
with open("./data/nombres/usuarios.txt","w") as fname:
    for usuario in usuarios:
        fname.write(usuario)
        
#%%Si quereremos escribir cada elemento de la lista en forma de lista 
#escribimos salto de linea
usuarios=["Manual","Juan","Pedro","Jose"]
with open("./data/nombres/usuarios.txt","w") as fname:
    for usuario in usuarios:
        fname.write(usuario)
        fname.write("\n")
"""
Lectura de archivos
"""
with open("./data/nombres/usuarios.txt") as fname:
    datos=fname.read()
    print(datos)
    print(type(datos))
"""
Si queremos separar los usuarios debemos separar el texto en lineas para
evitar consumir memoria se ocupa readlines() que en vez de leer todo el 
texto de una sola vez lo lee de forma iterativa
"""
usuarios_desde_archivo=[]
with open("./data/nombres/usuarios.txt") as fname:
    lineas=fname.readlines()
    for linea in lineas:
        usuarios_desde_archivo.append(linea.strip("\n"))
print(usuarios_desde_archivo)
type(usuarios_desde_archivo)
#%%
"""
Usando PATHLIB
En windows las carpetas se definen con \ mientras que en linux o mac se usa /
Esto puede generar errores
Una manera que podemos acceder a archivos independientemente al sistema 
operativo que manejamos es el modulo pathlib(disponible en python 3.6)
"""
from pathlib import Path
carpeta=Path("./data/nombres/")
archivo=carpeta / "usuarios.txt"
print(type(archivo))
archivo.read_text()
#%%
#Con path podemos escribir facilmente en un archivo
carpeta=Path("./data/nombres/")
archivo=carpeta/"usuarios_2.txt"
archivo.write_text("Hola")
print(archivo.read_text())
#%%Para poder añadir texto al final del archivo seguimos nesesitando
usuario=["Manuel","Pedro","Juan"]
carpeta=Path("./data/nombres/")
archivo=carpeta/"usuarios_2.txt"
with open(archivo,"a") as fname:
    for usuario in usuarios:
        fname.write(usuario)
        fname.write("\n")
print(archivo.read_text())
#%%
#Ejercicios 
"""
Hacer una funcion que dado el nombre de una archivo lo lea y devuelva la linea 
con mayor longitud
"""
import os
def linea_mas_larga(nombre):
    with open(nombre,"r") as fname:
        lineas=[linea.strip("\n") for linea in fname.readlines()]
        print(lineas)
        linea_mas_larga=lineas[0]
        for linea in lineas:
            if len(linea)>len(linea_mas_larga):
                linea_mas_larga=linea
        return linea_mas_larga
linea_mas_larga("./data/nombres/usuarios.txt")
#%%
"""
Hacer una funcin que tenga como argumento un nombre de un archivo y un numero n 
y devuelva las n ultimas lineas
"""
def leer_n_ultimas(nombre,n):
    with open(nombre,"r") as fname:
        lineas=[linea.strip("\n") for linea in fname.readlines()]
        return lineas[-n:]
leer_n_ultimas("./data/nombres/usuarios.txt",2)
#%%
"""
Hacer una funcion que dado un diccionario cree un archivo csv el cual tiene que
acabar en csv con los datos del mismo 
Los archivos csv (comma -separed-values)  son una forma de separar datos de 
cada columna por una coma
Por ejemplo si tenemos un diccionario 
{
"nombre":["Antonio","Juan","Pedro"],
"edad":[45,23,78],
"ciudad":["Murcia","Almeria","Madrid"]
}
Dicho diccionario se convertiria en formato csv
nombre,edad,ciudad
Antonio,45,"Murcia"
Juan,23,Almeria
Pedro,78,Madrid
"""
import os
datos={
       "nombre":["Antonio","Miguel","Julia","Andres"],
       "edad":[45,90,22,34],
       "Ciudad":["Murcia","Almeria","Balcelona","Madrid"]      
       }
def dict_a_csv(datos,nombre):
    claves=list(datos.keys())
    n_items=len(datos[claves[0]])
    with open(nombre,"w") as fname:
        fname.write(",".join(claves))
        fname.write("\n")
        for i in range(n_items):
            fila=",".join([str(datos[clave][i])for clave in claves])
            fname.write(fila)
            fname.write("\n")
dict_a_csv(datos,"./data/nombres/nombres.csv")
