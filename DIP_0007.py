
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 07 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um maneira pratica de calcular a área de um quadrado
#___________________________________________________________________#


class CalcularQuadrado:

    __slots__ = ('__valor_lado')

    __TIPO_GEOMETRIA = 'Quadrado'
    __valor_area = None


    def __init__(self, valor_lado=0.0):
        self.__valor_lado = valor_lado
        self.__calculando_area()

    @property
    def GetTipoGeometria(self):
        return CalcularQuadrado.__TIPO_GEOMETRIA

    @property
    def GetValorArea(self):
        return CalcularQuadrado.__valor_area
    @GetValorArea.setter
    def SetValorArea(self, area):
        CalcularQuadrado.__valor_area = area

    @property
    def GetValorLado(self):
        return self.__valor_lado


    def __calculando_area(self):
        "Método protegido. Realiza o calculo da área, será chamado automaticamente na inicialização da classe."
        self.SetValorArea = (self.GetValorLado ** 2)
        return print('Figura geometrica: {}  |  Lado: {}  | Área: {}(m²)'.format(self.GetTipoGeometria, self.GetValorLado, self.GetValorArea))


    def dimensionar_area(self, nVezes=0):
        "Realiza o calculo de dobragem do valor da área."
        try:
            if isinstance(nVezes, int):
                area_dobrada = (self.GetValorArea * nVezes)
                return print(f'{nVezes}x ---- ---- ---- {area_dobrada}(m²)')
            else:
                raise ValueError
        except ValueError:
            print('Só podemos dimensionar por números inteiros.')






if __name__ == '__main__':
    t = CalcularQuadrado()
    t.dimensionar_area()
