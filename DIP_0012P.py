
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 12 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Criar uma solução prática para definir médias esclares
#___________________________________________________________________#


__notas_aluno = list()


def recolher_notas():
    """
    ------> A função recolhe as notas de um aluno e armazena em uma lista
    de escopo global.
    :return: Uma modificação na lista de escopo global.
    """
    for n in range(1, 5):
        print('{:=^30}'.format(f' {n}º Nota '))
        nota = float(input('>>> '))

        if nota < 0 or nota > 10:
            print('ERRO. A nota repassada está fora do padrão.')
            return
        else:
            __notas_aluno.append(nota)


def calcular_media():
    """
    ------> A função calcula a média, acessando a lista de escopo global
    :return: A média calculada, e uma classificação que chamamos de "status".
    """
    somatoria = 0
    for nota in __notas_aluno:
        somatoria += nota

    media = (somatoria / len(notas_aluno))

    print('\n')
    if 0 <= media <= 5:
        status = '<Reprovado>'
    elif 5 < media <= 7:
        status = '<Recuperação>'
    elif 7 < media <= 10:
        status = '<Aprovado>'
    else:
        status = '<INDEFINIDO>'
    return (media, status)


def saida_formatada(media, status):
    """
    ------> A função formata uma saída mais elegante para o usuário.
    :parametro media: Recebe a média de retorno da função "calcular_media".
    :parametro status: Recebe o status da classificação de cada aluno, retornado da função "calcular_media".
    :return: Uma sequência de prints que monta um relatório das notas.
    """
    print('{:=^30}'.format(' Relatório de notas '))
    print('\n'
          f'1º Nota  -------------> {__notas_aluno[0]:.1f}\n'
          f'2º Nota  -------------> {__notas_aluno[1]:.1f}\n'
          f'3º Nota  -------------> {__notas_aluno[2]:.1f}\n'
          f'4º Nota  -------------> {__notas_aluno[3]:.1f}\n'
          '\n'
          f'Status: {status}\n'
          f'Média Final: {media:.1f}\n')
    print('='*30)



def main():
    """
    A função é responsável por chamar as demais funções do moódulo
    que executaram os calculos para definição da média.
    """
    recolher_notas()
    m, s = calcular_media()
    saida_formatada(media=m, status=s)


main()
