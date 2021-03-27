
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 06 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um maneira pratica de calcular o raio de uma circunferência
#__________________________________________________________________


def calcula_raio(diametro):
    "Encontra o raio da circunferência."
    raio = (diametro / 2)

    return print('Raio --> {:.2f}'.format(raio))


def calcula_cumprimento(raio):
    "Encontra o cumprimento da circunferência."
    PI = 3.14
    cumprimento = (2 * PI) * raio

    return print('Cumprimento --> {:.2f}'.format(cumprimento))


def calcula_area(raio):
    "Encontra a área da circunferência."
    PI = 3.14
    area = PI * (raio ** 2)

    return print('Área --> {:.2f}'.format(area))


def menu_operetion():
    "Gera um menu de apresentação e direciona o fluxo de execução dos calculos."
    print('{:-^40}'.format(' Menu de Operação '))
    print('>>> Calcular Raio            [1]')
    print('>>> Calcular Cumprimento     [2]')
    print('>>> Calcular Área            [3]')
    print('-'*40)


    try:
        c = False
        option = int(input('>>> '))

        if option == 1:
            diametro = float(input('Diametro da circunferência..: '))
            calcula_raio(diametro=diametro)

        elif option == 2:
            raio = float(input('Raio da circunferência..: '))
            calcula_cumprimento(raio=raio)

        elif option == 3:
            raio = float(input('Raio da circunferência..: '))
            calcula_area(raio=raio)
        else:
            print('Opção inexistente.')

    except ValueError:
        c = True
        print('Por favor, somente valores indicados!.')

    return c   # este retorno controla o fluxo do laço, no "main()".



def main():
    "Corpo principal do código."

    while True:
        if menu_operetion():
            continue
        else:
            break


main()