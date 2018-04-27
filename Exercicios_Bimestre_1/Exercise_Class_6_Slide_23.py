
# coding: utf-8

# In[33]:


# Pesquise o assunto Decoradores. Desenvolva um Decorador exemplo.

class Person(object):
    def __init__(self, last_name, first_name, profession):
        self.last_name = last_name
        self.first_name = first_name
        self.profession = profession

def some_function(argument_related):
    def decorate_related_to_that_function(function_to_be_decorated):
        def new_function_to_be_returned(a):
            return "<" + argument_related + ">" + function_to_be_decorated(a) + "</" + argument_related + ">"
        return new_function_to_be_returned
    return decorate_related_to_that_function

@some_function("p")
@some_function("div")
@some_function("strong")
def return_some_part(a):
    return "One of my favorite celebrities is %s %s. He/She is a/an %s" %(a.first_name, a.last_name, a.profession)

a = Person("Kubrick", "Stanley", "Director")
return_some_part(a)


# In[56]:


# Crie um exemplo de funcao com lista de argumentos e dicionario de argumentos

def factory(product, market, *company_news, **company_division):
    print("The Rolling StonesTM is a British company")
    print("It is a", product, "company")
    print("It is conquering the", market, "market\n")
    
    for information in company_news:
        print(information)
        
    for elements in company_division:
        print(elements, ":", company_division[elements])
        
factory("Steel", "American", "Some of the companys departments are growing", "Jobs openings are increasing\n", Trainee='Mick Jagger', Manager='Keith Richards', Director='Brian Jones', Department='Sales', HR_Grade='9.0')

