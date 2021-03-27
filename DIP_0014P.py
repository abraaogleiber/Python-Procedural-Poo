
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 15 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um programa que identifica o maior valor
#___________________________________________________________________#


def maior(n):
    """
    -------> A função busca e define o maior valor da lista recebida.
    parametro -> n: Recebe uma lista de valores numericos.
    retorna: Um identificador e o maior valor encontrado na lista recebida.
    """
    maior_num = n[0]
    for num in n:
        if num > maior_num:
            maior_num = num
    return saida_resultado(0, maior_num)


def menor(n):
    """
    ------> A função busca e define o menor valor de uma lista recebida.
    parametro -> n: Recebe uma lista de valores numericos.
    retorna: Um identificador e o menor número da lista.
    """
    menor_num = n[0]
    for num in n:
        if num < menor_num:
            menor_num = num
    return saida_resultado(1, menor_num)


def saida_resultado(id, result):
    """
    ------> A função gera uma saída formatada, implementando uma condicional para identificar a forma de tratamento.
    parametro -> id: Recebe um número que identifica uma das funções de processamento da lista de valores recebida.
    parametro -> result: Recebe o menor valor ou o maior valor, depende de qual função retorna.
    retorna: uma saída formatada.
    """
    if id == 0:
        print('O maior valor da lista repassada é {}'.format(result))
    else:
        print('O menor valor da lista repassada é {}'.format(result))


def main():
    """
    -------> A função representa o corpo principal do programa.
    retorna: Uma serie de chamadas e verificações dos valores e funções de processamento, além da coleta de informações.
    """
    print('Para Enterromper o modo de inserção de valores digite "-0".')

    lista_num = []
    while True:
        sequencia_num = str(input('Adicione um número à lista.: '))

        if sequencia_num.isalpha() and sequencia_num in 'e':
            if sequencia_num == 'e' and len(lista_num) == 0:
                exit()
            elif sequencia_num == 'e':
                break

        try:
            lista_num.append(int(sequencia_num))
        except ValueError:
            print('Não foi possivel identificar sua entrada.')


    maior(lista_num)
    menor(lista_num)


main()
