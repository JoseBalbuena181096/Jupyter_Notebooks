#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:53:13 2018

@author: jose
"""
#%%
#Clases en python
"""
Python es un lenguaje orientado a objetos,¿Eso se significa? que pese a que podemos 
programar de forma "funcional", esto es simplemente enviando datos a través de 
funciones ,muchas de las ventajas de pyton estan en sus clases

class Clase:
    def metodo(self): -->Todos los metodos de la clase toman self como primer argumento
        #metodo que tienen los objetos de la clase
    def metodo(self):
        #otro metodo que tienen los objetos de la clase
"""
#%%
#Por ejemplo la clase coche
class CocheBasico:
    def girar_izquierda(self):
        print("Turn left")
    def girar_derecha(self):
        print("Turn right")
    def aceleara(self):
        #Podemos usar pass cuando definimos una funcion para que no haga nada
        pass
    def frenar(self):
        pass
print(CocheBasico)
"""
Hemos generado una clase CocheBasico. Las clases se pueden considerar como plantillas
que se puede usar para generar objetos.Por ejemplo la plantilla (clase) Coche nos 
da las instruccione para fabricar un coche.
En jerga de desarrollo se llama "instanciar una clase" creamos una instancia 
(objeto) de la clase Coche.
"""
coche_de_manuel=CocheBasico()
print(coche_de_manuel)
#%%Este objeto coche es un Coche, es decir es un objeto de la Clase Cooche
print(type(coche_de_manuel)==CocheBasico)
#%%
#Este coche tambien tiene todas las caracteristicas de la clase coche
coche_de_manuel.girar_derecha()
coche_de_manuel.girar_izquierda()
coche_de_manuel.aceleara()
#%%
"""
Al igual que con las funciones, generalmente querremos que los objetos que 
creamos tengan unas caracteristicas definidas de forma variable.
Con la clase cpche temermos todos los coches que creamos seran 100 iguales 
¿Como podemos generar coches que tenga distinto color, por ejemplo?
Para eso podemos usar el metodo especial_init_ que se ejecuta cuando se crea un 
objeto de una clase.
"""
class CocheConColor:
    ##
    def __init__(self, color):
        self.color=color#Esto es un atributo de la clase
    def describir(self):
        print("Coche de color {}".format(self.color))
    def girar_izquierda(self):
        print("Turn left")
    def girar_derecha(self):
        print("Turn right")
    def aceleara(self):
        #Podemos usar pass cuando definimos una funcion para que no haga nada
        pass
    def frenar(self):
        pass
coche_rojo=CocheConColor(color="rojo")
coche_rojo.describir()
print(coche_rojo.color)
#%%  
#Tambie podemos añadir atributos a las instancias
coche_rojo.matricula="ER123"
print(coche_rojo.matricula)
##Ahora que hemos creado un CocheConColor tenemos que especificar un color
coche_sin_color=CocheConColor()
#%%
##Podemos evitar esto simplemente  indicando argumentos por defecto en el
#metodo __init__
class CocheConColor:
    def __init__(self,color="negro"):
        self.color=color
    def describir(self):
        print("Coche de color {}".format(self.color))
    def girar_izquierda(self):
        print("Turn left")
    def girar_derecha(self):
        print("Turn right")
    def aceleara(self):
        #Podemos usar pass cuando definimos una funcion para que no haga nada
        pass
    def frenar(self):
        pass
coche_sin_color=CocheConColor()
coche_sin_color.describir()
#%%
#De igual forma podemos definir las vatriables nesesarias para definir un objeto
class CocheVariable:
    def __init__(self,modelo,velocidad_maxima,color="negro"):
        self.color=color
        self.modelo=modelo
        self.velocidad_maxima=velocidad_maxima
        self.velocidad=0#Elcoche esta parado
    def describir(self):
        print("Coche modelo {}, color {} velocidad maxima {}".format(self.modelo,self.color,self.velocidad_maxima))
    def describir_estado(self):
        if self.velocidad==0:
            print("El coche esta parado")
        else:
            print("El coche va a una velocidad de {} kilometros".format(self.velocidad))
    def girar_izquierda(self):
        print("Turn left")
    def girar_derecha(self):
        print("Turn right")
    def acelerar(self):
        pass
    def frenar(self):
        pass
coche_manuel=CocheVariable(modelo="Ford",color="Azul",velocidad_maxima=1000)
coche_manuel.describir()
#%%
#Podemos en cualquier momento  cambiar los atributos de un objeto
coche_manuel.velocidad=100
coche_manuel.describir_estado()
#%%
"""
Uno de los usos principales de las clases es conservar el "estado" de un objeto,
si no usamos clases para almacenar la velocidad de un coche , tendriamos que
tener un diccionario como los identificadores de coches y su velocidad y cada vez qur cambiaramos la velocidad
tendriamos que cambiar los diccionarios
Ahora nos falta simplemente añadir las funciones para acelerar y tendremos un 
veiculo completo
"""
class Vehiculo:
    def __init__(self,modelo,velocidad_maxima,color="Negro"):
        self.color=color
        self.modelo=modelo
        self.velocidad_maxima=velocidad_maxima
        self.velocidad=0
    def describir(self):
        description="Vehiculo Modelo {},color {}, velocida_maxima {}".format(
                self.modelo,self.color,self.velocidad_maxima)
        return description
    #El metodo __repr__ es un metodo magico que se usa cuando queremos representar algo(con el metodo print)
    def __repr__(self):
        return self.describir()
    def decribir_estado(self):
        if self.velocidad==0:
            print("EL vehiculo esta parado")
        elif self.velocidad >0:
            print("EL vehiculo va a {} kilometros por hora".format(self.velocidad))
        else:
            print("El vehiculo va marcha atras {} kilometros por hora".format(self.velocidad))
    def girar_izquierda(self):
        print("Turn left")
    def girar_derecha(self):
        print("Turn right")
    def acelerar(self, diferencia_velocidad):
        print("Acelerando {} km/hr".format(diferencia_velocidad))
        #abs devuelve el valor absoluto de un numero
        self.velocidad+=abs(diferencia_velocidad)
        #min devuelve el valor minimo de una lista de numeros
        self.velocidad=min(self.velocidad,self.velocidad_maxima)
    def frenar(self,diferencia_velocidad):
        print("Frenando {}Km/h".format(diferencia_velocidad))
        self.velocidad-=abs(diferencia_velocidad)
        #max nos devuelve el maximo valor de una lista de numeros
        self.velocidad=max(self.velocidad,-5)
        
coche_manuel=Vehiculo(modelo="Jeta",color="Blue",velocidad_maxima=300)
coche_manuel.decribir_estado()
coche_manuel.acelerar(20)
coche_manuel.decribir_estado()
#%%
coche_manuel.acelerar(20)
coche_manuel.decribir_estado()
#%%
coche_manuel.frenar(60)
coche_manuel.decribir_estado()
coche_manuel.acelerar(5)
coche_manuel.decribir_estado()
print(coche_manuel)
#%%%
"""
Herencia de clases
Una de las principales caracteristicas de usar clases es que se puede crear clases usando
como plantillas otras clases( se dice que una clase "hereda" de otra)
Esto nos permite crear una clase base con funciones genericas
y despues crear una clase avanzada con diversas funciones especificas

