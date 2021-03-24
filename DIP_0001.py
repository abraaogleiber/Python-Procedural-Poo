
#__________________ Script Python - versão 3.8 _____________________#
#  Autor |> Abraão A.da Silva
#  Data |> 05 de Março de 2021
#  Paradigma |> Orientado à objetos
#  Objetivo |> Dá boas vindas
#___________________________________________________________________#

class HelloWord:

    __mensagem = 'Olá Mundo, olha eu aqui do zero denovo.'

    @property
    def GetMensagem(self):
        return HelloWord.__mensagem
    @GetMensagem.setter
    def SetMensagem(self, nova_mensagem):
        HelloWord.__mensagem = nova_mensagem


    def mostrar_mensagem(self):
        print(self.GetMensagem)




if __name__ == '__main__':
    msg = HelloWord()
    msg.mostrar_mensagem()
    msg.SetMensagem = 'Oi, Olha nós...'
    msg.mostrar_mensagem()


