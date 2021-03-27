
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 23 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um gerador da sequência de Fibonacci
#___________________________________________________________________#

"""
-----> O módulo fornece uma maneira simples para geração de termos da sequência de Fibonacci.
"""

def sequencia_fibonacci(n_termos):
    """
    --------> A função atraves de iteração encontra a quantidade de termos da sequência de Fibonacci.
    parametro n_termos: Recebe a quantidade de termos que será encontrado.
    retorna: None
    """
    anterior = 1
    atual = 1
    posterior = (anterior + atual)

    for i in range(1, n_termos-1):
        if i == 1:
            print(f'{anterior} -> {atual}', end='')
        print(f' -> {posterior}', end='')

        anterior = atual
        atual = posterior
        posterior = (anterior + atual)


def main():
    """
    -------> A função executa o corpo principal da aplicação. Efetuando chamada de função e coleta de dados.
            Além disso, faz a captura de exceções.
    retorna: None
    """
    try:
        n_termos = int(input('Número de termos: '))
    except ValueError:
        exit('O valor de entrada não é válido!.')

    sequencia_fibonacci(n_termos)


main()