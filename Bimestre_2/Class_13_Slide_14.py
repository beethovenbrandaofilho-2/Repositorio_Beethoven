class Fruit:
    """fruta"""
    def peel(self):
        """retorna o número de cascas"""
        print("Peeling is appealing")
        return 1

class Apple(Fruit):
    pass

apple=Apple()
pieces=apple.peel()
print(pieces)
