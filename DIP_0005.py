
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 06 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um conversor de médidas inteligente
#___________________________________________________________________#


"Este módulo armazena a classe responsável pela conversão de médidas."

class Conversor():
    "Recebe um valor na sua instaciação e retorna de forma automatica o valor convertido."

    __valor_centimetros = 0.0

    def __init__(self, valor_metros):
        try:
            self.__valor_metros = float(valor_metros)
            self.calculo_conversao()
            self.mostrar_resultado()

        except ValueError:
            print('Não foi possivel converter essa "letra/símbolo" para uma valor calculavel!!!.')



    @property
    def GetValorCentimetros(self):
        return Conversor.__valor_centimetros

    @GetValorCentimetros.setter
    def SetValorCentimetros(self, valor_centimetros):
        Conversor.__valor_centimetros = valor_centimetros

    @property
    def GetValorMetros(self):
        return self.__valor_metros


    def calculo_conversao(self):
        self.SetValorCentimetros = (self.GetValorMetros * 100)


    def mostrar_resultado(self):
        print('-'*20, 'Calculo de conversão', '-'*20)
        print(f'>>> {self.GetValorMetros}(m) --------------------------------- {self.GetValorCentimetros}(cm)')
        print('-'*62)




if __name__ == '__main__':
    x = Conversor(456)

