
class Lavadora:
    def __init__(self):
        pass

      # este metodo es publico cuando no tiene guion bajo
    def lavar(self,temperatura='caliente'):
        self._llenar_tanque(temperatura)
        self._anadir_jabon() #parametros o metodos privados
        self._lavar()
        self._centrifugar()

    def _llenar_tanque(self,temperatura):#definir los metodos
        print(f'llenando tanque de agua{temperatura}')

    def _anadir_jabon(self):
        print('anadir jabon')

    def _lavar(self): # "_" guion bajo para los metodos privados
        print('lavando ropa')

    def _centrifugar(self):
        print('centrifugando la ropa')

if __name__ =='__main__':

    lavadora = Lavadora()  #se genera una instanciadejamos la temperatura por defult que es caliente
    lavadora.lavar()   #podemos elegir otra temperatura ya sea fria o tibia

    #mandamos a llamar a la funcion