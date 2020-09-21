class Lavadora:
    def __init__(self):
        pass
    def lavar(self,temperatura = 'caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir:jabon() #parametrod
        self._lavar()
        self.centrifugar()

    def _llenar_tanque(self,temperatura):#definir los metodos
        print(f'llenando tanque de agua{temperatura}')

    def _anadir_jabon(self):
        print('lavando la ropa')

    def _lavar(self):
        print('lavando ropa')

    def _centrifugar(self):
        print('centrifugando la ropa')