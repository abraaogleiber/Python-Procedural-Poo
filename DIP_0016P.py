
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 16 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Mostrar os valores de entrada do termino ao inicio
#___________________________________________________________________#


def reajuste_salarial(salario):
    """
    -------> A função avalia o valor do salário e efetua o calculo correspondente
            para o reajuste de salaário.
    parametro salario: Recebe o salário do funcionário em questão.
    retorna: Uma saida com o valor reajustado.
    """
    if 0 < salario <= 1000:
       aumento = (salario * 20) / 100
    elif 1000 < salario <= 1500:
        aumento = (salario * 45) / 100
    elif salario > 1500:
        aumento = (salario * 55) / 100
    else:
        print('O salário não pode está abaixo de R$00.00')
        exit()

    novo_salario = (salario + aumento)
    print('O novo salário com reajuste é R${:.2f}'.format(novo_salario))


def main():
    """
    ------> Corpo principal do programa.
    retorna: Faz a chamada da função que calcula o reajuste.
    """
    try:
        reajuste_salarial()
    except TypeError:
        print('O valor digitado não é válido!.')


main()
