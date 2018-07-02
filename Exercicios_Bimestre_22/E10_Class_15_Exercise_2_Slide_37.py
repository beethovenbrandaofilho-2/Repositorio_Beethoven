# 10 CRIAR EXEMPLO DE PROGRAMA COM O PADRAO MEDIADOR
# Bolsa de valores

class Empresa():
    def __init__(self, mediador, nome):
        self.mediador = mediador
        self.nome = nome

    def vendendo_acoes(self, msg):
        print(self.nome + " esta vendendo as seguintes acoes: " + msg)
        self.mediador.enviar_oferta(msg, self)

    def comprando_acoes(self, msg):
        print(self.nome + " esta comprando as seguintes acoes: " + msg)

class Mediador():
    def __init__(self):
        self.empresas = []

    def adicionar_empresa(self, empresa):
        self.empresas.append(empresa)

    def enviar_oferta(self, msg, empresa):
        for u in self.empresas:
            if u != empresa:
                u.comprando_acoes(msg)

def main():

    mediador = Mediador();

    empresa_1 = Empresa(mediador, "Ibovespa")
    empresa_2 = Empresa(mediador, "Dow Jones")
    empresa_3 = Empresa(mediador, "Yahoo")

    mediador.adicionar_empresa(empresa_1)
    mediador.adicionar_empresa(empresa_2)
    mediador.adicionar_empresa(empresa_3)

    print("Bolsa de Valores em alta!")
    empresa_1.vendendo_acoes("Apple")
    empresa_2.vendendo_acoes("Google")
    empresa_3.vendendo_acoes("IBM")

main()