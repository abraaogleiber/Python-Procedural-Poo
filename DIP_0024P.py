
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 23 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Criar um calculador demográfico
#___________________________________________________________________#


def calculo_demografico(pa, ta, pb, tb):
    """
    ------> A função calcula a quantidade de anos que serão precisos para que o país "A" alcance
            o país "B" em população.
    parametro pa: População do país "A"
    parametro ta: Taxa de crescimento do país "A"
    parametro pb: População do País "B"
    parametro tb: Taxa de crescimento do país "B"
    retorna: a quantidade de anos.
    """
    anos = 0
    while pa < pb:
        pa += (pa * ta) / 100
        pb += (pb * tb) / 100

        anos += 1

    return anos


def main():
    """
    ------> Corpo principal do programa. Define o valor de variaveis.
    retorna: None
    """
    pais_a = 80000
    taxa_a = 3

    pais_b = 200000
    taxa_b = 1.5

    quant_anos = calculo_demografico(pais_a, taxa_a, pais_b, taxa_b)
    print('Para que a população do pais "A" alcance a do pais "B" serão precisos de {} ano(s)'.format(quant_anos))


main()
