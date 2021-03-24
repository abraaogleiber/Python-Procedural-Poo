
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 16 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Mostrar os valores de entrada do termino ao inicio
#___________________________________________________________________#


"""

"""
class FolhaPagamento:

    __salario_bruto = 00.00
    __salario_liquido = 00.00
    __slots__ = ('__valor_hora', '__horas_trabalhadas')


    def __init__(self, valor_hora, horas_trabalhadas):
        try:
            if isinstance(valor_hora, int) or isinstance(valor_hora, float):
                self.__valor_hora = valor_hora
            else:
                raise ValueError

            if isinstance(horas_trabalhadas, int) or isinstance(horas_trabalhadas, float):
                self.__horas_trabalhadas = horas_trabalhadas
            else:
                raise ValueError
        except ValueError:
            print('Impossivel executar este programa com valores NÃO numericos!.')
            exit()


    @property
    def GetSalarioBruto(self):
        return FolhaPagamento.__salario_bruto
    @GetSalarioBruto.setter
    def SetSalarioBruto(self, salario):
        FolhaPagamento.__salario_bruto = salario

    @property
    def GetSalarioLiquido(self):
        return FolhaPagamento.__salario_liquido
    @GetSalarioLiquido.setter
    def SetSalarioLiquido(self, salario):
        FolhaPagamento.__salario_liquido = salario

    @property
    def GetValorHora(self):
        return self.__valor_hora

    @property
    def GetHorasTrabalhadas(self):
        return self.__horas_trabalhadas


    def calcular_salario_bruto(self):
        """
        -------> O método Calcula e define o salário-bruto.
        retorna: None
        """
        self.SetSalarioBruto = (self.GetHorasTrabalhadas * self.GetValorHora)


    def efetuar_descontos(self):
        """
        -------> O método afetua sobre o salário-bruto os descontos de acordo com as condições. E define o salário-
                 líquido.
        retorna: None
        """
        if self.GetSalarioBruto != 0:
            if 900 < self.GetSalarioBruto <= 1500:
                ir = (self.GetSalarioBruto * 5) / 100
            elif 1500 < self.GetSalarioBruto <= 2500:
                ir = (self.GetSalarioBruto * 10) / 100
            elif self.GetSalarioBruto > 2500:
                ir = (self.GetSalarioBruto * 20) / 100
            else:
                ir = 0.0

            inss = (self.GetSalarioBruto * 10) / 100
            fgts = (self.GetSalarioBruto * 11) / 100

            total_descontos = (ir + inss + fgts)
            self.SetSalarioLiquido = (self.GetSalarioBruto - total_descontos)
        else:
            print('Primeiro execute o método responsável pelo calculo do salário bruto!.')


    def salario_liquido(self):
        """
        -------> O método gera uma saída dos valores processados, mostrando o valor do salário-líquido ao usuário
                 por meio de um "print".
        retorna: None
        """
        if self.GetSalarioLiquido != 0:
            print(f'O salário líquido é R${self.GetSalarioLiquido:.2f}')
        else:
            print('Primeiro execute o método responsável pelo calculo do salário bruto e aplique os descontos!.')



if __name__ == '__main__':
    empresa = FolhaPagamento(5.87, 220)
    empresa.calcular_salario_bruto()
    empresa.efetuar_descontos()
    empresa.salario_liquido()
