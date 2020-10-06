
def morral(tamano_morral, pesos, valores, n):#variable n cual es el indice que estamos trabajando

    if n == 0 or tamano_morral == 0:#si esta lleno regeresa 0 que ya no hay mas elemntos o el moral esta lleno
        return 0

    if pesos[n - 1] > tamano_morral:#checa el siguiente elemento
        return morral(tamano_morral, pesos, valores, n - 1)#n-1 pasa al siguinte  elemento

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))
#funcion max escojer el valor maximo de dos valores

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)