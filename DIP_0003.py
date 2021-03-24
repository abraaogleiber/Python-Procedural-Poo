
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 05 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Somando dois números
#___________________________________________________________________#

class Somatoria:

    __slots__ = ('__n1', '__n2')
    __soma = None

    def __init__(self, n1=0, n2=0):
        self.__n1 = n1
        self.__n2 = n2


    @property
    def GetN1(self):
        return self.__n1

    @property
    def GetN2(self):
        return self.__n2

    @property
    def GetSoma(self):
        return Somatoria.__soma
    @GetSoma.setter
    def SetSoma(self, resultado):
        Somatoria.__soma = resultado


    def executar_soma(self):
        """Este método realiza os calculos."""
        self.SetSoma = (self.GetN1 + self.GetN2)

    def mostrar_resultado(self):
        """Este método imprime a saída."""
        print('A soma entre os valore é {}'.format(self.GetSoma))




if __name__ == '__main__':
    try:
        x = int(input('1º Número: '))
        y = int(input('2º Número: '))

        s = Somatoria(x, y)
        s.executar_soma()
        s.mostrar_resultado()

    except Exception:
        print('Por favor, digite somente valores numericos!.')
        