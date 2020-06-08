#Esttayegia divide y venceras
"""
21 10 0 34 15
p  i        d
"""

def quick_sort(lista):
    quicksort2(lista,0,len(lista)-1)



def quicksort2(lista, inicio,fin):
    if inicio<fin:
        pivote = particion(lista,inicio,fin)
        quicksort2(lista,inicio,pivote-1)
        quicksort2(lista,pivote+1,fin)

def particion(lista, inicio,fin):
    pivote= lista[inicio]
    #print("Valor pivote ",format(pivote))
    izq=inicio+1
    der=fin
    #print("Indice izq {} e indice derecho {}",format(izq),format(der))
    bandera=False
    while not bandera:
        while izq<=der and lista[izq]<= pivote:
            izq = izq+1
        while lista[der]>= pivote and der>=izq:
            der=der-1
        if der<=izq:
            bandera=True
        else:
            aux=lista[izq]
            lista[izq]=lista[der]
            lista[der]=aux
        

    #print(lista)
    temp= lista[inicio]
    lista[inicio]=lista[der]
    lista[der]=temp

    return der


if __name__ == "__main__":

    lista = [21,10,12,45,0,34,15]

    #print(lista)
    quick_sort(lista)
    #print(lista)


