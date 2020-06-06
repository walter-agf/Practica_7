# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:55:43 2020

@author: Usuario
"""

from random import randint
from time import datetime
tiempo_inicial=datetime.now()
lista= [20, 10, 5]

for i in range (0, 10):
    lista.append(randint(0, 10000000))

print (lista)

temp = 0

"""
for J in range(l, len(lista)):
    for i in range (0, len(lista)-j):
        if lista [i]>lsita[i+l]:
            temp=lista[i]
            lista[i]=lista[i+l]
            lista[i+l]=temp 
"""
tiempo_final=datetime.now()
d =str(tiempo_final-timepo_inicial)
print("tiempo de ejecucion: "+d)