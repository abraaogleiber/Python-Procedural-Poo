
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 08 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Criar uma solução que converta graus fahrenheit para celsius
#___________________________________________________________________#


def __imprimir_temperatura(resultado=00.0):
    "Imprimi a saída do valor convertido. "
    print('A temperatura convertida é {:.1f}ºC'.format(resultado))


def __converte_para_celsius(temperatura_fahrenheit=00.0):
    "Executa o calculo de conversão da temperatura."
    graus_celsius = ((temperatura_fahrenheit - 32) / 9) * 5

    return __imprimir_temperatura(graus_celsius)


def colheta_temperatura():
    "Faz a colheta do valor entrado pelo usuário. "
    try:
        temperatura = float(input('Temperatura(ºF): '))
        return __converte_para_celsius(temperatura_fahrenheit=temperatura)
    except ValueError:
        print('Por gentileza, utilize somente valores numericos.')


def main():
    "Corpo principal do programa."
    colheta_temperatura()


main()
