from Sortfunc import loadFromFile,createRandomList,sortBurbuja,sortSeleccion,sortMerge,sortQuick
"""
Crea una lista con numeros de punto flotnate 
respcto al arcchivo data
"""
import os
directorio_actual = os.getcwd()
name = directorio_actual+"/data.txt"
lista = loadFromFile(name)
########print (lista,end="\n\n")
"""
Crea una lista completamente aleatoria 
con una cantidad de numeros y un minimo y un maximo
"""
L = createRandomList (24,20,80)
########print (L,end="\n\n")
"""
Hace el respectoivo ordenamieto por algorimo de burbuja
"""
num = sortBurbuja(lista)
########print (num,end="\n\n")
"""
Vulvemos a leer la lista que esta en data
y volvemos a ordenar por el algorimo de Seleccion
"""
from tkinter.filedialog import askopenfilename 
fname = askopenfilename()
lista = loadFromFile(fname)
num = sortSeleccion(lista)
########print (num,end="\n\n")
"""
Con la lista aleatoria creada anteriormete de forma aleatoria
la ordenamos de con el algorimo de Mergue Sort
"""
cont = 0
L,cont = sortMerge(L,cont)
#print (L)
########print (cont,end="\n\n")
"""
Volvemos a crear una lista aleatoria a la que ordenamos
con el algorimo de Quick Sort
"""
L = createRandomList (12,30,80)
#print (L,end="\n\n")
cont = 0
num,cont = sortQuick(L,cont)
#print (num,end="\n\n")
#########print (cont)
"""
Pregutamos cuantas veces se quiere hacer esta misma prueba
para comprobar el funcionamieto de los algorimos de Sortfunc
"""
print ("\n\n\n")
conti = True
while conti ==  True:
    print ("\tMecanismo de Prueba de algoritmos de SORTFUNC\n")
    n = 0
    while n <= 0:
        try:
            n = int(input("Cual es el tamaño de la lista aleaotria para probar los 4 algoritmos\n---> "))
        except ValueError:
            print ("\nValor impreciso")
            n = 0
    print ("\n\n\n\n")
    inf = 0
    sup = 0
    while inf >= sup:
        try:
            inf = int(input ("Ingrese un numero Inferior [Tiene que ser inferior al numero superior]\n---> "))
            sup = int(input ("Ingrese un numero Superior [Tiene que ser superio al numero inferior]\n---> "))
        except ValueError:
            print ("\n\n\n\n")
            print ("\nValor impreciso")
            inf = 0
            sup = 0
    """
    Se crea una lista aleatoria que se utiliza para compara todos los algorimos
    """
    L = createRandomList (n,inf,sup)
    print ("\n\n")
    #print (L)
    num = sortBurbuja(L[:])
    print (num,end="  --  Algoritmo Burbuja\n\n")
    #print (L)
    num = sortSeleccion(L[:])
    print (num,end="  --  Algoritmo Seleccion\n\n")
    #print (L)
    cont = 0
    M,cont = sortMerge(L[:],cont)
    print (cont,end="  --  Algoritmo Merge Sort\n\n")
    #print (L)
    cont = 0
    num,cont = sortQuick(L[:],cont)
    print (cont,end="  --  Algoritmo de Quick Sort\n\n")
    x = 0
    while x == 0:
        try:
            print ("Quiere continuar ?\n\n1) SI\n2) N0")
            x = int(input("--> "))
            if x > 2 or x < 0:
                print ("\n\n\n\n")
                print ("\nValor impreciso")
                x = 0
        except ValueError:
            print ("\n\n\n\n")
            print ("\nValor impreciso")
            x = 0
    if x == 2:
        conti = False