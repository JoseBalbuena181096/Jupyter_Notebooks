#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:20:31 2019

@author: jose
"""
"""
Caracteristicas de la programacion Orientada a Objetos:
    
Abstraccion:
Se refiere a que un elemento pueda aislarse del resto de elementos y de su contexto 
para centrar el interes en lo que se hace y no cómo lo hace(caja negra).

Modularidad
Es la capacidad de dividir una aplicacion en partes mas pequeñas independientes y
reutilizables llamadas modulos.
Encapsulacion 
Consiste en reunir todos los elementos posibles de una entidad al mismo nivel de abstraccion
para aumentar la cohesión, contando con la posibilidad de ocultar los atributos de un objetos
(en python solo se ocultan en aparencia)

Herencia
Se refiere a que pueda heredar las caracteristicas de una clase superior para obtener
objetos similares. Se heredan tanto atributos como los métodos.Estos últimos pueden 
sobrescribirse para ser adaptados a las nesesidades de la nueva clase. Ala posibilidad de 
heredar atributos y metodos de varias clases se denomina Herencia Múltiple
    
Polimorfismo
Alude a la posibilidad de identificar de la misma forma comportamientos similares asociados 
a objetos distintos.La idea es que sigan la siempre la misma pautas aunque los objetos y los resultados 
sean otros.
"""
"""
Variables de clases y variables

En un lenguaje se crean objetos a partir de clase, un objeto es una instancia de una clase . Y de una misma
clase se pueden mantener activas en el programa más de una instancia al mismos tiempo

Una varable de clase es compartida por todas las instancias de una clase.Se define dentro de la clase(Se define dentro de las clase)
pero nunca dentro del metodo. Este tipo de variables no se utiliza con tanta frecuencia como las variables de instancia.

Una variable de instancia se define dentro de un metodo y pertenece a un objeto determinado de la clasee instanciada
"""
"""
Crear clases

Una clse consta de dos partes: un encabezado que comienza con el término class y seguido
del nombre de la clase(en singular ) y dos puntos(:) y un cuerpo donde se declaran atributos y
metodos:
"""
class NombreClase:
    'Texto para documentar la clase'
    varclase1="Variable clase1"
    def nombreMetodo1(self, var1):
        self.var1=var1
    def nombreMetodo2(self):
        self.var1+=1
"""
La documentacion de la clase se debe situar despues del encabezado
y justo antes del lugar donde se declaran las variables y metodos de la clase.

Desde cualquier lugar de un programa se puede acceder a la cadena de la cocumentacion
con atributo especial: NombreClase._doc_

"""
#%%
class Clase:
    pass
"""La declaracion pass indica que no se ejecutara ningún código.Sin embargo, esta clase
una vez definida permite que inicialicemos objetos de ella e incluso es posible realizar 
algunas operaciones elementales.

"""        
objeto1=Clase()#Crear objeto 1
objeto2=Clase()#Crear objeto 2
print(objeto1==objeto2)#Retorna False...
##Los objetos aunque sean de la misma clase son diferentes.
#%%
class Alumno:
    "Clase para alumnos"
    numalumnos=0
    sumanotas=0
    def __init__(self,nombre, nota):
        self.nombre=nombre
        self.nota=nota
        Alumno.numalumnos+=1
        Alumno.sumanotas+=nota
    def mostrarNombreNota(self):
        return(self.nombre,self.nota)
    def mostrarNumAlumno(self):
        return(Alumno.numalumnos)
    def mostrarSumaNotas(self):
        return(Alumno.sumanotas)
    def mostrarNotaMedia(self):
        if Alumno.numalumnos>0:
            return(Alumno.sumanotas/Alumno.numalumnos)
        else:
            return("Sin Alumnos")
"""
La clase Alumno consta de dos variables de clase(Alumno.numalumnos y 
Alumno.sumanotas) que son accesibles desde los metodos de la clase. Ademas 
sus valores son compartidos por todas las instancias que exista de esta clase

A continuacio, se declaran varios metodos(funciones) que incluyen como primer 
argumento a self que contiene la referencia del objeto especifico que llama
al método en momento dado. Con su valor es implicito cuando se llama a un metodo
no es necesario pazar este argumento

El metodo __init__() es especial porque se ejecuta automaticamente cada vez que 
se crea un nuevo objeto,Este método , que es opcional, se llama constructor
y se suele utilizar para inicializar las variables de las instancias(en este caso para 
inicializar las variables self.nombre y sel.nota)
El resto de los metodos se utiliza para acceder y mostrar el Valor de las 
variables de clase y de instancia. Por ultimo, el método mostrarNotaMedia() realiza un calculo
y después muestra su resultado  
"""            
##Crear objetos(instancia) de una clase

"""
Para crear instancias de una clase se llama a la clase por su propio
nombre pasando los argumentos que requiera el metodo constructor __init__ si existe
"""
alumno1=Alumno("Maria",8)
alumno2=Alumno("Carlos",6)
"""
Todos los argumentos se pasan escribiendolos entre parentesis y separados entre 
parentesis y separados por comas(",").El primer argumento self se omite porque su valor es una referencia
al objeto
y es implicito para todos los metodos
Accediendo a los atributos y llamandolos a los métodos
Para acceder a la variable de un objeto se indica el  nombre del objeto, seguido de un punto
y nombre de la variable
"""
print(alumno1.nombre)
print(alumno1.nota)
"""
Para acceder a la variable de un objeto se utiliza siemple la misma notacion para referirse al atributo
y despues del signo igual(=) se indica la nueva signacion:
"""
alumno1.nombre="Juana"
print(Alumno.numalumnos)
print(Alumno.sumanotas)
"""
Para llamar a un metodo se indica el nombre del objeto, seguido de un punto y el nombre del 
metodo.Si se requiere varios argumentos se pasa escribiendo entre parantesis, separados
por comas(",").Si no es nesesario pasar argumentos se añaden los parentesis vacios "()" al 
nombre del metodo.
"""
print(alumno1.mostrarNombreNota())
print(alumno2.mostrarNombreNota())
"""
Para suprimir un atributo 
"""
del alumno1.nombre
"""
Si a continuacion, se intenta acceder al valor del atributo borrado o se llama
a algún método que lo utilice, lo producirá la siguiente excepción 
"""
#print(alumno1.mostrarNombreNota())
#!/usr/bin/env python
import cv2
import numpy as np
import matplotlib.pyplot as plt
def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

image=cv2.imread("test_image.jpg")
lane_image=np.copy(image)
canny=canny(lane_image)
#from matplotlib plt
#cv2.imshow("thereshold",canny)
plt.imshow(canny)
#cv2.waitKey(0)
plt.show(0)