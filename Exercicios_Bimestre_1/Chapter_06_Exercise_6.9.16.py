
# coding: utf-8

# In[7]:


# Write a function is_factor(f, n) that passes these tests:

import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)
    
def is_factor(a,b):
    if b%a == 0:
        return 1
    else:
        return 0

def test_suite():
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))

test_suite()

