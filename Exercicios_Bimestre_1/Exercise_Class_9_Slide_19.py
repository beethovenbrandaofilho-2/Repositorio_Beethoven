
# coding: utf-8

# In[ ]:


# Faca um programa para comparar o desempenho de threads e processos. 
# Crie uma situacao onde usar thread e mais vantajoso que processos e vice-versa.

# As Threads e os Processos sao bastante diferentes.
# Cada Processo realizado e executado em um endereco de espaco separado
# Para um Processo acessar os recursos de outro processo, devem ser instituidas comunicaoes entre processos
# Ja as Threads existem associadas a um processo e compartilham seus recursos
# Dessa forma, diferentes Threads podem acessar recursos de um mesmo processo
# Uma Thread e um caminho particular de execucao de um processo
# E possivel afirmar que processos podem ocorrer em paralelo
# A principal diferenca entre Processos e Threads se encontra na forma de lidar com a memoria

import multiprocessing
import threading

