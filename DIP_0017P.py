
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 16 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Mostrar os valores de entrada do termino ao inicio
#___________________________________________________________________#


def ordenar_crescente(valores):
    """
    -------> A função realiza a transposição dos valores.
    parametro valores: Recebe um lista de valores numericos.
    retorna: Um "print" da lista alterada.
    """
    aux = 0
    for x in range(len(valores)):
        for y in range(x+1, len(valores)):
            if valores[x] > valores[y]:
                aux = valores[x]
                valores[x] = valores[y]
                valores[y] = aux
    print(valores)


def main():
    """
    ------> A função é a principal do programa, responsável por realizar a chamada da função, como também, recebe e
            faz a validação dos valores de entrada.
    retorna: None
    """
    valores = []
    for vz in range(5):
        try:
            num = int(input('Número.: '))
            valores.append(num)
        except Exception:
            print('Só é possivel realizar esta funcionalidade com valores numericos!.')
            exit('Não é possivel dá continuidade ao programa...')

    ordenar_crescente(valores=valores)



main()