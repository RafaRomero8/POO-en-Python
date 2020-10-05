import random

def ordenamiento_mezcla(lista):
    if len(lista) > 1: #si la longitud de lista es mayor  a uno
        medio =len(lista) // 2 #encontrar la mitad de la lista se divide en dos
        izquierda = lista[:medio] #se divide  en la lista ezq. va de 0 a la mitad
        derecha = lista[medio:]#se genera la mitad hasta el final (rebanadas)

        #llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)#llamada a ordenamiento por la izuierda
        ordenamiento_mezcla(derecha)#llamada a la derecha
        #iteradores para correr las dos sublistas
        i = 0 #iterador para la lita,
        j = 0
        #iterador para la lista principal
        k = 0

        # comparacion entre listas
        while i < len(izquierda) and j < len(derecha):# mientras la longitud de i sea menor que la longitud de izq y j pmenor que derecha
            if izquierda[i] < derecha[j]:#si la isq en indice i es menor que en la indice j
                lista[k] = izquierda[i]#sea igual a laizq en el indice i
                i += 1 #aumentar indice
            else:
                lista[k] = derecha[j]
                j +=1
            k += 1 #para que no se valla al infinito

        while i < len(izquierda): # i sea menor que longitud de la izq.
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            list[k] = derecha[j]
            j += 1
            k += 1

        return  lista



if __name__=='__main__':
    tamano_lista = int(input('de que tamano sera la lsta? '))

    lista =[random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    print('-' * 20)#

    lista_ordenada = ordenamiento_mezcla(lista)
    print(lista_ordenada)