class Fruit:
    def peel(self):
        print("Peeling is appealing")
        return 1

class Apple:
    def __init__(self):
        self.fruit=Fruit()  # composicao

    def peel(self):
        return self.fruit.peel()

apple=Apple()
pieces=apple.peel()
print(pieces)
