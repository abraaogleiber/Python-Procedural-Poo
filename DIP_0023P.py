
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 22 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um validador de informações
#___________________________________________________________________#


def recolher_infor():
    """
    -------> A função, faz a coleta de informações e o calculo da idade do usuário.
    retorna: Uma tupla com as informações do usuário.
    """
    from datetime import datetime

    try:
        nome = str(input('Nome: ')).strip().title()
        nasc = int(input('Nascimento: '))
        sexo = str(input('Sexo: ')).strip().upper()
        salario = float(input('Salário(R$): '))
        estado_civil = str(input('Estado Civil: ')).strip().upper()
    except (TypeError,ValueError):
        exit('Foi repassado algum dado inválido!.')

    ano_atual = datetime.now().year
    idade = (ano_atual - nasc)
    return (nome, idade, sexo, salario, estado_civil)


def validador(infor):
    """
    ------> A função, descompacta a tupla com as informações e faz as validações e por fim imprimi uma saída.
    parametro infor: Recebe uma tupla com as infomações do usuário.
    retorna: None
    """
    nome, idade, sexo, salario, estado_civil = infor[0], infor[1], infor[2], infor[3], infor[4]
    if len(nome) > 3 and nome.isalpha():
        if 0 <= idade <= 150:
            if sexo in 'FfMm':
                if salario > 0:
                    if estado_civil in 'SCVD':
                        print('Todas as informações repassadas, são válidas!.')
                    else:
                        exit('Seu estado civil não pode ser identificado!.')
                else:
                    exit('O salário não pode ser igual ou menor que zero(0)!.')
            else:
                exit('O seu sexo não foi identificado, digite (M) masculino ou (F) feminino.')
        else:
            exit('A idade não pode ser menor que zero(0) ou maior que cento e cinquenta anos(150)')
    else:
        exit('O nome não pode ter menos que três(3) letras e deve ser totalmente alfabético!.')


def main():
    """
    ------> A função é o corpo principal do programa e faz chamadas.
    retorna: None
    """
    validador(recolher_infor())


main()