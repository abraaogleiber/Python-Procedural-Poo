
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 07 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um maneira pratica de calcular a área de um quadrado
#___________________________________________________________________#


def calculando_area(valor_lado):
    "Realiza o calculo da área."
    area = (valor_lado ** 2)
    return area


def dobrar_area(area, nVezes):
    "Realiza o calculo de dobragem da área."
    area_dobrada = (area * nVezes)
    return area_dobrada


def main():
    "Corpo princial do programa."
    while True:
        try:
            area = float(input('Área: '))
            dimensionar = int(input('Número de vezes: '))

            a = calculando_area(valor_lado=area)
            d = dobrar_area(area=a, nVezes=dimensionar)

            print(f'Área: {a} ---- ---- ---- ---- {dimensionar}x ---- {d}(m²)')
            break

        except Exception:
            print('Por favor, utilize somente valores válidos.')
            continue


main()




