# 9 CRIAR EXEMPLO DE PROGRAMA COM O PADRAO FABRICA ABSTRATA
# Fabrica de Naves

import abc

class Tamanho_Nave(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def tamanho(self):
        pass

class Velocidade_Nave(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def velocidade(self):
        pass

class Fabrica_Abstrata(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def definir_tamanho(self):
        pass

    @abc.abstractmethod
    def definir_velocidade(self):
        pass

class Pequena(Tamanho_Nave):
    def tamanho(self):
        print("Nave de pequeno porte! 10m.")

class Media(Tamanho_Nave):
    def tamanho(self):
        print("Nave de medio porte! 20m.")

class Grande(Tamanho_Nave):
    def tamanho(self):
        print("Nave de grande porte! 30m.")

class Baixa(Velocidade_Nave):
    def velocidade(self):
        print("Nave com velocidade baixa! 1/5 da velocidade da luz.")

class Mediana(Velocidade_Nave):
    def velocidade(self):
        print("Nave com velocidade mediana! 1/3 da velocidade da luz.")

class Alta(Velocidade_Nave):
    def velocidade(self):
        print("Nave com velocidade alta! 1/2 da velocidade da luz.")

class Fabrica_Tamanho(Fabrica_Abstrata):
    def definir_tamanho(self, tamanho):
        if tamanho == None:
            return None
        if tamanho == "PEQUENA":
            return Pequena()
        elif tamanho == "MEDIA":
            return Media()
        elif tamanho == "GRANDE":
            return Grande()
        return None
    def definir_velocidade(self):
        return None

class Fabrica_Velocidade(Fabrica_Abstrata):
    def definir_tamanho(self):
        return None
    def definir_velocidade(self, velocidade):
        if velocidade == None:
            return None
        if velocidade == "BAIXA":
            return Baixa()
        elif velocidade == "MEDIANA":
            return Mediana()
        elif velocidade == "ALTA":
            return Alta()
        return None

class Produtor:
    def definir_fabrica(escolha):
        if escolha == "TAMANHO":
            return Fabrica_Tamanho()
        elif escolha == "VELOCIDADE":
            return Fabrica_Velocidade()
        return None

def main():
    print("Bem vindo a nossa fabrica de naves!")

    print("Primeiro, temos algumas opcoes para o tamanho da nave")
    print("CONTACTANDO O SETOR DE TAMANHOS...")
    tamanho_fabrica = Produtor.definir_fabrica("TAMANHO")
    tamanho_1 = tamanho_fabrica.definir_tamanho("PEQUENA")
    tamanho_1.tamanho()
    tamanho_2 = tamanho_fabrica.definir_tamanho("MEDIA")
    tamanho_2.tamanho()
    tamanho_3 = tamanho_fabrica.definir_tamanho("GRANDE")
    tamanho_3.tamanho()

    print("Agora, temos algumas opcoes para a velocidade da nave")
    print("CONTACTANDO O SETOR DE VELOCIDADES...")
    velocidade_fabrica = Produtor.definir_fabrica("VELOCIDADE")
    velocidade_1 = velocidade_fabrica.definir_velocidade("BAIXA")
    velocidade_1.velocidade()
    velocidade_2 = velocidade_fabrica.definir_velocidade("MEDIANA")
    velocidade_2.velocidade()
    velocidade_3 = velocidade_fabrica.definir_velocidade("ALTA")
    velocidade_3.velocidade()

    print("Qual sera a sua escolha?")

main()