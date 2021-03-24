
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 07 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um maneira pratica de calcular o ganho mensal de um trabalhador
#___________________________________________________________________#

"""
    O módulo disponibiliza uma solução prática para calcular o salário de um trabalhador, dado algumas informações
    básicas, como hora trabalhadas por dia, valor da hora pago e o mês referênte ao pagamento.
"""


class Contabilidade:

    __slots__ = ('__valor_hora', '__horas_dia', '__num_mes')

    def __init__(self, valor_hora, horas_dia, num_mes):
        self.__valor_hora = valor_hora
        self.__horas_dia = horas_dia
        self.__num_mes = num_mes
        self.__definir_horas_trabalhadas()


    @property
    def GetValorHora(self):
        return self.__valor_hora

    @property
    def GetHoraDia(self):
        return self.__horas_dia

    @property
    def GetMes(self):
        return self.__num_mes


    def __definir_horas_trabalhadas(self):
        "Calcula a quantidade de horas trabalhadas em um mês."
        try:
            if self.GetMes in (1, 3, 5, 7, 8, 10, 12):
                quant_horas_mes = self.GetHoraDia * 31
                return self.__calcular_salario(horas_mes=quant_horas_mes)
            elif self.GetMes in (4, 6, 9, 11):
                quant_horas_mes = self.GetHoraDia * 30
                return self.__calcular_salario(horas_mes=quant_horas_mes)
            elif self.GetMes == 2:
                quant_horas_mes = self.GetHoraDia * 28
                return self.__calcular_salario(horas_mes=quant_horas_mes)
            else:
                raise ValueError

        except ValueError:
            print('Esse mês não existe.')


    def __calcular_salario(self, horas_mes):
        "Calcula o salario, recebendo o retorno do método que '__definir_horas_trabalhadas'."
        salario = self.GetValorHora * horas_mes
        print('O salario é igual à R${:.2f}'.format(salario))




if __name__ == '__main__':
    teste = Contabilidade(12.60, 4, 13)