
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 23 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Desenvolver um gerador da sequência de Fibonacci
#___________________________________________________________________#


class Fibonacci:
    """
    ------> A classe executa uma logica capaz de encontar a sequência de Fibonacci..
    """
    def __init__(self):
        """
        ------> O método inicializador, define os valores iniciais para montagem da sequência de Fibonacci.
        """
        self.anterior = 1
        self.atual = 1
        self.posterior = (self.anterior + self.atual)


    def encontra_fibonacci(self, num_elemento):
        """
        ------> O método realiza uma serie de iterações afim de encontrar o numero desejado
                de termos da sequência de Fibonacci, a cada laço, gera uma saida.
        parametro num_elemento: Recebe a quantidade desejada de termos
        retorna: None
        """
        print(f'{self.anterior} -> {self.atual}', end='')
        for i in range(2, num_elemento):
            print(f' -> {self.posterior}', end='')

            self.anterior = self.atual
            self.atual = self.posterior
            self.posterior = (self.anterior + self.atual)



if __name__ == '__main__':

    try:
        quant = int(input('Quantos termos fibonacci você deseja ver: '))
    except ValueError:
        exit('Você digitou um texto, frase ou palavra!.')

    meu_fibo = Fibonacci()
    meu_fibo.encontra_fibonacci(quant)