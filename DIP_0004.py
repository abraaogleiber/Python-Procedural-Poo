
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 05 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Calculando média
#___________________________________________________________________#

class CalculaMedia:
    "A classe fornece uma maneira automatizada de calcular médias."

    def __init__(self, n1=0.0, n2=0.0, n3=0.0, n4=0.0):
        self.__n1 = n1
        self.__n2 = n2
        self.__n3 = n3
        self.__n4 = n4


    @property
    def GetN1(self):
        return self.__n1

    @property
    def GetN2(self):
        return self.__n2
                                    # Areá de getters e setters
    @property
    def GetN3(self):
        return self.__n3

    @property
    def GetN4(self):
        return self.__n4


    def calculando_media(self, imprimir=False):
        "Realiza a somatoria e o calculo da média."

        somatoria = (self.GetN1 + self.GetN2 + self.GetN3 + self.GetN4)
        media = ( somatoria / 4)

        if imprimir:
            print('A média do aluno é {:.2f}'.format(media))



if __name__ == '__main__':
    x = CalculaMedia()
    x.calculando_media(imprimir=True)
