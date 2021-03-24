
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 10 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um maneira de estimar o tempo de download pelo tamanho do arquivo
#___________________________________________________________________#


class TaxaDownload:
    """
    A classe reuni um conjunto de métodos que quando executados calculam valores e retorna
    o tempo estimado de Download.
    """
    __velocidade_internet_MB = 0.0
    __taxa_transferencia = 0.0

    def __init__(self, velocidade_internet=0.0, tamanho_arquivo=0.0):
        try:
            if isinstance(velocidade_internet, float) or isinstance(tamanho_arquivo, float):
                self.__velocidade_internet_Mbps = velocidade_internet
                self.__tamanho_arquivo = tamanho_arquivo
                self.converter_Mbps_para_MB()
                self.calcular_tempo_download()
                self.formata_saida()
            else:
                raise TypeError
        except TypeError:
            print('Só é possivel calcular valores numericos(fracionados)')


    @property
    def GetVelocidadeInternetMB(self):
        return TaxaDownload.__velocidade_internet_MB
    @GetVelocidadeInternetMB.setter
    def SetVelocidadeInternetMB(self, velocidade):
        if isinstance(velocidade, float):
            TaxaDownload.__velocidade_internet_MB = velocidade

    @property
    def GetTaxaTransferencia(self):
        return TaxaDownload.__taxa_transferencia
    @GetTaxaTransferencia.setter
    def SetTaxaTransferencia(self, taxa):
        if isinstance(taxa, float):
            TaxaDownload.__taxa_transferencia = taxa

    @property
    def GetVelocidadeInternetMbps(self):
        return self.__velocidade_internet_Mbps

    @property
    def GetTamanhoArquivo(self):
        return self.__tamanho_arquivo


    def converter_Mbps_para_MB(self):
        """
        O método converte a velocidade em (Mbps) para (MB) e altera o atributo de classe '__velocidade_internet_MB'
        """
        VALOR_1_MEGABYTE = 8
        self.SetVelocidadeInternetMB = (self.GetVelocidadeInternetMbps / VALOR_1_MEGABYTE)


    def calcular_tempo_download(self):
        """
        O método calcula a taxa de transferência e altera o atributo de classe '__taxa_transferencia'.
        """
        self.SetTaxaTransferencia = (self.GetTamanhoArquivo / self.GetVelocidadeInternetMB) / 60


    def formata_saida(self):
        """
        O método imprime atraves de um print uma saida formatada dos valores processados.
        """
        print('Tempo de Download estimado para o arquivo de {:.2f}(MB) é {:.2f}(m)'.format(self.GetTamanhoArquivo, self.GetTaxaTransferencia))




if __name__ == '__main__':

    while True:
        try:
            velocidade_mbps = float(input('Velocidade da internet(Mbps): '))
            tamanho_MB = float(input('Tamanho do arquivo(MB): '))

            teste = TaxaDownload(velocidade_internet=velocidade_mbps, tamanho_arquivo=tamanho_MB)
            break
        except ValueError:
            print('Somente valores numericos!.\n')
            continue