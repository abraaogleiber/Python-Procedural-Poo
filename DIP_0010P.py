
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 10 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver uma solução prática para orçamento de tintas
#___________________________________________________________________#

from math import ceil


def __calcula_quantidade_tinta(area):
    """

    area: Recebe a área repassada pelo usuário na função 'main'.
    A função retorna a quantidade de litros e repassa à função '__calcula_quantidade_latas()'.
    """
    area_pintada_por_litro = 3
    quant_tinta = (area / area_pintada_por_litro)
    return __calcula_quantidade_latas(quant_tinta=quant_tinta)


def __calcula_quantidade_latas(quant_tinta):
    """

    quant_tinta: Recebe o valor de retorno da função '__calcula_quantidade_tinta()'
    A função retorna a quantidade de latas, pra dentro da função '__calcula_valor_orcamento()'.
    """
    quantidade_litros_por_lata = 18
    quant_latas = ceil(quant_tinta / quantidade_litros_por_lata)
    return __calcula_valor_orcamento(quant_latas=quant_latas)


def __calcula_valor_orcamento(quant_latas):
    """

    quant_latas: Recebe o valor de retorno da função '__calcula_quantidade_latas'
    A função retorna o valor do orçamento, pra dentro da função '__formata_saida()'.
    """
    valor_de_uma_lata = 18
    valor_do_orcamento = (quant_latas * valor_de_uma_lata)
    return __formata_saida(valor_do_orcamento=valor_do_orcamento)


def __formata_saida(valor_do_orcamento):
    """
    valor_do_orcamento: recebe o valor de retorno da função '__calcula_valor_orcamento()'.
    A função retorna uma saída formatada.
    """
    print('O orçamento da área fica no valor de R${:.2f}'.format(valor_do_orcamento))


def main():
    """
    Função principal.
    A função somente faz chamadas á outras funções.
    """
    valor_area = float(input('Área(m²): '))
    __calcula_quantidade_tinta(area=valor_area)


main()
