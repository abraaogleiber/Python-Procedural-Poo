
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 22 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver validador de acesso
#___________________________________________________________________#


from abc import ABC, abstractmethod


class RecolherInfor:
    """
    ------> A classe executa o método responsável pela coleta das informações de acesso.
    """
    def recolher_infor(self):
        """
        -------> o método executa linhas input`s, e armazena os dados recolhidos.
        retorna: None
        """
        print('-'*50)
        senha = str(input('Login: ')).strip().lower()
        login = str(input('Senha: ')).strip().lower()
        print('-'*50)

        try:
            if login.isalnum() and senha.isalnum():
                self.__senha = senha
                self.__login = login
            else:
                raise TypeError
        except TypeError:
            exit('Não é permitido o uso de caracteres especiais!. [#*&()@!.^...]')


    @property
    def senha(self):
        return self.__senha

    @property
    def login(self):
        return self.__login



class AcessoCliente(RecolherInfor):
    """
    ------> A classe disponibiliza um método que faz a verificação de acesso a clientes cadastrados.
            A classe também, herda de "RecolherInfor" e faz uso do métodos especiais (getters e setters)
    """
    def __init__(self):
        self.acessar()


    def acessar(self):
        """
        -------> O método faz a verificação do login e senha, se estiver fora do padrão, e feita uma chamada,
                 novamente ao método de recolhimento (While).
        retorna: None
        """
        self.recolher_infor()
        while True:
            if self.login == self.senha:
                print('Seu login é igual a senha!.. O acesso foi negado.')
                self.recolher_infor()
            else:
                print('Acesso concedido!.')
                # Aqui liberamos o sistema para o cliente, com restrições.
                break



class AcessoPrivado(RecolherInfor):
    """
    ------> A classe implementa um método que efetua a verificação de acesso, A classe herda de "RecolherInfor".
    """
    def __init__(self):
        self.acessar()


    def acessar(self):
        """
        ------> O método verifica os dados para validar o acesso, se os dados não estiverem corretos
                é feita uma chamada ao método de recolhimento.
        retorna: None
        """
        while True:
            self.recolher_infor()
            if self.login == self.senha:
                print('Seu login é igual a senha!.. O acesso foi negado.')
                self.recolher_infor()
            else:
                print('Acesso concedido!.')
                # Aqui liberamos o sistema para o funcionario ou qualquer patente superior, com recursos
                #livres.
                break



if __name__ == '__main__':

    cliente1 = AcessoCliente()
    funcionario1 = AcessoPrivado()