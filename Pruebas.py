from Sortfunc import loadFromFile,createRandomList,sortBurbuja,sortSeleccion,sortMerge

name = open("data.txt","r")
lista = loadFromFile(name)
print (lista,end="\n\n")

L = createRandomList (24,30,80)
print (L,end="\n\n")

num = sortBurbuja(L)
print (num,end="\n\n")

num = sortSeleccion(L)
print (num,end="\n\n")

cont = 0
L,cont = sortMerge(L,cont)
#print (L)
print (cont,end="\n\n")





#n = input("Cuantas pruebas de orden aleatorio quiere hacer a los 4 algoritmos\n---> ")



#for i in range (n):