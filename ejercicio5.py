def Insert_Sort(lista):
    for index in range(1, len(lista)):
        actual = lista[index]
        posicion = index
        #print("Valor a ordenar ", format(actual))
        while posicion >0 and lista[posicion-1]>actual:
            lista[posicion] = lista[posicion-1]
            posicion = posicion-1
        lista[posicion] = actual
        #print(lista)
        
        #print()
    return lista



if __name__ == "__main__":
    lista = [21,10,12,45,0,34,15]
    print(lista)
    lista = Insert_Sort(lista)
    print(lista)



