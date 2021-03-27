
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 17 de Março de 2021
#  Paradigma |> Procedural
#  Objetivo |> Desenvolver um mecânismo para empresas efetuarem o pagamento
#              de salários líquidos.
#___________________________________________________________________


def calcular_salario(v_hora, h_trabalhadas):
    """
    -------> A função calcula o salário-bruto de um funcionário e torna a variavel "salario_bruto" global
             para que possa ser acessivel no módulo inteiro.
    parametro v_hora: Recebe o valor da hora.
    parametro h_trabalhadas: Recebe a quantidade de horas trabalhadas pelo funcionário(a).
    retorna: None
    """
    global salario_bruto
    salario_bruto = (v_hora * h_trabalhadas)


def descontar_impostos():
    """
    -------> A função acessa o valor da variavel feita global na função "calcular_salario()"
             define o taxa do imposto de renda e calcula os demais impostos como inss e fgts.
    retorna: Para dentro da função "calcular_salario_liquido" uma tupla com os impostos.
    """
    if 900 < salario_bruto <= 1500:
        imposto_renda = (salario_bruto * 5) / 100
    elif 1500 < salario_bruto <= 2500:
        imposto_renda = (salario_bruto * 10) / 100
    elif salario_bruto > 2500:
        imposto_renda = (salario_bruto * 20) / 100
    else:
        imposto_renda = 00.00

    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100

    return calcular_salario_liquido((imposto_renda, inss, fgts))


def calcular_salario_liquido(pacotes_impostos):
    """
    -------> A função calcula o salário líquido, acessando a variavel "salario_bruto" e subtraindo os impostos.
            por fim, realiza uma chamada a uma função de saída "saida-formatada".
    parametro pacotes_impostos: Recebe uma tupla com as variaveis referêntes aos impostos.
    retorna: None
    """
    imposto_renda, inss, fgts = pacotes_impostos
    salario_liquido = salario_bruto - (imposto_renda + inss + fgts)

    msg = 'O salário líquido com todos os descontos fica R$'
    saida_formatada(msg, salario_liquido)


def saida_formatada(msg, conteudo=''):
    """
    -------> A função gera uma saida formatada.
    parametro msg: Recebe uma mensagem.
    parametro conteudo: É por padrão '' (string vazia). mas pode ser outro conteúdo que você queira concatenar
                        com a "msg".
    retorna: None
    """
    print(msg, conteudo)


def main():
    """
    -------> A função representa o corpo principal da aplicação. Efetua chamadas de funções e caça exceções.
    retorna: None
    """
    try:
        valor_hora = float(input('Valor da hora.: '))
        horas_trabalhadas = int(input('Carga horária mensal.: '))
    except ValueError:
        print('Os valores repassados não são válidos!.')
        exit()

    calcular_salario(valor_hora, horas_trabalhadas)
    descontar_impostos()
