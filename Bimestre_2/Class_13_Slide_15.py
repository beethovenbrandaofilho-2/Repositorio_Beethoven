class Peel:
    """casca"""

    def __init__(self, peelCount):
        self.peelCount = peelCount

    def getPeelCount(self):
        return self.peelCount

class Fruit:
    """fruta"""

    def peel(self):
        print("Peeling is appealing")
        return Peel(1)

class Apple(Fruit):
    pass

apple = Apple()
pieces = apple.peel()
print(pieces)  # imprime o objeto pieces !!!
