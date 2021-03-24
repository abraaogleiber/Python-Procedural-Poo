
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 20 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um contador de valores pares e impares
#___________________________________________________________________#


class Valores:

    __lista_valores = list()

    def __init__(self):

        for valor in range(1, 11):
            try:
                v = int(input('{}º Valor: '.format(valor)))
                Valores.__lista_valores.append(v)
            except ValueError:
                print('Só é possivel com valores numericos!. Tente novamente.')
                exit()


    def retorna_lista_valores(self):
        """
        ------>
        retorna:
        """
        if len(Valores.__lista_valores) > 0:
            return Valores.__lista_valores



class Identificador:

    __lista_pares = []
    __lista_impares = []

    def __init__(self, lista_valores):
        self.__lista_valores = lista_valores


    @property
    def valores(self):
        return self.__lista_valores


    def analisador(self):
        """
        ------>
        retorna:
        """
        for valor in self.valores:
            if valor % 2 == 0:
                self.__lista_pares.append(valor)
            else:
                self.__lista_impares.append(valor)


    def contabilizador(self):
        """
        ------>
        retorna:
        """
        if len(self.__lista_impares) != 0 or len(self.__lista_pares) != 0:
            print('')
            print('Foram identicados, {} pares e {} impares.'.format(len(self.__lista_pares), len(self.__lista_impares)))
            print(f'Pares: {self.__lista_pares} ----------> Impares: {self.__lista_impares}')
        else:
            print('Antes de contabilizar é preciso analisar os valores!.')



if __name__ == '__main__':
    a = Valores()
    b = Identificador(a.retorna_lista_valores())
    b.analisador()
    b.contabilizador()

    print(a.__init__().__doc__)