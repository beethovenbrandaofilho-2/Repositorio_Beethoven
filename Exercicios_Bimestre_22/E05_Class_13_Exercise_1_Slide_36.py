# 5 IDENTIFIQUE NO PROJETO DO GRUPO SITUACOES ONDE OS PRINCIPIOS SOLID PODERIAM SER (OU FORAM) APLICADOS

"""
No projeto desenvolvido utilizando FLASK foram utilizados alguns dos princípios SOLID, visando
uma boa e eficiente construção de código. Dentre os princípios que se destacaram na realização
do projeto, é possível ilustrar:

1) S - Princípio da Única Responsabilidade:
Algumas classes criadas no projeto cumprem esse princípio, ou seja, estão associadas a um
único emprego/responsabilidade. Dentre essas classes é possível citar as classes relacionadas
aos formulários de envio de vagas e de cadastro do usuário, que possuem função única de criação
dos formulários.

4) I - Princípio da Segregação de Interface:
O projeto foi desenvolvido de tal forma que nenhuma das classes realizasse a implementação
de interfaces desnecessárias. Ao realizar a análise das classes associadas aos formulários
tem-se que estas implementam apenas o suficiente para que seu funcionamento seja realizado
de forma satisfatória, cumprindo suas funções primordiais.
"""