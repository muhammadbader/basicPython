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

# n = int(input())
# for _ in range(n):
#     card = input()
#     if re.match(r"^[456][\d]{3}(-?\d{4}){3}$",card) and not re.search(r"(\d)\1\1\1",card.replace('-','')):
# #     if re.match(r"^[456](\d{15}|[\d]{3}[-\d{4}]$)",card) and not re.search(r"(\d)\1\1\1",card.replace('-','')): # the same
#         print("Valid")
#     else:
#         print("Invalid")

# TESTER = re.compile(
#     r"^"
#     r"(?!.*(\d)(-?\1){3})"
#     r"[456]"
#     r"\d{3}"
#     r"(?:-?\d{4}){3}"
#     r"$")
# for _ in range(int(input().strip())):
#     print("Valid" if TESTER.search(input().strip()) else "Invalid")

# print(123)