
# coding: utf-8

# In[7]:


# Lists can be used to represent mathematical vectors. 
# In this exercise and several that follow you will write functions to perform standard operations on vectors. 
# Create a script named vectors.py and write Python code to pass the tests in each case.

# Write a function add_vectors(u, v) that takes two lists of numbers of the same length, 
# and returns a new list containing the sums of the corresponding elements of each:

import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)
    
def add_vectors(a,b):
    for i in range(len(a)):
        a[i] = a[i] + b[i] 
    return a

def test_suite():
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

test_suite()

