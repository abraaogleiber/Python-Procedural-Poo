
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 23 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Criar um calculador demográfico
#___________________________________________________________________#


class PaisA:
    """
    ------> A classe implementa o país "A" e seus atributos, como taxa de crescimento anual e
            a quantidade populacional.
    """
    def __init__(self):
        self.__taxa_crescimento = 3
        self.__populacao = 80000

    @property
    def taxa_crescimento(self):
        return self.__taxa_crescimento

    @property
    def populacao(self):
        return self.__populacao


class PaisB:
    """
    ------> A classe implementa o país "B" e seus atributos, como taxa de crescimento anual e
            a quantidade populacional.
    """
    def __init__(self):
        self.__taxa_crescimento = 1.5
        self.__populacao = 200000

    @property
    def taxa_crescimento(self):
        return self.__taxa_crescimento

    @property
    def populacao(self):
        return self.__populacao


class CrescimentoDemografico:
    """
    ------> A classe implementa um método que realiza o calculo para previsão de crescimento populacional.
    """
    def __init__(self, taxa_a, populacao_a, taxa_b, populacao_b):
        """
        -------> O método é executado na instaciação da classe.
        parametro taxa_a: Taxa de crecimento anual do país "A"
        parametro populacao_a: Quantidade populacinal do país "A"
        parametro taxa_b: Taxa de crecimento anual do país "B"
        parametro populacao_b: Quantidade populacinal do país "B"
        """
        self.__taxa_pais_a = taxa_a
        self.__taxa_pais_b = taxa_b
        self.__populacao_a = populacao_a
        self.__populacao_b = populacao_b


    @property
    def TaxaA(self):
        return self.__taxa_pais_a

    @property
    def TaxaB(self):
        return self.__taxa_pais_b

    @property
    def PopularA(self):
        return self.__populacao_a

    @property
    def PopularB(self):
        return self.__populacao_b


    def calculo_populacional(self):
        """
        -------> O método calcula a quantidade de anos necessarios para que um pais alcance o outro em termos
                 populacionais. Depois gera uma saida.
        retorna: NOne
        """
        anos = 0
        popu_a = self.PopularA
        popu_b = self.PopularB

        while popu_a < popu_b:
            popu_a += (popu_a * self.TaxaA) / 100
            popu_b += (popu_b * self.TaxaB) / 100

            anos += 1

        print('Serão preciso de {} ano(s) para que o país A alcance em população o país B.'.format(anos))



if __name__ == '__main__':
    a = PaisA()
    taxa_a = a.taxa_crescimento
    populacao_a = a.populacao

    b = PaisB()
    taxa_b = b.taxa_crescimento
    populacao_b = b.populacao

    calc = CrescimentoDemografico(taxa_a=taxa_a, taxa_b=taxa_b, populacao_a=populacao_a, populacao_b=populacao_b)
    calc.calculo_populacional()