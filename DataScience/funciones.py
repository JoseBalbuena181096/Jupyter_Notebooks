#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:09:56 2018

@author: jose
"""
#%%
#FUNCIONES
"""
Los scripts de python se ejecutan linea a linea 
las funciones son formas de separar la logica del programa
en piezas sin tener que estar ejecutando linea a linea , permite reutilizar
partes del codigo que se repiten

Las funciones se definen como:
    def nombre_de_funcion(argumento1,argumento2,...)
        logica_de_funcion
"""
#%%
def saludar():
    print("Hola mundo!")
#Al crear  la funcion saludar no tenemos que escribir print cada vez
print(type(saludar))
saludar()
saludar()
#%%
#La principal utilidad de las funciones es que permite usar argumentos y
# da flexibilidad  a la logica del codigo
def saludar(nombre):
    print(f"Hola {nombre}, ¿Como estas?")

saludar("Jose")
saludar("Angel")

#Las funciones tambien pueden tener valores por defecto en los argumentos
def saludar_despistado(nombre="amigo"):
    saludar(nombre)
saludar_despistado("Jose")
saludar_despistado()
#%%
#Las funciones pueden devolver un valor
def suma(a,b):
    return a+b
    print("Esto no se va imprimir, porque la funcion finaliza con return")
resultado_suma=suma(1,1.2)
print(resultado_suma)
#ahora podemos usar el resultado con arguumento
resultado_suma2=suma(resultado_suma,3)
print(resultado_suma2)
#%%
#Una funcion que no tiene un return devuelve un none
def suma_erronea(a,b):
    resultado=a+b
    #tine que usar retun para devolver el resultado de la suma
resultado_suma1=suma_erronea(2.5,4)
print(resultado_suma1)
#%%
#Las funciones tiene un solo return , pero pueden devolver multiples cosas
def suma_y_resta(a,b):
    suma=a+b
    resta=a-b
    return suma,resta
resultado=suma_y_resta(10,5)
print(resultado)
print(type(resultado))
#podemos desempaquetar el resultado directamente
resultadoSuma,resultadoResta=suma_y_resta(10,5)
print(resultadoSuma)
print(resultadoResta)
#%%
"""
Existe otara forma de crear funciones llamadas lambda o funciones anonimas 
se define de la forma:
    funt_lambda=lambda input:output
Las funciones lambda se pueden utilizar cuando queremos aplicar logica sencilla 
para la cual la definicion formal no es nesesaria
"""
suma_lambda=lambda a,b:a+b
resultado_suma1=suma_lambda(2.5,5)
print(resultado_suma1)
#podemos usar el resultado de la funcion como input
resultado_suma2=suma_lambda(resultado_suma1,10)
print(resultado_suma2)
#%%
#Crear una funcion que resta 2 numero y devuelve el resultado 
def resta(a,b):
    return a-b
print(resta(52,10))
#%%
#Crear una funcion que convierte  un string en minusculas
def minusculas(texto):
    return texto.lower()
minusculas1= lambda texto:texto.lower()
print(minusculas1("HOLA!"))
#%%
#Crear una funcion que hacepta tres argumentos de dos numero y un string
#es un string "suma" devuelve la suma de dos numero
#si el string es "resta" devuelve la resta de dos numeros
def suma_o_resta(a,b,modo):
    if modo=="suma":
        return a+b
    elif modo=="resta":
        return a-b
    else:
        #generar una exception u error
        #sepuede usar print("suma_o_resta solo admite dos modos, suma o resta")
        raise Exception("suma_o_resta solo admite dos modos, suma o resta")
print(suma_o_resta(10,3,"suma"))
print(suma_o_resta(10,3,"resta"))
print(suma_o_resta(10,3,"multiplicacion"))
#%%
#Crear una funcion que pregunte al usuario una fase y devuelva dicha frase con 
#las palabrras en orden inverso si el usuario dice "la lluvia en sevilla" la 
#funcion devolvera "sevilla en lluvia la"
def invertir_frase(frase):
    frase_invertida=""
    palabras=frase.split(" ")
    for palabra in palabras[::-1]:
        frase_invertida += palabra
        frase_invertida += " "
    return frase_invertida
print(invertir_frase("la lluvia en sevilla"))
###########
def invertir_frase_mejorada(frase):
    palabras=frase.split(" ")
    return " ".join(palabras[::-1])
print(invertir_frase("La lluvia en sevilla"))
print(invertir_frase_mejorada("La lluvia en sevilla")) 
#%%
#Programa para determibar si una palabra es palindromo(frase se puede leer
# al derecho y alrevez)
def es_palindromo(frase):
    frase_invertida=frase[::-1]
    for i in range(len(frase_invertida)):
        if frase[i]!=frase_invertida[i]:
            return False
    return True
es_palindromo("oso")
#%%
"""
Crear una funcion dada una lista de listas, nos devuelva una lista simple es 
decir si ninguna lista simple
lista_nesteada=[
            [1,2,3],
            [4,5,6,7],
            [8,9]
            ]
la funcion nos devolvera la lista[1,2,3,4,5,6,7,8,9]
""" 
def simplificar_lista(lista_nesteada):
    lista_simple=[]
    for lista_interna in lista_nesteada:
        for elemento in lista_interna:
            lista_simple.append(elemento)
    return lista_simple
lista_nesteada=[
        [1,2,3],
        [2,3,5],
        [4,3,6]
        ]
simplificar_lista(lista_nesteada)