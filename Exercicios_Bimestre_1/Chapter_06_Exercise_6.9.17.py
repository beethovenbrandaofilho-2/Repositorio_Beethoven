
# coding: utf-8

# In[1]:


# Write is_multiple to satisfy these unit tests:

import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)
    
def is_multiple(a,b):
    if a%b == 0:
        return 1
    else:
        return 0

def test_suite():
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

test_suite()

