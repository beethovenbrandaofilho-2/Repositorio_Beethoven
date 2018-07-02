# 11 CRIAR EXEMPLO DE PROGRAMA COM O PADRAO STATE
# 100 metros rasos

import abc

class Desempenho_Fisico(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def velocidade(self):
        pass

    @abc.abstractmethod
    def batimentos(self):
        pass

class Inicio(Desempenho_Fisico):
    def velocidade(self):
        return "Velocidade: 20km/h"

    def batimentos(self):
        return "Frequencia: 80 batimentos por segundo"

class Pico_Desempenho(Desempenho_Fisico):
    def velocidade(self):
        return "Velocidade: 30km/h"

    def batimentos(self):
        return "Frequencia: 110 batimentos por segundo"

class Fim(Desempenho_Fisico):
    def velocidade(self):
        return "Velocidade: 15km/h"

    def batimentos(self):
        return "Frequencia: 140 batimentos por segundo"

class Atleta(Desempenho_Fisico):
    def __init__(self, estado):
        self.estado = estado

    def mudanca_de_desempenho(self, estado):
        self.estado = estado

    def velocidade(self):
        return self.estado.velocidade()

    def batimentos(self):
        return self.estado.batimentos()

def main():

    print("Vamos iniciar a prova dos 100 metros rasos")
    print("Usain Bolt e o nosso grande favorito")

    usainBolt = Atleta(Inicio())
    print("Foi dada a largada!")

    print("Condicoes fisicas iniciais do atleta:")
    print(usainBolt.velocidade())
    print(usainBolt.batimentos())

    usainBolt.mudanca_de_desempenho(Pico_Desempenho())
    print("Nesse momento Bolt ultrapassa todos adversarios")

    print("Condicoes fisicas de pico do atleta:")
    print(usainBolt.velocidade())
    print(usainBolt.batimentos())

    usainBolt.mudanca_de_desempenho(Fim())
    print("Bolt e o campeao!")

    print("Condicoes fisicais finais do atleta:")
    print(usainBolt.velocidade())
    print(usainBolt.batimentos())

main()