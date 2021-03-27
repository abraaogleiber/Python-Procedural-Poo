
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 05 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> iteração com usuário, input.
#___________________________________________________________________#

def receber_numero():
    "A função realizará a coleta do numero."

    try:
        numero = int(input('Digite um número: '))
        return imprime_relatorio(num=numero)

    except Exception:
        print('Ops.. Algo deu errado.')


def imprime_relatorio(num):
    "A função se responsabilizará por gera a saída para o usuário."

    print(f'O número que você digitou foi o {num}')


def main():
    "A função principal."
    receber_numero()


main()



