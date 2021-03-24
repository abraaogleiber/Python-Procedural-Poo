
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 16 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Mostrar os valores de entrada do termino ao inicio
#___________________________________________________________________#


class ReajusteAutomatico:
    """
    ------>  A classe efetua de forma automatizada, o calculo do reajuste salarial, tendo por base o salario e
            o valor em porcentagem do aumento.
    """
    def __init__(self, salario_atual):
        try:
            if isinstance(salario_atual, int) or isinstance(salario_atual, float):
                self.__salario_atual = salario_atual
            else:
                raise ValueError
        except ValueError:
            print('O valor digitado não é válido!.')
            exit()


    @property
    def GetSalarioAtual(self):
        return self.__salario_atual


    def reajuste_salarial(self):
        """
        ------> O método avalia e calcula o reajuste correto.
        retorna: O aumento de correto para cada salário.
        """
        if 0 < self.GetSalarioAtual <= 280:
            aumento = (self.GetSalarioAtual * 20) / 100
        elif 280 < self.GetSalarioAtual <= 700:
            aumento = (self.GetSalarioAtual * 35) / 100
        elif 700 < self.GetSalarioAtual <= 1250:
            aumento = (self.GetSalarioAtual * 40) / 100
        elif self.GetSalarioAtual > 1250:
            aumento = (self.GetSalarioAtual * 45) / 100
        else:
            print('O salário não pode ser ou está abaixo de R$00.00!.')
            exit()

        self.__novo_salario = (self.GetSalarioAtual + aumento)


    def salario_reajustado(self):
        """
        ------> O método gera uma saída para os dados formatados.
        retorna: Uma saída formatada
        """
        print('O salário do funcionario de {:.2f} passará a ser {:.2f}'.format(self.GetSalarioAtual, self.__novo_salario))



if __name__ == '__main__':
    funcionario = ReajusteAutomatico(100)
    funcionario.reajuste_salarial()
    funcionario.salario_reajustado()