Por ejemplo podemos crear una clase Autobus que no tine marcha atras y tiene un limite de velocidad de 100
"""
class Autobus(Vehiculo):
    def acelerar(self,diferencia_velocidad):
        print("Autobus acelerando {}km/h".format(diferencia_velocidad))
        ##abs es un metodo que devueve el valor absoluto de un numero
        self.velocidad+=abs(diferencia_velocidad)
        self.velocidad=min(self.velocidad,100)
    def frenar(self,diferencia_velocidad):
        print("Autobus frenando {}Km/h".format(diferencia_velocidad))
        self.velocidad-=abs(diferencia_velocidad)
        #max nos devuelve el maximo valor de una lista de numeros
        self.velocidad=max(self.velocidad,0)
autobus_urbano=Autobus(modelo="Mercedes",color="Blue",velocidad_maxima=180)
autobus_urbano.decribir_estado()
autobus_urbano.acelerar(80)
autobus_urbano.decribir_estado()
autobus_urbano.acelerar(10)
autobus_urbano.decribir_estado()
autobus_urbano.frenar(120)
autobus_urbano.decribir_estado()
#%%Ejercicios de clases
"""
Ejercicio 
Crear una clase Taxi que herede de Vehiculo, y que pueda cobrarnos un trayecto 
Tiene que tener un atributo "distancia_recorrida", los tres metodos adicionales:
-Metodo "cobrar" donde se imprime la cantidad a cobrar (3 euros por Kilometro)

