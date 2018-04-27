
# coding: utf-8

# In[12]:


# The section in this chapter called Alice in Wonderland, again! 
# started with the observation that the merge algorithm uses a pattern that can be reused in other situations. 
# Adapt the merge algorithm to write each of these functions, as was suggested there:
############################################################################
# ALICE IN WONDERLAND
#def find_unknowns_merge_pattern(vocab, wds):
#    """ Both the vocab and wds must be sorted.  Return a new
#        list of words from wds that do not occur in vocab.
#    """
#
#    result = []
#    xi = 0
#    yi = 0

#    while True:
#        if xi >= len(vocab):
#            result.extend(wds[yi:])
#            return result
#
#        if yi >= len(wds):
#            return result
#
#        if vocab[xi] == wds[yi]:  # Good, word exists in vocab
#            yi += 1
#
#        elif vocab[xi] < wds[yi]: # Move past this vocab word,
#            xi += 1
#
#        else:                     # Got word that is not in vocab
#            result.append(wds[yi])
#            yi += 1
############################################################################
# a) Return only those items that are present in both lists.
def both_lists (first, second):
    result = []
 
    for xi in range(len(first)):
        for yi in range(len(second)):
            if first[xi] == second[yi]:
                result += first[xi] 
    return result
############################################################################
# b) Return only those items that are present in the first list, but not in the second.
def first_list (first, second):
    result = []
    
    for xi in range(len(first)):
        is_not_present_second = True
        for yi in range(len(second)):
            if first[xi] == second[yi]:
                is_not_present_second = False
        if is_not_present_second:
            result += first[xi] 
    return result
############################################################################
# c) Return only those items that are present in the second list, but not in the first.
def second_list (first, second):
    result = []
    
    for yi in range(len(second)):
        is_not_present_first = True
        for xi in range(len(first)):
            if second[yi] == first[xi]:
                is_not_present_first = False
        if is_not_present_first:
            result += second[yi] 
    return result
############################################################################
# d) Return items that are present in either the first or the second list. (MELHORAR)
def any_list (first, second):
    result = []
    
    for xi in range(len(first)):
        for yi in range(len(second)):
            if first[xi] == second[yi]:
                result += first[xi] 
    
    for xi in range(len(first)):
        is_not_present_second = True
        for yi in range(len(second)):
            if first[xi] == second[yi]:
                is_not_present_second = False
        if is_not_present_second:
            result += first[xi] 
            
    for yi in range(len(second)):
        is_not_present_first = True
        for xi in range(len(first)):
            if second[yi] == first[xi]:
                is_not_present_first = False
        if is_not_present_first:
            result += second[yi] 
    return result
############################################################################
# e) Return items from the first list that are not eliminated by a matching element in the second list.
# In this case, an item in the second list “knocks out” just one matching item in the first list. 
# This operation is sometimes called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]
def bagdiff_list (first, second):
    result = []
    
    for xi in range(len(first)):
        is_not_present_second = True
        for yi in range(len(second)):
            if first[xi] == second[yi]:
                is_not_present_second = False
        if is_not_present_second:
            result += first[xi] 
    return result
############################################################################
first = ['0', '1', '2', '3', '4', '5', '6', '7']
second = ['1', '2', '3', '4', '5', '6', '8']
result1 = both_lists(first, second)
result2 = first_list(first, second)
result3 = second_list(first, second)
result4 = any_list(first, second)
result5 = bagdiff_list(first, second)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

