
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 12 de Março de 2021
#  Paradigma |> Orientado à objeto
#  Objetivo |> Desenvolver um identificador alfabético
#___________________________________________________________________#


class IdenficadorAlfabetico:
    """
    A classe disponibiliza métodos para tratar e idenficar letras e as classificar.
    :parametro texto: Recebe um texto, seguindo as regras para funcionamento
            ----> Letras sem acentuação, mas se for passado, será considerado "letras neutras"
            ----> Evitar a inserção de caracteres especiais, como: '.', '\\', ',', ':', ';', etc
    """

    def __init__(self, texto):
        try:
            if isinstance(texto, str):
                self.__texto = texto.strip()
            else:
                raise AttributeError
        except AttributeError:
            print('Só é possivel analisar textos, frases e palavras!.')
            exit()


    @property
    def GetTexto(self):
        return self.__texto


    def tratar_texto(self):
        __lista_palavras = self.GetTexto.split()

        lista_letra = list()
        for palavra in __lista_palavras:
            for letra in palavra:
                lista_letra.append(letra.lower())

        return self.analisar_letras(letras=lista_letra)


    def analisar_letras(self, letras):
        """
        ------> O método contabiliza caracteres.
        :parametro letras: uma lista de caracteres que foram tratados.
        :return: Uma lista com os resultados da análise.
        """
        consuantes = ('b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y')
        vogais = ('a', 'e', 'i', 'o', 'u')

        num_neutro = 0
        num_vogais = 0
        num_consuantes = 0
        num_nao_identificado = 0

        for letra in letras:
            if letra in consuantes:
                num_consuantes += 1
            elif letra in vogais:
                num_vogais += 1
            elif letra == 'h':
                num_neutro += 1
            else:
                num_nao_identificado += 1

        return self.mostrar_resultado([num_consuantes, num_vogais, num_neutro, num_nao_identificado])


    def mostrar_resultado(self, resultados):
        """
        ------> O método gera uma saída.
        :param resultados: É uma lista com variavais simples que são referência para os valores contabilizados.
        :return: Imprime uma saída formatada dos dados ao usuário.
        """
        print('{:*^51}\n'.format(' Relatório Pós-Análise '))
        print(' Número de Consuantes na frase: {}\n'.format(resultados[0]),
              'Número de Vogais na frase: {}\n'.format(resultados[1]),
              'Número de Caractere neutro(H, h): {}\n'.format(resultados[2]),
              'Número de Caracteres não identificados(â, @, #): {}'.format(resultados[3]),
              '\n',)
        print('*'*51)



if __name__ == '__main__':

    texto = str(input('Texto: ')).strip().lower()
    teste = IdenficadorAlfabetico(texto=texto)
    teste.tratar_texto()