-Metodo "añadir_distancia" donde se suma la distancia recorrida un numero de kilometros 
-Metodo "añadir_tiempo" donde dado un tiempo (en horas) se añade distancia en 
funcion de la velocidad
"""
class Taxi(Vehiculo):
    def __init__(self,modelo,velocidad_maxima):
        self.color="blanco"
        self.modelo=modelo
        self.velocidad_maxima=velocidad_maxima
        self.velocidad=0
        self.distancia_recorrida=0
        self.tarifa=3
    def cobrar(self):
        print("El total es {} euros".format(self.distancia_recorrida*self.tarifa))
    def añadir_distancia(self,distancia):
        self.distancia_recorrida+=distancia
    def añadir_tiempo(self,tiempo):
        self.añadir_distancia(tiempo*self.velocidad)
taxi=Taxi(modelo="Mercedes Benz",velocidad_maxima=120)
taxi.acelerar(100)
taxi.añadir_tiempo(1)
taxi.añadir_tiempo(5)
taxi.cobrar()
#%%%
class Taxi2(Vehiculo):
    #*args,**kwargs Significa que el metodo constructor toma cualquier tipo de dato como argumento
    def __init__(self,tarifa,*args,**kwargs):
        #El metodo super ejecuta el metodo __init__ de la clase padre
        super().__init__(*args,**kwargs)
        self.distancia_recorrida=0
        self.tarifa=tarifa
    def cobrar(self):
        print("El total es {}".format(self.distancia_recorrida*self.tarifa))
    def añadir_distancia(self,distancia):
        self.distancia_recorrida+=distancia
    def añadir_tiempo(self,tiempo):
        self.añadir_distancia(tiempo*self.velocidad)
taxi=Taxi2(modelo="Mercedez",velocidad_maxima=120,tarifa=2,color="Blanco")
taxi.acelerar(100)
taxi.añadir_tiempo(1)
taxi.añadir_tiempo(5)
taxi.cobrar()
#%%
"""
Ejercicio 2
Crear una clase Parking, donde pueda aparcar un limite determinado de vehiculos
(solo vehiculos)
Y donde pueda validar si un vehiculo esta aparcado o no
"""
class Parking:
    def __init__(self,capacidad):
        self.capacidad=capacidad
        self.vehiculos=[]
    def nivel_ocupacion(self):
        return len(self.vehiculos)/self.capacidad
    def __repr__(self):
        return "Parking con capacidad {}.Nivel de ocupacion {:.2f}".format(self.capacidad,self.nivel_ocupacion())
    def aparcar_vehiculo(self,vehiculo):
        if not type(vehiculo)==Vehiculo or vehiculo in self.vehiculos:
            print("Solo se aceptan vehiculos que no estan aparcados")
        elif len(self.vehiculos)<self.capacidad:
            print("Aparcando vehiculo {}".format(vehiculo))
            self.vehiculos.append(vehiculo)
    def sacar_vehiculo(self,vehiculo):
        if vehiculo in self.vehiculos:
            print("Sacando el vehiculo {}".format(vehiculo))
            self.vehiculos.pop(self.vehiculos.index(vehiculo))
        else:
            print("Vehiculo no esta aparcadp".format(vehiculo))
parking_glorieta=Parking(capacidad=100)

coche_manuel=Vehiculo(modelo="Nissan",color="Blue",velocidad_maxima=100)

coche_rojo=Vehiculo(modelo="Nissan",color="red",velocidad_maxima=130)
taxi=Taxi(modelo="Ford",velocidad_maxima=110)

parking_glorieta.aparcar_vehiculo(coche_manuel)
parking_glorieta.aparcar_vehiculo(coche_rojo)
parking_glorieta.aparcar_vehiculo(taxi)

print(parking_glorieta)
parking_glorieta.sacar_vehiculo(coche_rojo)
print(parking_glorieta)
