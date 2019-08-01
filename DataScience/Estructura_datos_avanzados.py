#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:21:44 2018

@author: jose
"""
"""
SETS
Los sets son conjunto de elementos no repetidos 
sirven para dos funciones principales 
"""
#Los sets sepueden crear apartir de listas
grupo_amigos1=set(["Manuel","Rodrigo","Miguel","Jesus","Pedro"])
print(type(grupo_amigos1))
#%%
#Tambien se pueden crear con llaves {}
grupo_amigos2={"Manuel","Alejandro","Fernando","Antonio","Lazaro"}
#%%
#Los sets se usan para evaluar pertenencia de un elemento en un grupo
print("Manuel"in grupo_amigos1)
#%%
#Los sets se pueden ver elementos en  comun o dispares de los mismos 
todos_amigos=grupo_amigos1.union(grupo_amigos2)
print(todos_amigos)

amigos_comunes=grupo_amigos1.intersection(grupo_amigos2)
print(amigos_comunes)

amigos_exclusivos_grupo1=grupo_amigos1-grupo_amigos2
print(amigos_exclusivos_grupo1)

#%%
#Se pueden añadir o quitar elementos de un set
avengers={"Iron Man","Thor","Hulk","Viuda Negra","Capitan America","Ojo de alcon"}
avengers.add("Spiderman")
print(avengers)
avengers.remove("Ojo de alcon")
print(avengers)
#%%
#LOs set sirven para eliminar los elementos repetidos de una lista
avengers_repetidos=["Iron_Man","Hulk","Thor","Iron_Man","Hulk","Thor"]
print(avengers_repetidos)
avengers_unicos=list(set(avengers_repetidos))
print(avengers_unicos)
#%%
#Se pueden comparar sets
set1={"strawberries","apples"}
set2={"strawberries","apples"}
print(set1==set2)
#%%
#Un set es mas grande que otro si contiene todos los elemtos del primero mas 
#un elemto mas
set3={"strawberries","apples","bananas"}
print(set3>set2)
set4={"blackberry","apples"}
print(set3>set4)
#%%
#Counter
#La clase Counter sirve para contar cosas
from collections import Counter
votos=[
       "PODEMOS",
       "PSOE",
       "PSOE",
       "PODEMOS",
       "PP",
       "PSOE",
       "PP",
       "PP",
       "PP",
       "PODEMOS",
       "PSOE",
       "PP",
       "CIUDADANOS",
       "PSOE",
       "PODEMOS",
       "PODEMOS",
       "PODEMOS",
       "PODEMOS"
       ]
recuento_votos=Counter(votos)
print(recuento_votos)
#%%
#podemos ver el numero de veces que un elemento en particular aparece
recuento_votos["PP"]
#%%
#si un elemento no existe, devuelve un cero
recuento_votos["UPyD"]
#%%
#Se pueden añadir elemetos a un Counter dinamicamente
print(recuento_votos["CIUDADANOS"])
recuento_votos.update(["CIUDADANOS"])
print(recuento_votos["CIUDADANOS"])
#%%
#Tambien se puede aumentar el recuento usando un diccionario
recuento_votos.update({"CIUDADANOS":5,"PODEMOS":7})
print(recuento_votos)
#%%
#Tambie podemos especificar directamente el recuento de un elemento
recuento_votos["UPyD"]=1
print(recuento_votos)
#%%
"""
Defaultdict
La clase defaultdict nos permite crear diccionarios que permiten devolver un valor
por defecto si una clave no existe
defauldict se inicia pasandole una funcion que iniciara un valor a devolver en 
caso de no existir la clave especificada
DefaultDict no existe como primitivo de python, si no que esta como modulo 
collections por lo que hay que importar 
"""
from collections import defaultdict
#Esto va a fallar porque vainilla no es una funcion
sabores_helado=defaultdict("vainilla")
#%%
sabores_helado=defaultdict(lambda:"vainilla")
print(sabores_helado)
#%%
sabores_helado["Manuel"]="chocolate"
print(sabores_helado["Manuel"])
#maria no es una clave existente porlo que devuelve un valor por defecto
print(sabores_helado["Maria"])
#%%
#Tambien podemos ccrear defaultdict a partir de un diccionario
sabores_helado_dict={
        "Manuel":"chocolate",
        "Maria":"fresa"
        }
sabores_helado=defaultdict(lambda:"vainilla",sabores_helado_dict)
print(sabores_helado)
#%%
"""
Un uso muy comun de defaultlist es cusndo tenemos un conjunto de elementos donde
cada elemento tiene multiples caracteristicas , y queremos hacer un diccionario para 
poder obtener rapidamente su lista de caracteristicas.
"""
pockemon_entrenador_lista=[
        ["Ash","Nidorian"],
        ["Ash","Charmander"],
        ["Ash","Pickachu"],
        ["Misty","Squirtle"],
        ["Misty","Rattata"],
        ["Misty","Jigglypuff"],
        ["Brock","Charmander"],
        ["Brock","Nidorian"]
        ]
pockemos_por_entrenador=defaultdict(list)
for entreandor,pockemon in pockemon_entrenador_lista:
    pockemos_por_entrenador[entreandor].append(pockemon)
pockemos_por_entrenador
#%%
"""
Ejercicios 
"""
#%%
#Convertir la lista pockemon entrenadores en lista de diccionarios con las 
#claves "entrenador" y "pockemon"
pockemon_entrenador_lista=[
        ["Ash","Nidoria"],
        ["Ash","Chanderman"],
        ["Ash","Pickachu"],
        ["Misty","Pickachu"],
        ["Misty","Squirtle"],
        ["Misty","Ratta"],
        ["Brock","Nidoria"],
        ["Brock","Singglypuff"]
        ]
pockemon_entrenadores_dict=[]

for lista in pockemon_entrenador_lista:
    pockemon_entrenadores_dict.append({"entrenador":lista[0],"pockemon":lista[1]})
pockemon_entrenadores_dict
#%%Otra forma seria
pockemon_entrenadores_dict=[]
for entrenadores,pockemones in pockemon_entrenador_lista:
    pockemon_entrenadores_dict.append({"entrenador":entrenadores,"pockemon":pockemones})
pockemon_entrenadores_dict
#%%
from collections import Counter
def contador_letras(frase):
    contador=Counter([letra for letra in frase if letra not in " ,.\n"])
    print(contador)
    return contador.most_common(5)
contador_letras("Pepe pica papas")
#%%
"""
Crear una funcion que dados dos listas devuelva su coeficiente de Jaccard la
cual es una medida de similaridad entre dos grupos y se define como  el numero 
de elementos en los dos grupos entre el numero de elementos de un gupo en otro
"""
def jaccard(grupo1,grupo2):
    union=len(set(grupo1).union(set(grupo2)))
    interseccion=len(set(grupo1).intersection(set(grupo2)))
    return interseccion/union
grupo_amigo1=["Manuel","Rodrigo","Miguel","Jesus","Pedro"]
grupo_amigos2=["Manuel","Alejandro","Fernando","Antonio","Lazaro"]
jaccard_friends=jaccard(grupo_amigo1,grupo_amigos2)
print(jaccard_friends)