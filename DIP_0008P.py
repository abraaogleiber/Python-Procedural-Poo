
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 07 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um maneira pratica de calcular o ganho mensal de um trabalhador
#___________________________________________________________________#

"""
    O módulo disponibiliza uma solução prática para calcular o salário de um trabalhador, dado algumas informações
    básicas, como hora trabalhadas por dia, valor da hora pago e o mês referênte ao pagamento.
"""


def calcula_horas_mes(horas_dia, n_mes):
    "A função realiza o calculo de horas por mês."
    if n_mes in [1, 3, 5, 7, 8, 10, 12]:
        horas_mes = horas_dia * 31
    elif n_mes in [4, 6, 9, 11]:
        horas_mes = horas_dia * 30
    elif n_mes == 2:
        horas_mes = horas_dia * 28

    return horas_mes


def calcula_salario(valor_hora, horas_mes):
    "A função realiza o calculo da salário."
    salario = (valor_hora * horas_mes)
    print('Valor salário: R${:.2f}'.format(salario))


def main():
    "Corpo principal do programa."
    quant_horas_mes = calcula_horas_mes(8, 3)
    calcula_salario(5.16, quant_horas_mes)



main()