
# coding: utf-8

# In[19]:


# Crie um exemplo usando metodos abstratos, metodos estaticos e metodos de classe. 
# O exemplo deve ilustrar as vantagens de cada tipo de metodo

##############################################################
# Metodos regulares - passam a instancia (self)

# a) abstractmethod:  
# Funcoes associadas podem ser concluidas posteriormente
# Util em projetos extensos, com grupos de trabalho grandes

# b) staticmethod 
# Nao passa a instancia e nem a classe
# Pode ser usado para implementar funcoes que nao precisam
# de informacoes alem de determinados parametros especificos

# c) classmethod 
# Nao passa a instância, e sim a classe
# Pode ser utilizado como construtor alternativo
##############################################################

import abc

class SomeMajorClass(object):
    __metaclass__ = abc.ABCMeta
    partial = 20
    
    def __init__(self):
        self.total = 10
    
    @staticmethod
    def another_function(multiplier, number):
        if multiplier == 2:
            print("It is even!")
        elif multiplier == 0:
            print("It is zero!")
        return number*multiplier
    
    @classmethod
    def some_another_function(cls):
        new_partial = cls.partial
        return new_partial

    @abc.abstractmethod
    def some_function(self):
        # It can be finished later
        pass
        
class SomeMinorClass(SomeMajorClass):
    def some_function(self, some_argument = 0):
        # Now it do something
        if some_argument:
            return self.total
        else: 
            return 0
        
first_test =  SomeMinorClass.some_function(0)
second_test = SomeMajorClass.another_function(2, 5)
third_test = SomeMajorClass.some_another_function()

print(first_test)
print(second_test)
print(third_test)

