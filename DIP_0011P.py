
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 10 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um maneira de estimar o tempo de download pelo tamanho do arquivo
#___________________________________________________________________#


def converte_mbps_para_MB(velocidade_mbps):
    """
    A função recebe velocidade(mbps, ainda não convertida)
    e retorna a velocidade em MB(já convertida).
    """
    VALOR_1_MEGABYTE = 8
    velocidade_mb = (velocidade_mbps / VALOR_1_MEGABYTE)

    return velocidade_mb


def calcula_tempo_download(velocidade_mb, tamanho_mb):
    """
    A função recebe velocidade(já convertida pra MB) e tamanho do arquivo(MB)
    e retorna o tempo de Download.
    """
    tempo_download = (tamanho_mb / velocidade_mb)

    return tempo_download


def main():
    """
    A função é o corpo principal do programa, e faz varias chamadas de funções.
    """
    while True:
        try:
            velocidade = float(input('Velocidade da internet(Mbps): '))
            tamanho = float(input('Tamanho do arquivo(MB): '))
            break
        except ValueError:
            print('Por gentileza, somente valores reais.')
            continue

    velocidade_mb = converte_mbps_para_MB(velocidade_mbps=velocidade)
    taxa_transferencia = calcula_tempo_download(velocidade_mb=velocidade_mb, tamanho_mb=tamanho)

    print('O tempo de Download estimado de um arquivo de {:.2f}(MB) é de {:.3f}(s)'.format(tamanho, taxa_transferencia))



main()

