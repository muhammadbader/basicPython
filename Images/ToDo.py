import re
from functools import reduce

regex = r"[0-9abcdef][0-9abcdef]"

test_str = "0x123fc6"

matches = re.finditer(regex, test_str, re.MULTILINE)
st=""

# x = ["a","b","c"]
# print(reduce(lambda a,b: a,x))
# sr =
# for match in enumerate(matches, start=1):
#     st=match[1].group()+st
print(test_str)
print(f"0x{reduce(lambda a,b: b[1].group()+a, enumerate(matches, start=1),'')}")

# # print("0x{}".format(st))
#
# s = "4.12.19"
# ss="4.13.0"
# print(s<ss)


