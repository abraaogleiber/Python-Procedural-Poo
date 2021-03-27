
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 05 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Dá boas vindas
#___________________________________________________________________#


def mostrar_mensagem(msg):
    "A função mostrará a mensagem."
    print(msg)


def definir_mensagem(modificar=False):
    "A vai definir qual mensagem será impressa."
    if modificar:
        msg = str(input('Defina a mensagem de saída >>  '))
    else:
        msg = 'Olá, meu mundo é você...'
    return mostrar_mensagem(msg=msg)


def main():
    """
    Chama a função responsável por recolher a mensagem
    e a função responsável por imprimir a mesma.
    """

    definir_mensagem(True)



main()

