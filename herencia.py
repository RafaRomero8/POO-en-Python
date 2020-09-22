
class Rectangulo:#se genera una clase rectangulo

    def __init__(self,base,altura):# se inicializa el constructor
        self.base=base
        self.altura = altura

    def area(self):#se gener un metodo
        return self.base * self.altura

class Cuadrado(Rectangulo):#la clase cuadrado extiende a rectangulo(aqui hacemos herencia)
    #tenemos acceso a la superclase rectangullo
    def __init__(self,lado):#constructor asi se define
        super().__init__(lado,lado)#obtenemos la referencia con la funcion super() de la superclase y podemos llamar al constructor
                                   #con super tenemos acceso a la supeclase

if __name__ =='__main__':
    rectangulo = Rectangulo(base=3,altura=4)
    print(rectangulo.area())
    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())