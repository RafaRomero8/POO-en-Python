import random

def busqueda_lineal(lista, objetivo):
    match = False #un elemento O(1)
           #se obtiene o(n) porque depende del tamaño de la lista se utiliza el for,es lineal
    for elemento in lista:#recorrer la lista(bucle a lo larg de la lista) se obtiene un O(n)
        if elemento == objetivo:#comparacion
            match = True#asignacion
            break#salir del bucle

    return  match#retornar valor


if __name__ == '__main__':
    tamano_de_lista = int(input('de que tamaño sera la lista'))#preguntar al usuario el tamaño de lista
    objetivo = int(input('que numero quieres encontrar?'))##preguntar al usuario cual es el objetivo

    lista =[random.randint(0,100) for i in range(tamano_de_lista)]
    #se genera la lista (se genera un numero aleatorio del tamaño de la lista)
    encontrado = busqueda_lineal(lista, objetivo)#encontrado

    print(lista)#imprimir lista
    print(f'el elemento{objetivo} {"esta" if encontrado  else "no esta"} en la lista"')#conquetenacion .si si esta en la lista va decir si esta en la lista
    #operacion ternria ,generar un if else
