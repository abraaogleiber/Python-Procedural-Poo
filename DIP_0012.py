
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 11 de Março de 2021
#  Paradigma |> Orientação à objetos
#  Objetivo |> Criar uma solução prática para definir médias esclares
#___________________________________________________________________#


class MediaAluno:
    """
    A classe define um conjunto de métodos que são executados de forma autômatica
    e executam operações para calculos da média de um aluno.
    É necessesario repassar 4 argumentos que são referêntes as notas e um outro que é opcional
    que habilita uma saída formatada, por padrão esse argumento é "True".
    """
    def __init__(self, n1=0.0, n2=0.0, n3=0.0, n4=0.0, imprimir=True):
        try:
            self.__n1 = n1
            self.__n2 = n2
            self.__n3 = n3
            self.__n4 = n4

            self.__status = '<Indefinido>'
            self.__imprimir = imprimir

            self.__calcula_notas()
            self.__calculando_media()
            self.__boletin_impresso(self.GetImprimir)

        except Exception:
            print('Por gentileza, verifique as notas que você repassou!.')


    @property
    def GetN1(self):
        return self.__n1

    @property
    def GetN2(self):
        return self.__n2

    @property
    def GetN3(self):
        return self.__n3

    @property
    def GetN4(self):
        return self.__n4

    @property
    def GetImprimir(self):
        return self.__imprimir

    @property
    def GetStatus(self):
        return self.__status
    @GetStatus.setter
    def SetStatus(self, media):
        try:
            if isinstance(media, float):
                if 0 <= media <= 5:
                    self.__status = 'Reprovado'
                elif 5 < media <= 7:
                    self.__status = 'Recuperação'
                elif 7 < media <= 10:
                    self.__status = 'Aprovado'
                else:
                    raise Exception
        except Exception:
            print('Status indefinido, verifique a integridade das notas repassadas.')



    def __calcula_notas(self):
        self.__soma = (self.GetN1 + self.GetN2 + self.GetN3 + self.GetN4)


    def __calculando_media(self):
        self.__media = (self.__soma / 4)
        self.SetStatus = self.__media


    def __boletin_impresso(self, result):
        if result:
            print('*'*45)
            print('1º Nota: {:.1f}'.format(self.GetN1))
            print('2º Nota: {:.1f}'.format(self.GetN2))
            print('3º Nota: {:.1f}'.format(self.GetN3))
            print('4º Nota: {:.1f}'.format(self.GetN4))
            print('\n')
            print('Status: {}'.format(self.GetStatus))
            print('Média Final: {}'.format(self.__media))
            print('*'*45)







if __name__ == '__main__':
    teste = MediaAluno(-1, -9, -7, 10)
