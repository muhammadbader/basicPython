import math

import one
import unittest

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        res = one.cap_text(text)
        self.assertEqual(res,"Python")

    def test_mult_word(self):
        text = "monty python"
        res = one.cap_text(text)
        self.assertEqual(res, "Monty Python")

# if __name__=="__main__":
    # unittest.main()
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n,m= input().split()
    n=int(n)
    m=int(m)
    # n = int(nm[0])

    # m = int(nm[1])
    # print(n,m)
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    x=sorted(arr,key=lambda x:x[k])
    for i in x:
        print(i)