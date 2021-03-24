
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 06 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um maneira pratica de calcular o raio de uma circunferência
#__________________________________________________________________


"O módulo disponibiliza recursos para calculos em circunferências."


class PropriedadesCircunferencia:
    "A classe disponibiliza uma serie de métodos que nos permite explorar as propriedades de uma circunferência."

    __PI = 3.14

    @property
    def GetPI(self):
        return PropriedadesCircunferencia.__PI


    def calcular_raio(self, diamentro):
        "Realiza o calculo do raio, formula: R = d / 2."

        try:
            if isinstance(diamentro, int) or isinstance(diamentro, float):
                raio = (diamentro / 2)
                return self.__saida_formatada(id=0, resultado=raio)
            else:
                raise ValueError
        except ValueError:
            print('Por gentileza, utilize somente valores numericos.')


    def calcular_cumprimento(self, raio):
        "Realiza o calculo do cumprimentodo da circunferência, formula: C = 2.pi.r."

        try:
            if raio is int or raio is float:
                cumprimento = (2 * self.GetPI) * raio
                return self.__saida_formatada(id=1, resultado=cumprimento)
            else:
                raise ValueError
        except:
            print('Por gentileza, somente valores numericos.')


    def calcular_area(self, raio):
        "Realiza o calculo da área da circunferência, formula: A = pi.r²."

        try:
            if isinstance(raio, int) or isinstance(raio, float):
                area = self.GetPI * (raio ** 2)
                return self.__saida_formatada(id=2, resultado=area)
            else:
                raise ValueError
        except ValueError:
            print('Por favor, somente valores numericos.')


    def __saida_formatada(self, id, resultado):
        "O método é protegido por somente ter uso dentro da classe, não servindo como interface."

        if id == 0:
            print('O raio da circunferência é {:.2f}(cm)'.format(resultado))
        elif id == 1:
            print('O cumprimento da circunferência é {:.2f}(cm)'.format(resultado))
        else:
            print('A área da circunferência é {:.2f}(cm²)'.format(resultado))




if __name__ == '__main__':
    x = PropriedadesCircunferencia()
    x.calcular_area()

