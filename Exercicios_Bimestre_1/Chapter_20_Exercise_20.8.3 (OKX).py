
# coding: utf-8

# In[11]:





# In[14]:


# Write a program called alice_words.py that creates a text file named alice_words.txt containing 
# an alphabetical listing of all the words, and the number of times each occurs, in the text version 
# of Alice’s Adventures in Wonderland. (You can obtain a free plain text version of the book, along with many others, 
# from http://www.gutenberg.org.) The first 10 lines of your output file should look something like this:

# Word              Count
# =======================
# a                 631
# a-piece           1
# abide             1
# able              1
# about             94
# above             3
# absence           1
# absurd            2

file_out = open("alice_dictionary.txt", "w")

list_of_words = {}
other_carachters = "!'@#$%¨&*()-_+=´`^~;:/?.>,<\"| 0123456789]["

with open("alice_words.txt", "r") as file_in:
    for line in file_in:
        for word in line.split():
            new_word = ''
            b = len(word)
            for a in range(b):
                if str(word[a]) not in other_carachters:
                    if str(word[a]).isupper():
                        word_aux = str(word[a])
                        new_word += word_aux.lower()
                    else:
                        new_word += str(word[a])
            if new_word in list_of_words:
                list_of_words[new_word] += 1
            else:
                list_of_words[new_word] = 1

new_list_of_words = sorted(list_of_words)

file_out.write("# Word              Count\n")
file_out.write("# =======================\n")

print("# Word              Count")
print("# =======================")

for k in sorted(list_of_words.keys()):
    a = len(str(k))
    b = len(str(list_of_words[k]))
    c = 17 - (a)
    if str(k) is not " ":
        file_out.write("# ")
        file_out.write(str(k))
        file_out.write(c*" ")
        file_out.write(str(list_of_words[k]))
        file_out.write("\n")
    
    print("#", k, c*" ", list_of_words[k])
    
file_in.close()
file_out.close()

# RESULTADO NAO BATE POR UM UNICO MOTIVO APENAS: NAO CONSEGUI ENCONTRAR UM TEXTO BEM FORMATADO 
# COM TODO O LIVRO. ISSO FAZ COM QUE OCORRAM ALGUNS ERROS DE CONTAGEM, ALGUMAS PALAVRAS NAO SEJAM
# BEM IDENTIFICADAS E O ARQUIVO DE TEXTO DE SAIDA SOFRA ERROS. COM QUAISQUER OUTROS EXEMPLOS O 
# RESULTADO E COMO DESEJADO. CASO TIVESSE SIDO DISPONIBILIZADO O TEXTO UTILIZADO PELO EDITOR DO
# LIVRO O RESULTADO SERIA IGUAL.

