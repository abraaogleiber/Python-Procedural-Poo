
"""
O objetivo é fazer experimentos, de funções, composição, usando a biblioteca de
interfaces gráficas turtle.
"""

import turtle

"""
def __desenhando_poligono(t: turtle.Turtle, quant_lados, lenlado):
    "Responsável por criar o poligono regular de acordo com as definições do usuário."

    angulo = (360 /quant_lados)
    for i in range(quant_lados):
        t.fd(lenlado)
        t.lt(angulo)
"""

def __desenhando_circulo(t, raio, quant_lados, lenlado):
    "Responsável por criar o circulo gráfico na janela."

    angulo = raio
    for i in range(quant_lados):
        t.fd(lenlado)
        t.lt(raio)


def criando_tartaruga_ambiente(lenlado, quant_lados, raio):
    """
    Cria a tartaruga, defini o loop da janela e chama a função responsável
    por realizar o desenho com a tartaruga.
    """

    bob = turtle.Turtle()
    __desenhando_circulo(bob, raio, quant_lados, lenlado)
    #__desenhando_poligono(t=bob, lenlado=lenlado, quant_lados=quant_lados)
    turtle.mainloop()


def main():
    "Corpo principal do programa."

    RAIO = 4
    QUANT_LADOS = 90
    lenlado = int(input('Tamanho da circunferência: '))
    criando_tartaruga_ambiente(lenlado, QUANT_LADOS, RAIO)


main()