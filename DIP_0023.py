
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 22 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um validador de informações
#___________________________________________________________________#


from abc import ABC, abstractmethod


class Funcionario(ABC):
    """
    -----> A classe é abstrata, e fornece um modelo para coleta de informações e sua disponibilização
           por meio de getters.
    """
    __slots__ = ('__nome', '__idade', '__sexo', '__salario')

    def __init__(self, nome, idade, sexo, salario):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__salario = salario


    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def sexo(self):
        return self.__sexo

    @property
    def salario(self):
        return self.__salario


    @abstractmethod
    def validar_infor(self):
        """
        -------> O método abstrato idealiza um mecânismo de validação de dados.
        retorna: None
        """
        pass



class Validador(Funcionario):
    """
    -----> A classe herda de "funcionario" e implementa seu método abstrato, essa herança é
           para diferência, ou seja, implementa mais um atributo.
    """
    def __init__(self, nome, idade, sexo, salario, estado_civil):
        super().__init__(nome, idade, sexo, salario)
        self.__estado_civil = estado_civil
        self.validar_infor()


    @property
    def estado_civil(self):
        return self.__estado_civil


    def validar_infor(self):
        """
        ------> O método faz a validação de das informações de entrada e gera uma saída.
        retorna: None
        """
        if len(nome) > 3 and nome.isalpha():
            if 0 <= idade <= 150:
                if sexo in 'MF':
                    if salario > 0:
                        if self.estado_civil in 'SCVD':
                            print('Todos os dados e informações estão válidos!.')
                        else:
                            exit('Seu estado civil não pode ser identificado!.')
                    else:
                        exit('O salário não pode ser igual ou menor que zero(0)!.')
                else:
                    exit('O seu sexo não foi identificado, digite (M) masculino ou (F) feminino.')
            else:
                exit('A idade não pode ser menor que zero(0) ou maior que cento e cinquenta anos(150)')
        else:
            exit('O nome deve possuir mais que três(3) caracteres e ser totalmente alfabético!.')



if __name__ == '__main__':

    try:
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: ')).strip().upper()
        salario = float(input('Salário(R$): '))
        estado_civil = str(input('Estado Civil: ')).strip().upper()
    except ValueError:
        exit('Você informou algum dado inválido!. Tente novamente.')

    funcionario1 = Validador(nome, idade, sexo, salario, estado_civil)
