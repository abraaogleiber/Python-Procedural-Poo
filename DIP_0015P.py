
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 15 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um analisador de preços
#___________________________________________________________________#

conteiner_produtos, produto_mais_barato = list(), list()


def cadastrar_produtos():
    """
    ------> A função é modificadora pois acessa uma lista de escopo global e modifica seu estado.
            a lista armaena o nome e o preço do produto que essa função recolhe.
    retorna: Adiciona um produto na lista de produtos.
    """
    interador = int(input('Quantos produtos você vai cadastrar? '))

    for p in range(1, interador+1):
        print('\n{}º produto de {}'.format(p, interador))
        nome = str(input('Nome: '))
        preco = float(input('Preço(R$): '))

        produto = [nome, preco]
        conteiner_produtos.append(produto)


def analisar_produtos():
    """
    ------> A função acessa um conteiner de escopo global e intera seus elementos(produtos), fazendo
            a comparação de valores.
    retorna: Define uma lista com o nome e o preço do produto mais barato.
    """
    produto_barato = conteiner_produtos[0]
    for p in conteiner_produtos:
        if p[1] < produto_barato[1]:
            produto_barato = p

    produto_mais_barato.insert(0, produto_barato[0])
    produto_mais_barato.insert(1, produto_barato[1])


def produto_selecionado():
    """
    ------> A função gera uma saída formatada, imprimindo as informações da lista do produto mais barato.
    retorna: Uma saída formatada.
    """
    print('\nO produto mais em conta, da lista passada é o(a) {} custando R${}'.format(produto_mais_barato[0],
                                                                                       produto_mais_barato[1])
                                                                                       )


def main():
    """
    ------> A função implementa uma interface para as funções do programa.
    retorna: Faz chamadas às funções do programa, interface do programa.
    """
    cadastrar_produtos()
    analisar_produtos()
    produto_selecionado()


main()

