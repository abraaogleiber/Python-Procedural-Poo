
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 15 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um analisador de preços
#___________________________________________________________________#


class Produto():

    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco


    @property
    def GetNome(self):
        return self.__nome

    @property
    def GetPreco(self):
        return self.__preco



class Analisador:

    def __init__(self, prods):
        self.__prods = prods
        self.analisar_produto()
        self.produto_barato()


    @property
    def GetProduto(self):
        return self.__prods


    def analisar_produto(self):
        self.__melhor_produto = self.GetProduto[0]

        for prod in self.GetProduto:
            if prod.GetPreco < self.__melhor_produto.GetPreco:
                self.__melhor_produto = prod


    def produto_barato(self):
        print('O produto mais em conta é o(a) {} com valor R${:.2f}'.format(self.__melhor_produto.GetNome, self.__melhor_produto.GetPreco))



if __name__ == '__main__':

    produtos = []
    while True:
        print('{:¨^75}'.format(' Adicione um produto '))

        try:
            nome = str(input('Nome: ')).strip().capitalize()

            if nome == 'E' and len(produtos) == 0:
                exit()
            elif nome == 'E':
                break
            elif nome.isdigit() or len(nome) == 0:
                raise ValueError


            preco = float(input('Preço(R$): '))

            produto = Produto(nome=nome, preco=preco)
            produtos.append(produto)

            print('\n')
            print('Obs. Digite "e" no campo NOME quando terminar de adicionar os produtos.')

        except Exception:
            print('ERRO.: O nome deve ser "alfabético" e o preço "numerico"!.')
            exit()

    analise = Analisador(produtos)
