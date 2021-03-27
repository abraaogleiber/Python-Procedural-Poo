
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 20 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um contador de valores pares e impares
#___________________________________________________________________#


def analisar_valores():
    """
    ------->
    retorna:
    """
    lista_valores = []
    for valor in range(1, 11):

        try:
            v = int(input(f'{valor}º Valor: '))
        except ValueError:
            print('Somente valores numericos!.')
            exit()

        lista_valores.append(v)


    pares, impares = [], []
    num_pares, num_impares = 0, 0

    for valor in lista_valores:
        if valor % 2 == 0:
            pares.append(valor)
            num_pares += 1
        else:
            impares.append(valor)
            num_impares += 1


    print('')
    print('Dos valores repassados temos: ')
    print(f'{num_pares} Pares -----> {pares}')
    print(f'{num_impares} Impares ---> {impares}')



def main():
    """
    ------->
    retorna:
    """
    analisar_valores()


main()