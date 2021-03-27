
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 05 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Calculando média
#___________________________________________________________________#

def recebendo_numeros(arm):
    "A função colherá as notas e armazenará em uma lista."

    for nota in range(1, 5):
        nota = float(input(f'{nota}º Nota: '))
        arm.append(nota)


def calculando_media(arm):
    "A função calculará a média, interando nota por nota."

    soma = 0.0
    for nota in arm:
        soma += nota
    media = (soma / len(arm))

    return media


def main():
    "Função principal da aplicação"

    notas_atuais = []
    try:
        recebendo_numeros(notas_atuais)
        media = calculando_media(notas_atuais)
        print('A média do aluno é {}'.format(media))

    except Exception:
        print('Por gentileza, somente valores numericos!!.')



main()
