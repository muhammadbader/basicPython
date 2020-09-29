'''
a simple comment
'''

def myfunc():
    '''
    inside
    '''
    first = 1
    second = 2
    print(first)
    print(second)

def cap_text(text):
    # return text.capitalize()
    return text.title()

'''
    generators
'''


def gen():
    for i in range(10):
        yield i**4

def gen_fibo(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b


# for i in gen_fibo(20):
# #     print(i)

# g = gen_fibo(2)
# print(next(g))
# print(next(g))
# print(next(g))

def gensquares(N):
    for i in range(N):
        yield i**2

import random
def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)


def convIter(s): return iter(s)


# my_list = [1,2,3,4,5]
#
# gencomp = (item for item in my_list if item > 3)
#
# for item in gencomp:
#     print(item)
