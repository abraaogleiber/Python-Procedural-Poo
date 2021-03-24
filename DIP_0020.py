
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 18 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um algoritmo que consiga calcular raízes
#              de equações do 2ºGrau
#___________________________________________________________________#


#----> Formula : Ax² + B + C = 0
# ---> Verificar possivel existência de uma raiz, dado os valores dos elementos da equação.
        # ----> r < 0 (negativo)  Nenhuma raiz
        # ----> r = 0 (nulo)  Uma raia
        # ----> r > 0 (positivo)  Duas raiz



class EquaRaiz:
    """
        A classe disponibiliza uma maneira prática para encontrar raízes de equações do 2ºGrau.
    """

    __slots__ = ('_a', '_b', '_c')

    _raiz_1 = None
    _raiz_2 = None

    def __init__(self, a=1, b=1 , c=1):
        try:
            if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
                self._a = a
                self._b = b
                self._c = c
            else:
                raise TypeError
        except TypeError:
            print('Impossivel continuar. Erro na atribuição de valores!.')
            exit()

        self.__calcular_descriminante()


    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c


    def __calcular_descriminante(self):
        """
        -------> O método realiza o calculo do delta, e o torna global, além de encerrar o programa caso o
                 valor de "A" seja igual a zero(0).
        retorna: O delta para dentro do método que irá determinar a quantidade de raizes da equação.
        """
        global descriminante

        if self._a == 0:
            print('A Equação não é do 2ºGrau!.')
            exit()
        descriminante = (self._b) ** 2 - (4 * self._a * self._c)
        return self.__validar_equacao(descriminante)


    def __validar_equacao(self, delta):
        """
        -------> O método avalia o delta e define a quantidade de raízes da equação.
        parametro delta: Recebe o delta.
        retorna: A quantidade de raízes da equação para dentro do método responsável pelo calculo da raíz.
        """
        if delta == 0:
            quant_raiz = 1
        elif delta < 0:
            quant_raiz = 0
        elif delta > 0:
            quant_raiz = 2
        return self.__encontrando_raiz(quant_raiz)


    def __encontrando_raiz(self, q_raiz):
        """
        -------> O método realiza o calculo da raíz(zes) da equação.
        parametro q_raiz: Recebe a quantidade de raízes da equação.
        retorna: O valor da(s) raíz(es) para dentro de um método que irá mostrar ao usuário.
        """
        if q_raiz == 0:
            print('Esta Equação não possui raiz, já que seu delta é menor que zero(0) -- Negativo.')
            print('Valor do delta ---> {}'.format(descriminante))
            exit()
        elif q_raiz == 2:
            EquaRaiz._raiz_1 = (self._b + descriminante) / (2 * self._a)
            EquaRaiz._raiz_2 = (self._b - descriminante) / (2 * self._a)
            return self.__raizes_encontradas(EquaRaiz._raiz_1, EquaRaiz._raiz_2)
        else:
            EquaRaiz._raiz_1 = (self._b ) / (2 * self._a)
            print(EquaRaiz._raiz_1)
            return self.__raizes_encontradas(EquaRaiz._raiz_1)


    def __raizes_encontradas(self, r1=None,  r2=None):
        """
        -------> O método mostra o valor da(s) raíz(es) da equação.
        parametro r1: Recebe a primeria raiz.
        parametro r2: Se houver, recebe a segunda raiz da equação.
        retorna: None
        """
        if r2 == None:
            print(f'A raiz encontrada foi {r1}')
        else:
            print(f'As duas raízes encontradas foram --> Raiz(1) {r1}\n'
                  f'                                     Raiz(2) {r2}')



if __name__ == '__main__':
    teste = EquaRaiz(a=3, b=5, c=6)
