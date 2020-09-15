
class Coordenada:

     def __init__(self,x,y):
        self.x = x
        self.y = y

     def distancia(self,otra_coordenada):
         x_diff = (self.x - otra_coordenada.x)**2 #
         y_diff = (self.y - otra_coordenada.y)**2

         return (x_diff + y_diff)**0.5

if __name__ =='__main__':
     coord_1 = Coordenada(3,30)
     coord_2 = Coordenada(4,8)
     print(coord_1.distancia(coord_2))
#definición de clase
"""
class <nombre_de_la_clase>(<super_classe>):
    def __init__(self,<params>):#constructor inicin con self
        <expresion>#
    def <nombre_del_metodo>(self,<params>):#definir la funcionalidad de la clase
        < expresion >

"""