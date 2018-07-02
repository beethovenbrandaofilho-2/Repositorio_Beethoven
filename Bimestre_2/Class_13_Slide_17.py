class Peel:
    def __init__(self, peelCount):
        self.peelCount = peelCount

    def getPeelCount(self):
        return self.peelCount


class Fruit:
    def peel(self):
        print("Peeling is appealing")
        return Peel(1)


class Apple:
    def __init__(self):
        self.fruit = Fruit()

    def peel(self):  # classe Apple é modificada
        self.peel = self.fruit.peel()
        return self.peel.getPeelCount()


apple = Apple()  # programa cliente não requer modificacao
pieces = apple.peel()
print(pieces)
