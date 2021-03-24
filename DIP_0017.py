
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 16 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Mostrar os valores de entrada do término ao início
#___________________________________________________________________#


class Indicio:

    def __init__(self, valores):
        """
        -------> O método inicializador, faz chamada ao metodo de transposição.
        parametro valores: Recebe uma lista de valores numericos.
        """
        self.__valores = valores


    @property
    def GetValores(self):
        return self.__valores
    @GetValores.setter
    def SetValores(self, valor):
        self.__valores


    def ordem_crescente(self):
        """
        -------> O método executa a transposição de elementos da lista, organizando os elementos de forma crescente.
        retorna:  Um "print" dá lista alterada.
        """
        aux = 0
        for x in range(len(self.GetValores)):
            for y in range(x+1, len(self.GetValores)):
                if self.GetValores[x] > self.GetValores[y]:
                    aux = self.GetValores[x]
                    self.SetValores[x] = self.GetValores[y]
                    self.SetValores[y] = aux

        print(self.GetValores)


    def ordem_decrescente(self):
        """
        ------> O método realiza a transposição de valores  da lista, ordenando os elementos de forma
                decrescente.
        retorna: Um "print" da lista alterada.
        """
        aux = 0
        for x in range(len(self.GetValores)):
            for y in range(x+1, len(self.GetValores)):
                if self.GetValores[x] < self.GetValores[y]:
                    aux = self.GetValores[x]
                    self.SetValores[x] = self.GetValores[y]
                    self.SetValores[y] = aux

        print(self.GetValores)



if __name__ == '__main__':

    valores = []
    for v in range(5):
        try:
            num = int(input('Número: '))
        except ValueError:
            print('Não é possivel trabalhar com valores que não sejam inteiros!.')
            exit('Impossivel continuar com a execução...')

        valores.append(num)

    teste = Indicio(valores)
    teste.ordem_decrescente()
    teste.ordem_crescente()
