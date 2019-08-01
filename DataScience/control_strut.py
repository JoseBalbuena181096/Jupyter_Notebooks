#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:35:11 2018

@author: jose
"""
"""
IF-ELSE 

Nosotros usamos  if-else para tomar decisiones y ejecutar 
diferentes partes de codigo en funcion de la condicion

"""
#%%La forma mas facil de implementar una evaluacion es con un if
temperature=25
if temperature <=20:
    print("Ponte una rebequita que refresca")
#si  toma diversas deciones condiciones en funcion de las condiciones
# una u otra
#%%
temperature=15
if temperature <=10:
    respuesta_abuela="Ponte un abrigo"
elif temperature <=20:
    respuesta_abuela="Ponte una rebequita que refresca"
elif temperature<= 30:
    respuesta_abuela="Merolico no vuelvas muy tarde"
else:
    respuesta_abuela="Ve por la sombra"
print(respuesta_abuela)
#%%Tambien se puede insertar un if dentro de otro if 
temperatura=25
lluvia=False
if 20 <=temperatura <30:
    if not lluvia:
        print("Vamos de picnic")
#%%
"""
Bucles for() (for loops)

Los bucles sirven para iterar entre los elementos de python que soporte 
una iteracion 
"""
numeros=[1,2,3,4,5,6,7,80,9,10]
for numero in numeros:
    if numero<=10:
        print(f"numero valido{numero}")
    else:
        print(f"Error! numeros mayor que 10")
#%%Hay veces que queremos romper un bucle for 
numeros=[1,2,3,4,5,6,7,80,9,10]
for numero in numeros:
    if numero<=10:
        print(f"numero valido{numero}")
    else:
        print(f"Error! numeros mayor que 10, saliendodel bucle")
        break
#%%
"""
Hay veces que en vez de  romper un bucle solo no hacemos nada, con pass
"""
numeros=[1,2,3,4,5,6,7,80,9,10]
for numero in numeros:
    if numero<=10:
        print(f"numero valido{numero}")
    else:
        pass
        #pass se usa simplemente en aquellos casos en los que hay que poner
        #algo en un segmento de codigo pero no hace nada
#%%
#Continue, al contrario de pass nos lleva directamente a lasigueinte iteracion
numeros=[1,2,3,4,5,6,7,88,9,10]
for numero in numeros:
    if numero <=10:
        print(f"numero {numero} valido")
    else:
        continue
        print("Esto no se va a imprimir")
#%%
#Hay una forma simplificada de iterar los elementos de una lista
[numero for numero in numeros if numeros<10]
#%%
inventario={
        "melocontones":3,
        "fresas":1,
        "manzanas":4
        }
#Podemos iterar las cave de un diccionario con for
for fruta in inventario:
    print(fruta)
#%%
#Podemos itear las claves y los valores de un diccionario a la vez en un bucle 
#for usando .items()
for fruta,cantidad in inventario.items():
    print("Tenemos {} kilos de {}".format(cantidad,fruta))
#%%No solo las listas son iterables sino tambien los strings 
nombre="Murcia"
for letra in nombre:
    print("Dame una {}!".format(letra))
#%%
"""
TRY-EXCEPT
En ocaciones los programas fallan lanzando una exepcion , pero una manera de 
poder hacer que un programa continue su funcion pese haber fallado es atrapado 
la exepcion en python se hace con el bloque try-except 

Importante: cuando atrapamos una excepcion
es importante por lo menos imprimir un mensaje de que el programa ha fallado 
de esta manera nos aseguramos que nuestro programa no esta fallando 
catastroficamente
"""
numero_str="10.5"
try:
    numero_int=int(numero_str)
except Exception as e:#Exception is a pyhton class
    print("Error el valor {} no se puede convertir a entero".format(numero_str))
    print("El mensaje de error ha sido")
    print(e,type(e))
#%%
"""
El problema de las capturas de errores de nuestros programas a ciegas es que 
podemos pasar errores que haga que todo falle de forma silenciosa, una manera 
mas efectiva de capturar errores es capturar aquellos que conozcamos, y fallar
en caso de un error que no conozcamos
"""
numero_str="10.5"
try:
    numero_int=int(numero_str)
except ValueError:# esto fallara para todo error que no sea un ValueError
    print("Error: el valor {} no se puede convertir a entero".format(numero_str))
#%%
"""
While 
Los bucles se siguen ejecutando mientras la condicion sigue ocurriendo
"""

n_elefante=2
print("1 elefante se balacea sobre la tela de una araña")
while n_elefante<=10:
    print("{} elefantes se balancea sobre la tela de una araña".format(n_elefante))
    #usar n_elefante +=1 equivale a n_elefante=n_elefante+1
    n_elefante+=1
#%%
"""
Hay que tener cuidadado al usar while, ya que podemos quedar atascado en un 
bucle infinito en python podemos pulsar ctrl + z para parar la ejecucion
"""
while 1<10:
    print("atascado en el loop!")
#%%
"""
Un uso comun de bucle while es validad el imput que nos esta dando un usiuario
podemos obtener el input de un usuario usando la funcion input
"""
while 1:
    input_users=input("Dime un numero del 1 al 10, 'exit' para salir: ")
    try:
        if input_users=="exit":
            print("Adios!")
            break
        elif int(input_users)<=10:
            cuadrado=int(input_users)**2
            print("El cuadrado del numero {} es {}".format(input_users,cuadrado))
        else:
            print("El valor {} no es un valor valido".format(input_users))
    except:
        print("Error: el valor {} no se puede convertir a entero".format(input_users))
#%%Ejercicios
#Dado el siguiente diccionario
dias_semana={
        "lunes":1,
        "martes":2,
        "miercoles":3,
        "jueves":4,
        "viernes":5,
        "sabado":6,
        "domingo":7
        }

dias_semana_mayusculas={}
for clave,valor in  dias_semana.items():
    dias_semana_mayusculas[clave.upper()]=valor
dias_semana=dias_semana_mayusculas
print(dias_semana)
#%%
dias_con_O=[]
for clave in dias_semana:
    if "O" in clave:
        dias_con_O.append(clave)
print(dias_con_O)