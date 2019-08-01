#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:54:23 2018

@author: jose
"""
"""
Listas son conjuntos de elementos ordenados donde cada elemento tiene una \
posicion 
"""
#%%
fruits=["orange","apple","pear","strawberry"]
print(fruits)
print(type(fruits))
#%%
"""
Accedemos a los elementos de una lista con [] el indice de los elementos de\
una lista comienza con 0, eso quiere decir que se accede al primer elemento con 
[0]
"""
print(fruits[0])
#%%Podemos acceder a un rango de elementos desde el 2 hasta el final
print(fruits[:2])
#%%Accedemos a los elemntos desde el 2 hasta el final
print(fruits[2:])
#%%
"""
Podemos acceder a los ementos empezando por el final accediendo con \
numeros negativos Por ejemplo accediendo a los ultimos dos elementos
"""
print(fruits[-2:])
#%%
#Podemos saltarmos elementos de n en n usando [::n],por ejemplo los\
#elementos impares
print(fruits[::2])
#%%Si el orden es un numero negativo nos devolverá la lista en sentido inverso
print(fruits[::-1])
#%%Podemos ver el numero de elementos de una lista con len
print(len(fruits))
##podemos añadir elemntos a la lista con el metodo append modificando la lista
##original
fruits.append("melon")
print(fruits)
#%%Podemos repetir una lista multipolicando la por un numero
print(fruits*2)
#%%Podemos concatenar listas con el simbolo +
citys=["Muicia","Cartagena"]
print(fruits+citys)
#%%podemos modificar los elementos de una lista
fruits[0]="mango"
print(fruits)
#%%Podemos alargar la lista sin importar el tamaño de la lista
fruits[3:]=["grape","fig","watermelon","grapefruit"]
print(fruits)
#%%
print(fruits)
print("grape"in fruits)
print("potatoe"in fruits)
#%%We can search the position of a item in the list
fruits=["orange","apple","pear","strawberry"]
print(fruits)
print("The position in the list of the word pear is {}".format(fruits.index("pear")))
#%%We can delate a item in the list with the method pop
fruits.pop(2)
print(fruits)
#%%Combined index and pop we can delate a concrete item in the list
fruits[3:]=["orange"]
fruits.pop(fruits.index("orange"))
print(fruits)
#%%
#The list can order with the method sort()
ages=[23,33,10,54,65,34,25]
ages.sort()
print(ages)
#%%
fruits=["orange","apple","pear","strawberry"]
fruits.sort()
print(fruits)
#%% 
#We can generate list of number with the funtion range()
print(list(range(10)))
#A object range isn't a list
type(range(10))
#%%#We can access to string in the same way like a list
nombre="Murcia"
print(nombre[0])
#Aprtir del elemento 2
print(nombre[2:])
#%%
"""
Tuplas(TUPLES)
They are list that we can't modify
"""
musketeers=("Athos","Porthos","Aramis")
print(type(musketeers))
print(musketeers[2:])
#No is possible do it in one tuple
musketeers[3]="D'artagnan"
#%%Dictionaries
"""
The dictionaries are a set of key associate to value 
Knowing a key we can find the value of the said key
"""
inventory={
        "melons":3,
        "strawberrys":2,
        "apples":5
        }
print(type(inventory))
print(inventory)
#%%We can see the keys that a dictonary has with the method .keys()
print(inventory.keys())
#convert to list
list_keys=list(inventory.keys())
print(list_keys)
#%%The method keys() doesn't return a list if we want to access to keys like 
##a list we have to convert they to list
print(list(inventory.keys())[0])
#We can see the values of dictionary with the method value()
print(inventory["strawberrys"])
#if the key does't exist, it will give us an KeyError error
print(inventory["pear"])
#%%We can evaluate if a key exist in a dictionary of easy way
print("melons"in inventory)
print("pear"in inventory)
#%%We can delete a key in a dictionary with pop()
kilos_strawberrys=inventory.pop("strawberrys")
print("We have {} kilos of strawberrys".format(kilos_strawberrys))
print(inventory)
#%%Every type of data structure can store to the others
#A list with list within
list_way=[
        ["Murcia","Valencia"],
        ["Muicia","Alicante"],
        ["Albacete","Granada"]
        ] 
print(list_way[0][1])
#%% Dictionary with tuplas like values
dict_way={
        "Murcia":("Valencia","Alicate"),
        "Albacete":("Valencia","Granada")
        }
print(dict_way["Murcia"])
#%%
#A list that contains dictionaries
list_dictionaries=[
        {"origin":"Murcia","destination":"Alicante"},
        {"origin":"Albacete","destination":"Granada"}
        ]
print(list(list_dictionaries[0]))
#Add items to dictionaries
days_week={"Mondey":1,"Tuesday":2,"Wednesday":3}
days_week["Thursday"]=4
print(days_week)
#Note for add item to list we need the method append(item)
#Exercise
#%%
week_days={
        "Monday":1,
        "Tuesday":2,
        "Wednesday":3
        }
print(week_days)
week_days["MONDAY"]=week_days.pop("Monday")
week_days["TUESDAY"]=week_days.pop("Tuesday")
week_days["WEDNESDAY"]=week_days.pop("Wednesday")
print(week_days)