
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 10 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver uma solução prática para orçamento de tintas
#___________________________________________________________________#

"""
A classe armazena um conjunto de métodos protegidos, que de forma automática realiza a tarefa
primaria, de calcular e definir um orçamento para clientes de uma loja de tintas.
"""
from math import ceil


class OrcamentoTintas:
    """
    A classe armazena um conjunto de métodos protegidos, que de forma automática realiza a tarefa
    primaria, de calcular e definir um orçamento para clientes de uma loja de tintas. Para tal
    recebe um unico parâmetro, chamado 'area' que informa o valor da área a ser pintada.
    """
    __valor_orcamento = 0.0
    __quantidade_litros = 0.0
    __quantidade_latas = 0

    def __init__(self, area):
        try:
            if isinstance(area, str):
                raise TypeError
            else:
                self.__area = area
                self.__calculando_quantidade_de_litros()
                self.__calculando_quantidade_de_latas()
                self.__calculando_valor()
                self.__imprime_saida_formatada()

        except TypeError:
            print('Por favor, somente valores numericos.')


    @property
    def GetValorOrcamento(self):
        return OrcamentoTintas.__valor_orcamento
    @GetValorOrcamento.setter
    def SetValorOrcamento(self, valor):
        OrcamentoTintas.__valor_orcamento = valor

    @property
    def GetQuantidadeLitros(self):
        return OrcamentoTintas.__quantidade_litros
    @GetQuantidadeLitros.setter
    def SetQuantidadeLitros(self, quantidade):
        OrcamentoTintas.__quantidade_litros = quantidade

    @property
    def GetQuantidadeLatas(self):
        return OrcamentoTintas.__quantidade_latas
    @GetQuantidadeLatas.setter
    def SetQuantidadeLatas(self, quantidade):
        OrcamentoTintas.__quantidade_latas = quantidade

    @property
    def GetArea(self):
        return self.__area


    def __calculando_quantidade_de_litros(self):
        """
        O método pega o valor da área(m²) e divide por 3, que é o valor em metros(m²)
        que 1 litro pinta.
        """
        self.SetQuantidadeLitros = (self.GetArea / 3)


    def __calculando_quantidade_de_latas(self):
        """
        O método pega a quantidade de litros que foi calculado, divide por de 18, que é
        a quantidade de litros de uma lata e retorna a quantidade de latas necessarias para pintar
        a área. O valor é arredondado pra cima.
        """
        self.SetQuantidadeLatas = ceil(self.GetQuantidadeLitros / 18)


    def __calculando_valor(self):
        """
        O método realiza o calculo do valor, levando em consideração o número de latas
        multiplicado pelo valor da lata.
        """
        self.SetValorOrcamento = (self.GetQuantidadeLatas * 80)


    def __imprime_saida_formatada(self):
        """
        O método formata uma saída elegante, das informações processadas.
        """
        print('{:-^50}'.format(' Relatório de orçamento '))
        print('Área informada: {:.2f}'.format(self.GetArea))
        print('Quantidade em (ls) necessario para pintar: {:.2f}'.format(self.GetQuantidadeLitros))
        print('Quantidade de latas necessarias para pintar: {}'.format(self.GetQuantidadeLatas))
        print('\nValor do orçamento: {}'.format(self.GetValorOrcamento))
        print('-'*50)




if __name__ == '__main__':
    teste = OrcamentoTintas('dfg')
