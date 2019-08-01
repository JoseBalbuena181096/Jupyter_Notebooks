"""
Tipos de variables
"""
#%%
"""
Python tiene muchos tipos de variables básicas que forman parte del núcleo del 
lenguaje, son lo que se llama primitivas
"""
"""
Las primitivas más comunes son strings mumeros booleanos
"""
"""
********************************************************
STRINGS
********************************************************
"""
print("Se usan para representar texto")
#%%
var_str="Hola!"
var_str2="Mundo!"
#la funcion type() nos dice el tipo de dato
print(type(var_str))
print(type(var_str2))
#%%
"""
Los strings se pueden unir para formar strings más largos. Hay 
varias de unir strings (lo que se llama interpolacion de strings)
"""
#Podemos usar el simbolo + para "Sumar"(concatenar) strings
var_str_unido=var_str+" "+var_str2
print(var_str_unido)
#%%
#Tambien podemos "multiplicar" string!
n="monja "
print(n*10)
#%%
"""
Tambien podemos usar el método format, que nos permite unos strings dentro de 
otros
"""
nombre="Manuel"
ciudad="Murcia"
presentacion="Hola, ,me llamo {}, soy de {}".format(nombre,ciudad)
print(presentacion)
#%%
#Usando el meto format puede indicar como formatear las variables
#Por ejemplo, redondear numeros decimales
import math

pi_str="Los primeros digitos de pi son: {}".format(math.pi)
pi_str=
