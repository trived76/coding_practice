#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    new_str_a = ""
    occurance_check_a = dict()
    not_common_words = 0
    for ind_a, each_word_a in enumerate(a):
        if each_word_a not in occurance_check_a:
            occurance_check_a[each_word_a] = 0
        occurance_check_a[each_word_a] = a.count(each_word_a)
    
    to_be_kept = 0
    for key in occurance_check_a:
        key_occurance_in_b = b.count(key)
        if key_occurance_in_b:
            to_be_kept += min(occurance_check_a[key], key_occurance_in_b)
    
    return abs(len(a) + len(b) - (2 * to_be_kept))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
