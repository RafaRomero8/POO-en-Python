import random
def busqueda_binaria(lista,comienzo,final,objetivo): #se recibe una lista comienzo final y objetivo
    if comienzo > final:#si el comienzo es mas grande que el final termina
        return  False   #si no es cierto se divide a la mitad

    medio = (comienzo + final) // 2#se divide la lista en dos
    if lista[medio] == objetivo:#comparamos si esta el onbjetivo
        return True
    elif lista[medio] < objetivo:#si es mas pequeño
        return busqueda_binaria(lista,medio+1,final,objetivo)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo)



if __name__ == '__main__':
    tamano_de_lista = int(input('de que tamaño sera la lista'))
    objetivo = int(input('que numero quieres encontrar?'))
    lista =sorted([random.randint(0,100) for i in range(tamano_de_lista)])
       #sorted para ordenar la lista para la busqueda binaria

    encontrado = busqueda_binaria(lista,0,len(lista),objetivo)#se empieza en 0 y se termin en l longitud de la lista
  #utilizar indices para movernos en la lista
    print(lista)
    print(f'el elemento{objetivo} {" si esta" if encontrado  else "no esta"} en la lista"')