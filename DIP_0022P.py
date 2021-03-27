
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 22 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver validador de acesso
#___________________________________________________________________#


def recolher_infor():
    """
    -------> A função, faz a coleta de informações (login e senha), através de input`s e a caça de exceções.
    retorna: Se não for encontrado exceções retorna uma tupla com as informações (login e senha).
    """
    print('-'*50)
    login = str(input('Login: ')).strip().upper()
    senha = str(input('Senha: ')).strip().upper()
    print('-'*50)

    try:
        if login.isalnum() and senha.isalnum():
            return (login, senha)
        else:
            raise TypeError
    except TypeError:
        exit('Não é permitido o uso de caracteres especiais!. [*&%$#@+_>...]')


def validador_acesso(dados):
    """
    -------> A função verifica a validade dos dados de acesso.
    parametro dados: Recebe uma tupla com as informações (login e senha)
    retorna: None
    """
    while True:
        login, senha = dados[0], dados[1]
        if login == senha:
            print('O login não pode ser igual à senha!.')
            dados = recolher_infor()
        else:
            print('Acesso concedido!.')
            break


def main():
    """
    -------> Corpo principal da aplicação!. Faz chamadas a outras funções.
    retorna: None
    """
    dados_acesso = recolher_infor()
    validador_acesso(dados_acesso)


main()