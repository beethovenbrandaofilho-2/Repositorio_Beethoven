
# coding: utf-8

# In[1]:


# Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar multiple of v by s. :

import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)
    
def scalar_mult(b, a):
    for i in range(len(a)):
        a[i] = b*a[i] 
    return a

def test_suite():
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

test_suite()

