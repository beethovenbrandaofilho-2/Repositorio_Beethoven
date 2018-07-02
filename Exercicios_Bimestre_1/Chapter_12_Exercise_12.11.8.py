
# coding: utf-8

# In[2]:


# Create a module named wordtools.py with our test scaffolding in place.
# Now add functions to these tests pass:

import sys
import wordtools

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)

def test_suite1():
    test(wordtools.cleanword("what?") == "what")
    test(wordtools.cleanword("'now!'") == "now")
    test(wordtools.cleanword("?+='w-o-r-d!,@$()'") ==  "word")

def test_suite2():
    test(wordtools.has_dashdash("distance--but"))
    test(not wordtools.has_dashdash("several"))
    test(wordtools.has_dashdash("spoke--"))
    test(wordtools.has_dashdash("distance--but"))
    test(not wordtools.has_dashdash("-yo-yo-"))

def test_suite3():
    test(wordtools.extract_words("Now is the time!  'Now', is the time? Yes, now.") == 
         ['now','is','the','time','now','is','the','time','yes','now'])
    test(wordtools.extract_words("she tried to curtsey as she spoke--fancy") ==
         ['she','tried','to','curtsey','as','she','spoke','fancy'])

def test_suite4():
    test(wordtools.wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wordtools.wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wordtools.wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wordtools.wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

def test_suite5():
    test(wordtools.wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
         ["is", "now", "time"])
    test(wordtools.wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
         ["I", "a", "am", "is"])
    test(wordtools.wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
         ["a", "am", "are", "be", "but", "is", "or"])

def test_suite6():
    test(wordtools.longestword(["a", "apple", "pear", "grape"]) == 5)
    test(wordtools.longestword(["a", "am", "I", "be"]) == 2)
    test(wordtools.longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(wordtools.longestword([ ]) == 0)

print("Test 1")
test_suite1()
print("Test 2")
test_suite2()
print("Test 3")
test_suite3()
print("Test 4")
test_suite4()
print("Test 5")
test_suite5()
print("Test 6")
test_suite6()

