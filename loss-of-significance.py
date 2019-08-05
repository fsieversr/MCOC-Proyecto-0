# -*- coding: utf-8 -*-
"""
Created on Mon Aug 05 07:29:27 2019

@author: panch
"""

#Calculos hechos con numero de Avogrado para la masa de un elemento

import numpy as np
import matplotlib.pyplot as plt
    

#numero de avogrado
avogrado = 6.022140857*(10**23) #atomos/mol
avogradoaprox = 6.023*(10**23) #numero de avogrado usado comunmente

#funcion para el calculo de masa de un atomo
def calculomasa(x):
    masaatomo= x/avogrado
    return masaatomo
    
def calculomasa1(x):
    masaatomoreal= x/avogradoaprox
    return masaatomoreal
   

#gramos por mol de elementos y moleculas
elementos = {"Agua":18, "Acido Sulfurico": 98, "Azufre": 32, "Cloruro de Sodio": 58, "Nitrato de Plata":170, "Acido Fosforico": 98, "Metano": 16, "Etano":30, "Alcohol Etilico": 46, "Cloruro Mercuroso": 235,"Cianuro de Potasio": 65, "Propano": 44}

masa = elementos.values()

valorcomun = []
f32= [] #lista con datos de 32
f64= [] #lista con datos de 64

for i in masa:
    f32.append(np.float32(calculomasa(i))) #calculamos los gramos del atomo en 32 bit
    f64.append(np.float64(calculomasa(i))) #calculamos los gramos del atomo en 64 bit
    valorcomun.append(calculomasa1(i))
    
#error relativo
def error(valorreal, valorcalculado):
    error= (valorcalculado-valorreal)/valorreal
    return error

errorf32=[] #lista con errores entre float32 y el valor comun
errorf64 =[] #lista con errores entre float64 y el valor comun
largo = []

for j in range(len(masa)):
    errorf32.append(error(valorcomun[j], f32[j]))
    errorf64.append(error(valorcomun[j], f64[j]))
    largo.append(j)


plt.plot(largo, errorf32, color ="r")
plt.plot(largo, errorf64, color="b")
plt.grid()
plt.show


print errorf32    
print errorf64

