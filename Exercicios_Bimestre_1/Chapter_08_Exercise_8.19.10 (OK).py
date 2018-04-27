
# coding: utf-8

# In[11]:


# Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):

import sys

# External stuff
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)
    
def is_palindrome(s):
    opposite = reverse(s)
    if s == opposite:
        return 1
    else:
        return 0

def test_suite():
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))    
    # Is an empty string a palindrome?

test_suite()

