
# coding: utf-8

# In[5]:


def cleanword(s):
    other_carachters = "!'@#$%¨&*()-_+=´`^~;:/?.>,<\|"
    word_cleaned = ""
    for x in s:
        if x not in other_carachters:
            word_cleaned += x
    return word_cleaned

def has_dashdash(s):
    really_do = False
    counter = 0
    for x in s:
        if x == '-':
            counter += 1
        else: 
            counter = 0
        if counter == 2:
            really_do = True
            return really_do
    return really_do

def extract_words(s):
    other_carachters = "!'@#$%¨&*()-_+=´`^~;:/?.>,<\| "
    result = []
    word = ''
    a = len(s) - 1
    for i in range(len(s)):
        if s[i] not in other_carachters:
            if s[i].isupper():
                word += (s[i].lower())
            else:
                word += (s[i])
        elif s[i] in other_carachters and word is not '':
            result.append(word)
            word = ''
        if i == a and s[i] not in other_carachters:
            result.append(word)
    return result

def wordcount(s, t):
    counter = 0
    for i in range(len(t)):
        if s == t[i]:
            counter += 1
    return counter

def wordset(s):
    words = []
    for i in range(len(s)):
        new_word_not_present = True
        for aux in range(len(words)):
            if (s[i] == words[aux]):
                new_word_not_present = False
        if new_word_not_present:
            words.append(s[i])
    new_words = sorted(words)
    return new_words

def longestword(t):
    counter = 0
    maximum = 0
    for i in range(len(t)):
        counter = len(t[i])
        if counter > maximum:
            maximum =  counter
    return maximum

