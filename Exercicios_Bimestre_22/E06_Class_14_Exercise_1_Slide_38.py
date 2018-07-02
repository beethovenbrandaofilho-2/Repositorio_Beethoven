# 6 CRIAR EXEMPLO QUE ILUSTRE O PADRAO PONTE
# Aparelhos de lazer e controles

class Aparato_de_Controle:

    def botao_do_Meio_Pressionado(self):
        raise NotImplemented()

class Controle_Remoto(Aparato_de_Controle):

    def __init__(self):
        self._implementation = None

class Controle_TV1(Controle_Remoto):

    def __init__(self, implementacao):
        self._implementation = implementacao

    def botao_do_Meio_Pressionado(self):
        print("Volume minimo")
        self._implementation.botao_de_Cima_Pressionado()

class Controle_TV2(Controle_Remoto):

    def __init__(self, implementacao):
        self._implementation = implementacao

    def botao_do_Meio_Pressionado(self):
        print("Volume maximo")
        self._implementation.botao_de_Cima_Pressionado()

class Aparelho_TV:

    def botao_de_Cima_Pressionado(self):
        raise NotImplemented

class TV_1(Aparelho_TV):

    def botao_de_Cima_Pressionado(self):
        print("Desliga a TV!")

class TV_2(Aparelho_TV):

    def botao_de_Cima_Pressionado(self):
        print("Muda da Antena para HDMI")

def main():
    minha_tv_1 = TV_1()
    minha_tv_2 = TV_2()

    controle_1 = Controle_TV1(minha_tv_1)
    controle_1.botao_do_Meio_Pressionado()
    print("\n")
    controle_1 = Controle_TV1(minha_tv_2)
    controle_1.botao_do_Meio_Pressionado()
    print("\n")
    controle_2 = Controle_TV2(minha_tv_1)
    controle_2.botao_do_Meio_Pressionado()
    print("\n")
    controle_2 = Controle_TV2(minha_tv_2)
    controle_2.botao_do_Meio_Pressionado()

main()