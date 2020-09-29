# from ipywidgets import interact, interactive,fixed
# import ipywidgets as widgets
#
# from IPython.display import display
# def func(x):return x

# interact(func,x="10")

# @interact(x=True,y=fixed(1.1))
# def g(x,y):
#     return (x,y)

# def f(a,b):
#     display(a+b)
#     return a+b
#
# w = interactive(f,a=20,b=10)
# # print(w.children)
# display(w)


# widgets.IntSlider()

import re
''' __________________________________________________'''

# import re
# def change(match):
#     # print(match.group(0))
#     try:
#         if match.group(0)=='||':
#             return "or"
#         elif match.group(0) == '&&':
#             return "and"
#     except:
#         print("Invalid")

# n = int(input())
# c = 1
# for i in range(n):
#     s = input()
#     x1=(re.sub(r" && | \|\| ", change, s))
#     x2=(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', s))
#     print(c,end='\t'+str(x1==x2))
#     print()
#     c+=1
# s = "x  & &&| && ||  ||  |x"
# x1=(re.sub(r"(?<= )(&&|\|\|)(?= )", change, s))
# x2=(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', s))
# print(x1)
# print(x2)
import re

n = int(input())
for _ in range(n):
    card = input()
    # res = re.findall(r"-",card)
    # print(res)
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-\d{4}){3})$",card) and not re.search(r"(\d)\1\1\1",card.replace("-",'')):
        print("Valid")
    else:
        print("Invalid")

