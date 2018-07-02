# 7 CRIAR EXEMPLO QUE ILUSTRE O PADRAO DECORADOR
# Big Kahuna Burger

class Meu_Sanduiche:

    def Ingredientes(self):
        return self.__class__.ingrediente

    def Custo(self):
        return self.__class__.custo

class Sanduiche_Basico(Meu_Sanduiche):

    ingrediente = "Pao de hamburger"

    custo = 2.00

class Acompanhamentos_Lanche(Meu_Sanduiche):

    ingrediente = "Batata Frita e Coca"

    custo = 6.00

class Decorador_Do_Sanduiche(Meu_Sanduiche):

    def __init__(self, outros_ingredientes):
        self.outro_ingrediente = outros_ingredientes

    def Ingredientes(self):
        return self.outro_ingrediente.Ingredientes() + "-" + Meu_Sanduiche.Ingredientes(self)

    def Custo(self):
        return self.outro_ingrediente.Custo() + Meu_Sanduiche.Custo(self)

class Hamburguer(Decorador_Do_Sanduiche):

    ingrediente = "Hamburguer"

    custo = 5.00

    def __init__(self, outro_ingrediente):
        Decorador_Do_Sanduiche.__init__(self, outro_ingrediente)

class Frango(Decorador_Do_Sanduiche):

    ingrediente = "Frango"

    custo = 4.25

    def __init__(self, outro_ingrediente):
        Decorador_Do_Sanduiche.__init__(self, outro_ingrediente)

class Queijo(Decorador_Do_Sanduiche):

    ingrediente = "Queijo"

    custo = 2.50

    def __init__(self, outro_ingrediente):
        Decorador_Do_Sanduiche.__init__(self, outro_ingrediente)

class Tomate(Decorador_Do_Sanduiche):

    ingrediente = "Tomate"

    custo = 3.00

    def __init__(self, outro_ingrediente):
        Decorador_Do_Sanduiche.__init__(self, outro_ingrediente)

class Bacon(Decorador_Do_Sanduiche):

    ingrediente = "Bacon"

    custo = 3.50

    def __init__(self, outro_ingrediente):
        Decorador_Do_Sanduiche.__init__(self, outro_ingrediente)

def main():
    print("Bem-vido ao Big Kahuna!")
    print("Temos algumas opcoes de sanduiches")

    bacon_burguer = Bacon(Queijo(Hamburguer(Sanduiche_Basico())))
    print("\nBacon Burguer: -" + bacon_burguer.Ingredientes())
    print("Preco: R$ " + str(bacon_burguer.Custo()))

    acompanhamento = Acompanhamentos_Lanche()
    print("\nTemos como acompanhamento: " + acompanhamento.Ingredientes())
    print("Custa: R%" + str(acompanhamento.Custo()))

    print("\nQual deseja?")

main()