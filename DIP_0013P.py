
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 12 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um identificador alfabético
#___________________________________________________________________#


def tratar_caracteres(texto: str):
    """
    ------> A função trata o texto repassado, quebrando e criando uma lista com letras.
    :parametro texto: Recebe o texto.
    :return: Uma lista de letras que é passado como argumento ao parâmetro de "classificar_caracteres()"
    """
    palavras_texto = texto.split()

    letras_texto = list()
    for palavra in palavras_texto:
        for letra in palavra:
            letras_texto.append(letra)

    return classificar_caracteres(letras=letras_texto)


def classificar_caracteres(letras):
    """
    ------> A função gera uma contabilidade e classificação de cada caracter da lista.
    :parametro letras: Recebe uma lista de letras.
    :return: Uma lista com variaveis simples com o resultado da análise.
    """
    n_neutro = 0
    n_vogais = 0
    n_consuantes = 0
    n_nao_identificados = 0

    for letra in letras:
        if letra in ('b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y'):
            n_consuantes += 1
        elif letra in ('a', 'e', 'i', 'o', 'u'):
            n_vogais += 1
        elif letra == 'h':
            n_neutro += 1
        else:
            n_nao_identificados += 1

    return [n_consuantes, n_vogais, n_neutro, n_nao_identificados]


def relatorio_final(resultado: list, txt: str):
    """
    ------> A função gera uma saída bem amigavel e clara para o entendimento.
    :parametro resultado: Recebe uma lista de variaveis simples com valores da análise.
    :parametro txt: Recebe o texto, que o usuário repassou.
    :return: Imprime o relatório na tela.
    """
    print('{:º^51}'.format(' Relatório da análise '))
    print('\n'
          f'Texto informado: <{txt}>\n'
          '\n'
          f'Número de consuantes: {resultado[0]}\n'
          f'Número de vogais: {resultado[1]}\n'
          f'Número de neutra("H"): {resultado[2]}\n'
          f'Número de não identificadas: {resultado[3]}\n'
          '\n')
    print('º'*51)


def main():
    """
    ------>
    :return:
    """
    texto = str(input('Texto: ')).strip().lower()

    lista_resultados = tratar_caracteres(texto=texto)
    relatorio_final(resultado=lista_resultados, txt=texto)


main()


