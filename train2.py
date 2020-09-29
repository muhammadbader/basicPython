# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except:
#     print("unsupported operation")

# try:
#     x = 5
#     y = 0
#     z = x / y
# except ZeroDivisionError:
#     print("you cann't divide by zero")
# except:
#     print("I give up")
# finally:
#     print("all done!")
import send2trash as send2trash


def ask():
    while True:
        try:
            res=int(input("enter a number: \n"))
            print(f"Input an integer: {res}")
        except:
            print("An error occurred! Please try again!!")
        else:
            print(f"Thank you, your number squared is:  {res**2}")
            break
# ask()

from collections import Counter


mylist = [11,1,1,1,11,12,3,3,123,3,123,3,3,2,123,32,1]
# print(Counter(mylist))


'''
    Collections
'''


from collections import defaultdict

d = defaultdict(lambda : "no key")
d["hi"]=10
# print(d["ss"])
# print(d.keys())


from collections import namedtuple

Dog = namedtuple("Dog",["age","breed","name"])

samy = Dog(12,"husk","samy")
# print(samy)


'''
    OS Module
'''
import os
# import shutil

# d = open("practice.txt","w+")
# d.write("this is a test file")
# d.close()
#
# shutil.move("practice.txt","/Users/muhammadbader/Desktop")


    # similar to terminal commands
# print(os.listdir())
# print(os.getcwd())

# send2trash.send2trash('/Users/muhammadbader/Desktop/practice.txt')
    # sends to the trash can,, we can use rmtree for removing it completely


# for folder,sub_folder,file in os.walk(os.getcwd()):
#     print(f"folder: \t {folder}")
#     for sub in sub_folder:
#         print(f"\t sub_Folder:\t {sub}")
#
#     for fil in file:
#         print(f"\t\tfile:\t {fil}")



'''
        Date & Time
'''


import datetime

# t = datetime.time(2,20,23,19)
# print(t.minute)
# print(t)

# today = datetime.date.today()
# print(today)
# print(today.ctime())




'''
        Random libraries
'''


# import random
#
# lst = [random.randint(0,100) for i in range(15)]
# print(lst)
# print(random.choice(lst))
# #  sampling with repalcements
# print(random.choices(population=lst,k=5))
#
# # sampling without repalcements
# print(random.sample(lst,5))


'''
    Debugger
'''

import pdb

# x =[1,2,3]
# y=2
# z=3
#
# result = y + z
#
# pdb.set_trace() ## signing a debugger break
                ## used like gdb in assembly

# result2 = x + z


'''
        Resular Expressions
'''


import re

# text = "my phone number is 054-6185234, please!!! call my phone."
# pattern = "phone"
# # print(re.search(pattern,text))
# print(re.findall(pattern,text))
#
# for match in re.finditer("phone",text):
#     print(match)
#
# print(re.search(r"\d\d\d-\d\d\d\d\d\d\d",text))
# print(re.search(r"\d{3}-\d{7}",text)) # we can use the + or * also we can use the ? to search for once or more
# print(re.search(r"\d\d\d-\d\d\d\d\d\d\d",text).group())
#
# print(re.search(r"cat|dog","the cat is here"))   # using the pipe operator
#
# print(re.findall(r".at","the cat in the hat and splat"))   # the . operator is the wild card
#
# print(re.findall(r'[^p! .]+',text))  # the r[...] is used to remove the ... from the text


'''
    Timing your code
'''

import time

def func1(n):
    return [str(num) for num in range(n)]

def func2(n):
    return list(map(str,range(n)))


# # CURRENT time
# start_time = time.time()
# # RUN CODE
# res1 = func1(10000000)
#
# # CURRENT TIME after running the code
# end_time = time.time()
# # ELAPSED TIME
# elapsed_time = end_time-start_time
#
# print("function 1")
# print(elapsed_time)
#
# # CURRENT time
# start_time = time.time()
# # RUN CODE
# res2 = func2(10000000)
#
# # CURRENT TIME after running the code
# end_time = time.time()
# # ELAPSED TIME
# elapsed_time = end_time-start_time
#
# print("function 2")
# print(elapsed_time)
        # the time.time() is not efficient enough in some cases





import timeit

stmt = '''
func1(100)
'''
setup = '''
def func1(n):
    return [str(num) for num in range(n)]
'''
# print(timeit.timeit(stmt,setup,number=100000))

stmt = '''
func2(100)
'''
setup = '''
def func2(n):
    return list(map(str,range(n)))
'''
# print(timeit.timeit(stmt,setup,number=100000))



'''
        Zipping and Unzipping files
'''


import zipfile
import shutil


# f = open("fileone.txt","w+")
# f.write("this is one")
# f.close()
#
# f = open("filetwo.txt","w+")
# f.write("this is two")
# f.close()
#
# z_file  = zipfile.ZipFile("compressed_file.zip","w")
# z_file.write("fileone.txt",compress_type=zipfile.ZIP_DEFLATED)
# z_file.write("filetwo.txt",compress_type=zipfile.ZIP_DEFLATED)
# z_file.close()
#
#
# z_obj = zipfile.ZipFile("compressed_file.zip","r")
# z_obj.extractall("extracted_content")

# f = open("extracted_content/Instructions.txt","r")
# print(f.read())
#
# def searches(file,format=r'\d{3}-\d{3}-\d{4}'):
#     f = open(file,'r+')
#     return re.search(format,f.read())
#
# format = r'\d{3}-\d{3}-\d{4}'
# res=[]
# # print(os.getcwd()+"\extracted_content")
# for folder,sub_folder,files in os.walk(os.getcwd()+"/extracted_content"):
#     print(f"folder: \t {folder}")
#     for sub in sub_folder:
#         print(f"\t sub_Folder:\t {sub}")
#
#     for fil in files:
#         if fil==".DS_Store":
#             continue
#         file = f"{folder}/{fil}"
#         res.append(searches(file))
#
# # print(res)
# for i in res:
#     if i!=None:
#         print(i.group())



# import re
# format = "^[\\w-]+@[0-9a-zA-Z]+\\.[a-zA-Z]{1,3}$"
# def fun(s):
#   pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
#   return pattern.match(s)
# # def fun(s):
# #     # return True if s is a valid email, else return False
# #
# #     print(re.search(format,s))
# #     if re.findall(format,s):
# #         return True
# #     else:
# #         return False
#
# def filter_mail(emails):
#     return list(filter(fun, emails))
#
# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())
#
# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)


# ss="britts_54@hackerrank.com"
# s="britts54@hackerrank.com"
# sss="123.123123"
# format2 = r"\d*.\d*"
# format = r"\w*@\w*.\w\w\w"
# print(re.findall(format,ss))

from fractions import Fraction
from functools import reduce

def product(fracs):
    # t = # complete this line with a reduce statement
    t = Fraction(reduce(lambda x,y: Fraction(*[x.numerator*y.numerator,x.denominator*y.denominator]),fracs))
    return t.numerator, t.denominator
#

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    # print(fracs)
    result = product(fracs)
    print(*result)

# lst = [[x,x+1] for x in range(1,10)]
# print(Fraction(*reduce(lambda x,y: [x[0]*y[0],x[1]*y[1]],lst)))
# x=Fraction(*[1,2])
# y=Fraction(*[2,23])
# res = Fraction(*[x.numerator*y.numerator,x.denominator*y.denominator])
# print(res)