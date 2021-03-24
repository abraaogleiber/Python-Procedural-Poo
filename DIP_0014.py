
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 13 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um programa que identifica o maior valor
#___________________________________________________________________#

from abc import ABC, abstractmethod


class Numero(ABC):
    """"""
    def __init__(self, *n):
        super().__init__()
        self.__valores = n


    @property
    def GetValores(self):
        return self.__valores



class Maior(Numero):
    """"""
    __maior = 'Os valores são iguais!.'

    def __init__(self, *n):
        super().__init__(*n)
        self.definindo_maior()


    @property
    def GetMaior(self):
        return Maior.__maior
    @GetMaior.setter
    def SetMaior(self, maior):
        Maior.__maior = maior


    def definindo_maior(self):
        self.SetMaior = self.GetValores[0]

        for n in self.GetValores:
            if n > self.GetMaior:
                self.SetMaior = n


    def maior_numero(self):
        return self.GetMaior




class Menor(Numero):
    """"""
    __menor = 'Os valores são iguais!.'

    def __init__(self, *n):
        super().__init__(*n)
        self.definindo_menor()


    @property
    def GetMenor(self):
        return Menor.__menor
    @GetMenor.setter
    def SetMenor(self, menor):
        Menor.__menor = menor


    def definindo_menor(self):
        self.SetMenor = self.GetValores[0]

        for n in self.GetValores:
            if n < self.GetMenor:
                self.SetMenor = n


    def menor_numero(self):
        return self.GetMenor



if __name__ == '__main__':

    menor = Menor(11, 22, 33, 0, 1, -2)
    print(menor.menor_numero())

    maior = Maior(11, 22, 43, 90, 102)
    print(maior.maior_numero())

