import random

def ordenamiento_burbuja(lista):#
    n =len(lista)#obtenemos la longitud de la lista

    for i in range(n):#iterar internamente hasta el final(tamaño de la lista)
        for j in range(0,n-i-1 ):#comparar elemntos si es mayor intercambiamos
               #tamaño de lista - lo que ya recorrimos,- 1 que es la longitud
            if lista[j]>lista[j+1]:#comparar indices al elemto adiacente (el elmento de a lado)
                lista[j],lista[j+1] = lista[j + 1],lista[j]#el +1 lo pasamos a lista j

    return  lista



if __name__=='__main__':
    tamano_lista = int(input('de que tamano sera la lsta? '))

    lista =[random.randint(0,100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)