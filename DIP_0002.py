
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 05 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Interação com usuário, input.
#___________________________________________________________________#

class ReceberNumero:

    __num = None

    def __init__(self):
        try:
            ReceberNumero.__num = int(input('Digite um número: '))
            MostrarNumero(ReceberNumero.__num)

        except:
            print('Ops.. Algo deu errado.')


class MostrarNumero:

    @classmethod
    def __init__(cls, numero):
        print('O número que você digitou foi o {}'.format(numero))




if __name__ == '__main__':
    x = ReceberNumero()
