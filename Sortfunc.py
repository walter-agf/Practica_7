def loadFromFile(name):
    ''' 
        Recibe el nombre de un archivo (str)
        Retorna una lista de floats con cada uno 
        de los números extraídos del archivo name
    '''
    name = name.readlines()
    cont = 0
    for i in name:
        name[cont] = float(i[:-1])
        cont += 1
    return name

def sortBurbuja(L):
    ''' 
        Recibe una lista de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de burbuja
        para ordenar la lista L
    '''
    num = 0
    for i in range (len(L)):
        cont = False
        for a in range (len(L)-1):
            if L[a] > L[a+1]:
                ca = L[a]
                L[a]=L[a+1]
                L[a+1]= ca
                cont = True
            num += 1
        if cont == False:
            #print (L)
            return num
    #print(L)
    return num

def sortSeleccion(L):
    ''' 
        Recibe una lista de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de selección
        para ordenar la lista L
    '''
    num = 0
    for i in range (len(L)):
        for a in range(i+1,len(L)):
            if L[a] < L[i]:
                ca = L[a]
                L[a] = L[i]
                L[i] = ca
            num += 1
    #print (L)
    return num

def createRandomList(size, minimo, maximo):
    '''
    Retorna un lista de size números aleatorios. Cada elemento de la lista debe 
    estar en el rango [minimo, maximo]
    
    Parámetros
        size: cantidad de elementos a poner en la lista
        minimo: número mínimo que puede haber en la lista
        maximo: número máximo que puede haber en la lista
    '''
    from random import randint
    lis = []
    for i in range (size):
        lis.append(randint(minimo,maximo))
    return lis

def sortMerge(L,cont):
    def merge(left,right):
        """
        Asume que left y right son listas ordenas
        """
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
                #print (i,"Left")
            else:
                result.append(right[j])
                j += 1
                #print (j,"Right")
        #print (result)
        while i < len(left):
            result.append(left[i])
            i += 1
            #print (i,"Left")
        while j < len(right):
            result.append(right[j])
            j += 1
            #print (j,"Right")
        return result
    """
    Asume que L es una lista y retorna una nueva lista ordenada
    """
    #print (L)
    cont += 1
    #print (cont)
    if len(L) < 2:
        return L[:],cont
    else:
        mid = len(L)//2
        left,cont = sortMerge(L[:mid],cont)
        right,cont = sortMerge(L[mid:],cont)
        #print (left)
        #print (right)
        return merge(left,right),cont
def sortQuick(L):
    ''' 
        
    '''
    pass
