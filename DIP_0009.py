
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 08 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Criar uma solução que converta graus fahrenheit para celsius
#___________________________________________________________________#


class ConversorCelsius:
    """
        A classe converte um temperatura em graus Fahrenheit para graus Celsius.
    """

    def __init__(self, graus_fahrenheit):
        try:
            if isinstance(graus_fahrenheit, int) or isinstance(graus_fahrenheit, float):
                self.__graus_fahrenheit = graus_fahrenheit
                self.__graus_celsius = None
                self.__converter_para_celsius()
            else:
                raise TypeError
        except TypeError:
            print('Por favor, somente valores numericos.')


    @property
    def GetGrausFahrenheit(self):
        return self.__graus_fahrenheit

    @property
    def GetGrausCelsius(self):
        return self.__graus_celsius
    @GetGrausCelsius.setter
    def SetGrausCelsius(self, graus_celsius):
        self.__graus_celsius = graus_celsius


    def __converter_para_celsius(self):
        self.SetGrausCelsius = ((self.GetGrausFahrenheit - 32) / 9) * 5
        self.__imprimir_resultado(self.GetGrausCelsius)


    def __imprimir_resultado(self, resultado):
        print('A temperatura convertida é {:.1f}ºC'.format(resultado))



if __name__ == '__main__':
    x = ConversorCelsius(12.6)
