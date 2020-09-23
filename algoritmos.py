import  time

def factorial(n):#recibimos un numero factorial
    respuesta = 1 #respuesta que comienza en uno

    while n > 1:
        respuesta *= n #multiplicamos respuest por n
        n -= 1  #va a ir decreciendo

    return  respuesta#regresamos respuesta

def factorial_r(n):#factorial recursivo
    if n==1: #si en es igual a uno,regresa uno
        return 1
    return  n * factorial_r(n-1)

if __name__ =='__main__':
    n = 100 #definimos n

    comienzo = time.time()#se ejecuta el modulo time en el comienzo
    factorial(n)
    final = time.time()
    print(final - comienzo) #se imprime cuanto tiempo nos tardamos o se tarda el algoritmo

    comienzo = time.time()
    factorial_r(n)#
    final = time.time()
    print(final - comienzo)
    #se compara los dos tiempos de las implementaciones
