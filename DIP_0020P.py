
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 18 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um algoritmo que consiga calcular raízes
#              de equações do 2ºGrau
#___________________________________________________________________#


"""
    O módulo disponibiliza uma função que efetua o calculo da raiz de uma equação do 2ºGrau.
"""

def encontrar_delta(a=1, b=1, c=1):
    """
    -------> A função efetua validação e encontra a quantidade de raízes que tem a equação.
    parametro a: Recebe o valor de "A" na formula.
    parametro b: Recebe o valor de "B" na formula.
    parametro c: Recebe o valor de "C" na formula.
    retorna: A quantidade de raizes da equação.
    """
    global delta

    if a == 0:
        print('Essa equação não é do 2ºGrau!.')
        exit()
    else:
        delta = (b ** 2) - (4 * a * c)

        if delta == 0:
            quant_raiz = 1
        elif delta < 0:
            quant_raiz = 0
        elif delta > 0:
            quant_raiz = 2

        return quant_raiz


def encontrar_raizes(a, b, c, q_raiz):
    """
    --------> A função encontra as raízes da equação e após executa uma saída formatada.
    parametro a: Recebe o valor de "A" na formula.
    parametro b: Recebe o valor de "B" na formula.
    parametro c: Recebe o valor de "C" na formula.
    parametro q_raiz: Recebe a quantidade de raizes que tem a equção, serve para validação.
    retorna: None
    """
    if q_raiz == 0:
        print('Essa equação não possui raíz, desde que seu delta seja menor que zero(0)!.\n'
              'Valor do delta(descriminante) ---> {}'.format(delta))
        exit()
    elif q_raiz == 1:
        raiz1 = (b / (2 * a))
        print(f'A raiz da equação do 2ºGrau é {raiz1}.')
    elif q_raiz == 2:
        raiz1 = (b + delta) / (2 * a)
        raiz2 = (b - delta) / (2 * a)
        print(f'A equação do 2ºGrau possui duas(2) raízes, são elas: (R1)---> {raiz1}\n'
              f'                                                     (R2)---> {raiz2}')


def main():
    """
    -------> A função representa o corpo principal do programa. Efetuando chamadase e a caça de exceções.
    retorna: None
    """
    print('Formula: ax² + b + c = 0')
    print('-'*35)

    try:
        a = int(input('Valor de "A": '))
        b = int(input('Valor de "B": '))
        c = int(input('Valor de "C": '))
    except ValueError:
        print('Impossivel continuar!...')
        print('-' * 35)
        exit()

    print('-'*35)

    encontrar_raizes(a, b, c, encontrar_delta(a, b, c))


main()