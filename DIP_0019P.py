
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 17 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um dissecador de médidas, no objetivo de
#              informar a existência de um possivel triângulo e qual seu tipo.
#___________________________________________________________________#

from Python_Procedural.DIP_0018 import saida_formatada


def recolher_medidas():
    """
    -------> A função recolhe as medições, procura exceções e por fim, armazena os valores em um lista.
             A lista é feita global, para que possa ser acessada por outra função.
    retorna: None
    """
    global lados
    lados = []

    for l in range(1, 4):
        try:
            n = float(input(f'{l}º Lado.: '))
            lados.append(n)
        except ValueError:
            print('Não é possivel processar esse valor!. Tente mais uma vez.')
            exit()


def verificar_existencia():
    """
    -------> A função verifica as medições recebida e avalia a possibilidade da existência de um triângulo.
    retorna: Um valor booleano para a função "classificando_triangulo" que irá processar o retorno.
    """
    if lados[0] < (lados[1] + lados[2]) and lados[1] < (lados[0] + lados[2]) and lados[2] < (lados[0] + lados[1]):
        return classificando_triangulo(True)
    else:
        return classificando_triangulo(False)


def classificando_triangulo(exts):
    """
    -------> A função avalia o valor recebido executando o bloco correspondente
            bloco 1 --> Avalia as medições e classifica o triângulo.
            bloco 2 --> Mostra uma mensagem e fecha o programa.
            por fim, faz uma chamada a uma função do módulo "DIP_0018" que gera uma saída formatada.
    parametro exts: Recebe um valor booleano
    retorna: None
    """
    if exts:
        if lados[0] == lados[1] == lados[2]:
            tipo = 'Equilátero'
        elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
            tipo = 'Escaleno'
        else:
            tipo = 'Isósceles'
    else:
        print('Não é possivel ter uma triângulo com essas medições!.')
        exit()

    saida_formatada(f'O triângulo formado é do tipo: {tipo}')


def main():
    """
    -------> A função é o corpo principal e realiza chamadas de funções.
    retorna: None
    """
    recolher_medidas()
    verificar_existencia()


main()