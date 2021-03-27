
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 06 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um conversor de médidas inteligente
#___________________________________________________________________#

"Este módulo armazena o código resonsável pela conversão de médida."


def conversor(m: float):
    "Realiza a conversão, multiplicando o valor de entrada por 100."
    valor_cm = (m * 100)
    return valor_cm


def main():
    "Realiza a chamada da função 'conversor()' e caça possiveis erros de entrada."
    try:
        valor_m = float(input('Valor(m): '))
        print(conversor(valor_m))

    except ValueError:
        print('Não foi possivel identificar sua entrada!!')


main()
