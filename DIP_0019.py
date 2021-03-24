
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 17 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um dissecador de médidas, no objetivo de
#              informar a existência de um possivel triângulo e qual seu tipo.
#___________________________________________________________________#

from Python_Procedural.DIP_0018 import saida_formatada


class RecolheLados:
    """
        A classe junta métodos que coletam e armazenam as medições (lados)
    """
    __lista_lados = []

    def __init__(self):
        self.__recolher_lados()

    @property
    def GetArmazenamento(self):
        return RecolheLados.__lista_lados
    @GetArmazenamento.setter
    def SetArmazenamento(cls, l):
        RecolheLados.__lista_lados.append(l)


    def __recolher_lados(self):
        """
        -------> O método faz a coleta de medições, realiza a caça de exceções e
                por fim, passa os valores dentro de uma lista ao método "armazena_lados".
                obs.: se uma exceção for encontrada, o programa é fechado.
        retorna: None
        """
        try:
            l1 = float(input('1º Lado: '))
            l2 = float(input('2º Lado: '))
            l3 = float(input('3º Lado: '))
            self.__armazenar_lados([l1, l2, l3])

        except ValueError:
            print('O valor não é válido!.')
            exit()


    def __armazenar_lados(self, lados):
        """
        -------> O método realiza o armazenamento dos valores de forma devida, acessando-os um por um, atraves
                de um loop "for" e repassando-os ao setter responsável.
        parametro lados: Recebe uma lista de valores, referência os lados.
        retorna: None
        """
        for lado in lados:
            self.SetArmazenamento = lado



class AnalisarLados:
    """
        A classe junta métodos que validam as medições (lados) e classificam os triângulos formados.
    """
    __tipo_triangulo = None

    def __init__(self, lados: RecolheLados):
        self._l1 = lados.GetArmazenamento[0]
        self._l2 = lados.GetArmazenamento[1]
        self._l3 = lados.GetArmazenamento[2]

        existe = self.verificando_existencia()
        self.definindo_tipo(existe)


    def Tipo_triangulo(self):
        """
        -------> O método chama uma função do módulo DIP_0018 da pasta Python_Procedural, que gera uma saída
                cria um variável simples e atribui a ela uma mensagem de saída para a função "saida_formatada".
        retorna: None
        """
        msg = f'As médidas repassadas possibilitam a formação de um triângulo \nTipo: {AnalisarLados.__tipo_triangulo}'
        saida_formatada(msg=msg)


    def verificando_existencia(self):
        """
        -------> O método realiza a verificação de possivel existência de um triângulo.
        retorna: Retona um valor booleano que servirá para validação em outro método.
        """
        if self._l1 < (self._l2 + self._l3) and self._l2 < (self._l1 + self._l3) and self._l3 < (self._l1 + self._l2):
            return True
        else:
            return False


    def definindo_tipo(self, exts):
        """
        -------> O método avalia "exts" e executa um dos dois blocos.
                bloco 1 --> Classifica o triângulo
                bloco 2 --> Mostra uma mensagem e termina a execução.
        :parametro exts: Recebe um valor booleano
        retorna: None
        """
        if exts:
            if self._l1 == self._l2 == self._l3:
                AnalisarLados.__tipo_triangulo = 'Equilátero'
            elif self._l1 != self._l2 and self._l1 != self._l3 and self._l2 != self._l3:
                AnalisarLados.__tipo_triangulo = 'Escaleno'
            else:
                AnalisarLados.__tipo_triangulo = 'Isósceles'
        else:
            print('Não é possivel ter um triângulo com essas médidas!.')
            exit()







if __name__ == '__main__':

    x = RecolheLados()
    y = AnalisarLados(x)
    y.Tipo_triangulo()