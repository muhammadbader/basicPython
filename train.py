# from itertools import groupby
#
#
# def stairs(n):
#     arr = [0]*(n+1)
#     return stairss(n,arr)
#
# def stairss(n,arr):
#     if n == 0:
#         return 1
#     elif n<0:
#         return 0
#     elif arr[n]!=0:
#         return arr[n]
#     else:
#         arr[n] = stairss(n-1,arr)+stairss(n-2,arr)+stairss(n-3,arr)
#     return arr[n]
#
# def MagicalIndex(arr):
#     return MagicalIndex2(arr,0,len(arr))
#
# def MagicalIndex2(arr,start,end):
#     if(start>end):
#         return -1
#     mid = (start+end)/2
#     # print mid
#     # print arr[mid]
#     if arr[mid]==mid:
#         return mid
#     elif arr[mid]>mid:
#         return MagicalIndex2(arr,mid+1,end)
#     else:
#         return MagicalIndex2(arr,start,mid-1)
#
# arr = [123,32,123,123987,56,33,4,10,2,3,4,5,6,7,8,9,9,9898,123111111]
#
# # print MagicalIndex(sorted(arr))
#
#
#
# def powerSet(arr):
#     return powerSet2(arr,0,[[]])
# def powerSet2(arr,i,power):
#     if(i>=len(arr)):
#         return power
#     l=len(power)
#     for num in range(l):
#         tmp= list(power[num])
#         tmp.append(arr[i])
#         power.append(tmp)
#     return powerSet2(arr,i+1,power)
#
# # x = powerSet([1,2,3,4,5,6])
#
#
# def allUnique(str):
#     if len(str)!= 127:
#         print len(str)
#         return False
#     special = [0]*127
#     for ch in str:
#         if special[ord(ch)] == 1: ## already found
#             return False
#         special[ord(ch)] = 1
#     for i in arr:
#         if i!=1:
#             return False
#         return True
#
#
# # print allUnique("1234567890z")
#
# def permutation(str1, str2):
#     perm  =[0]*128
#     for ch in str1:
#         perm[ord(ch)]+=1
#     for ch in str2:
#         perm[ord(ch)]-=1
#
#     for i in perm:
#         if i!= 0:
#             return False
#     return True
#
# def URLify(str,length):
#     x = list(str)
#     length -= 1
#     i=len(x)-1
#     while i>=0:
#         if(x[length]!=' '):
#             # print i
#             x[i]=x[length]
#             length-=1
#             i-=1
#         else:
#             # print "here"
#             length-=1
#             x[i]='0'
#             x[i-1]='2'
#             x[i-2]='%'
#             i-=3
#
#     print ''.join(x)
#
#
# # URLify("mnb mnb mnb    ",11)
#
#
# def PalinPerm(str):
#     str = str.lower()
#
#     chs = [0]*128
#     x=0
#     y=0
#     for ch in str:
#         if ch == ' ':
#             y+=1
#         elif chs[ord(ch)] == 0:
#             chs[ord(ch)] = 1
#         else:
#             chs[ord(ch)] = 0
#     for i in chs:
#         x+=i
#     if((len(str)-y)%2 == 0):
#         return x == 0
#     else:
#         return x == 1
#
#
# # print PalinPerm("Tact coa")
#
# def OneWay(str1,str2):
#     x=False
#     if len(str1)>len(str2)+1 or len(str2)>len(str1)+1:
#         return False
#     elif len(str1)==len(str2):
#         for i in range(len(str1)):
#             if str1[i]!=str2[i]:
#                 if x:
#                     return x
#                 else:
#                     x=True
#     elif len(str1)==len(str2)+1:
#         i=0
#         k=0
#         while k <(len(str2)):
#             if str1[i]!=str2[k]:
#                 if x:
#                     return x
#                 else:
#                     i+=1
#                     x=True
#             else:
#                 i += 1
#                 k += 1
#     elif len(str2)==len(str1)+1:
#         i=0
#         k=0
#         while k <(len(str1)):
#             if str2[i]!=str1[k]:
#                 if x:
#                     return x
#                 else:
#                     i+=1
#                     x=True
#             else:
#                 i += 1
#                 k += 1
#
#     return True
#
# # print OneWay("pal","pale")
#
# def StringComp(str1):
#     if len(str1)==0 or len(str1)==1 or len(str1)== 2:
#         return str1
#     ans = str1[0]
#     ch = str1[0]
#     c = 1
#     for i in range(1, len(str1), 1):
#         if ch != str1[i]:
#             ans = ans+str(c)+str1[i]
#             c = 1
#             ch  = str1[i]
#         else:
#             c+=1
#     # print ans
#     ans = ans +str(c)
#     if len(str1)>len(ans):
#         return ans
#     else:
#         return str1
#
# # print StringComp("aaaaaaaaaaabbbbbbbcccccccc")
#
#
# # three in one stack
# class stacks:
#     def __init__(self,length):
#         self.st1 = 0
#         self.st2 = length/2
#         self.break1 = length/2
#         self.st3 = length-1
#         self.sts = [0]*length
#         self.size=0
#         self.length=length
#
#     def push1(self,x):
#         if self.size < self.length:
#             self.size+=1
#             if self.st1!= self.break1-1:
#                 self.sts[self.st1] = x
#                 self.st1+=1
#             else:
#                 if self.st2!= self.st3-1:
#                     for i in range(self.break1,self.st2,-1):
#                         self.sts[i+1]=self.sts[i]
#                     self.break1+=1
#                     self.sts[self.st1] = x
#                     self.st1 += 1
#                 else:
#                     print "full stack"
#     def pop(self):
#         if self.st1!=0:
#             self.st1-=1
#             return self.sts[self.st1+1]
#
# class SetofStacks:
#     def __init__(self,capacity):
#         self.threshhold = capacity
#         self.stacks = []
#         self.stacks.append([])
#         self.num = 0
#
#
#     def push(self,item):
#         if len(self.stacks[self.num])>= self.threshhold:
#             self.stacks.append([])
#             self.num+=1
#         self.stacks[self.num].append(item)
#
#     def pop(self):
#         if len(self.stacks) == 0 :
#             print "error empty stack"
#         else:
#             x = self.stacks[self.num].pop()
#             if len(self.stacks[self.num])==0:
#                 self.stacks.pop()
#             return x
#
# class AnimalShelter:
#     def __init__(self):
#         self.cats = []
#         self.dogs = []
#         self.both = []
#         self.size = 0
#
#     def queueDog(self,d):
#         self.dogs.append([d,self.size])
#         self.both.append('D')
#         self.size+=1
#     def dequeueDog(self):
#         if len(self.dogs) != 0:
#             x = self.dogs.pop(0)
#             self.both[x[1]] = 'X'
#             return x[0]
#
#     def queueCat(self,c):
#
#         self.cats.append([c,self.size])
#         self.both.append('C')
#         self.size+=1
#     def dequeueCat(self):
#         if len(self.cats) != 0:
#             x = self.cats.pop(0)
#             self.both[x[1]] = 'X'
#             return x[0]
#
#     def queue(self,s,kind):
#         if kind == "Dog":
#             self.queueDog(s)
#         else:
#             self.queueCat(s)
#
#     def dequeue(self):
#         for i in self.both:
#             if i == 'D':
#                 return self.dequeueDog()
#             elif i == 'C':
#                 return self.dequeueCat()
#         print "empty Shelter!!"
#
#
# def TripleStep(n,arr):
#     if n==0:
#         return 1
#     elif n<0:
#         return 0
#     if arr[n]==-1:
#         arr[n] = TripleStep(n-1,arr)+TripleStep(n-2,arr)+TripleStep(n-3,arr)
#     return arr[n]
#
# # print TripleStep(10,[-1]*11)
#
# def powerSet(arr):
#     ans = [[]]
#     for i in arr:
#         x = len(ans)
#         for k in range(x):
#             tmp = list(ans[k])
#             tmp.append(i)
#             ans.append(tmp)
#     return ans
#
# # print (powerSet([1,2,3,4]))
#
# def Coins(n):
#     return Coinsh(n,[-1]*(n+1))
# def Coinsh(n,arr):
#     if n==0:
#         return 1
#     if n<0:
#         return 0
#     if arr[n]==-1:
#         arr[n] = Coinsh(n-1,arr)+Coinsh(n-5,arr)+Coinsh(n-10,arr)+Coinsh(n-25,arr)
#     return arr[n]
#
# def wordFreq(word,book):
#     map ={}
#     for wor in book:
#         if not map.__contains__(wor):
#             map.update({wor:1})
#         else:
#             map.update({wor:map[wor]+1})
#     return map
#
# def intersection(point1,point2):
#     ans = []
#     if point1[0]>= point2[0] and point1[0]<=point2[1]:
#         ans.append(point1[0])
#     elif point2[0]>=point1[0] and point2[0]<=point1[1]:
#         ans.append(point2[0])
#     if point1[1]>= point2[0] and point1[1]<=point2[1]:
#         ans.append(point1[1])
#     elif point2[1]>=point1[0] and point2[1]<=point1[1]:
#         ans.append(point2[1])
#     return ans
#
# def tictactoe(mat):
#     if (mat[0][0]==mat[1][1] and mat[1][1]==mat[2][2]) or (mat[0][2])==mat[1][1] and mat[1][1]==mat[2][0]:
#         return True
#     for i in range(3):
#         if((mat[i][0]== mat[i][1] and mat[i][2]==mat[i][1]) or (mat[0][i] ==  mat[1][i] and mat[1][i]== mat[2][i])):
#             return True
#     return False
#
# class sortStack:
#     def __init__(self):
#         self.stack = []
#         self.helper = []
#         self.size = 0
#
#     def push(self,elem):
#         while len(self.stack)!= 0 :
#             if self.stack[len(self.stack)-1] > elem:
#                 break
#             self.helper.append(self.stack.pop())
#
#         self.stack.append(elem)
#         while len(self.helper)!=0:
#             self.stack.append(self.helper.pop())
#
#     def pop(self):
#         return self.stack.pop()
#
# def ZeroMatrix(matrix):
#     col = [1]*len(matrix)
#     row = [1]*(len(matrix[0]))
#     for j in range(len(matrix)):
#         for i in range(len(matrix[j])):
#             if matrix[j][i] == 0 :
#                 row[i]=0
#                 col[j]=0
#
#     for i in range(len(col)):
#         if col[i]==0:
#             for j in len(row):
#                 matrix[i][j]=0
#
#     for i in range(len(row)):
#         if col[i]==0:
#             for j in len(col):
#                 matrix[i][j]=0
#
#     return matrix
#
#
# def reverse_words_order_and_swap_cases(sentence):
#     # Write your code here
#     ans = ""
#     prev = 0
#     for i in range(len(sentence)):
#         if sentence[i] == ' ':
#             tmp=""
#             # print ans
#             for k in range(prev,i):
#                 if sentence[k] >= 'a' and sentence[k] <= 'z':
#                     tmp = tmp + str.upper(sentence[k])
#                 else:
#                     tmp = tmp + str.lower(sentence[k])
#             ans = " "+tmp + ans
#             prev = i+1
#     # print ans
#     tmp=""
#     for k in range(prev, len(sentence)):
#         if sentence[k] >= 'a' and sentence[k] <= 'z':
#             tmp = tmp + str.upper(sentence[k])
#         else:
#             tmp = tmp + str.lower(sentence[k])
#     ans = tmp + ans
#
#     return ans
#
# # print reverse_words_order_and_swap_cases("aWESOME is cODING")
#
#
# class Car:
#     def __init__(self,maxS,unit):
#         self.maxS=maxS
#         self.unit=unit
#     def __str__(self):
#         return "Car with maximum speed of %d %s"%(self.maxS,self.unit)
#
# # veh = Car(12,"kmp")
# # print veh
#
# def decryptPassword(s):
#     # Write your code here
#     length= len(s)
#     i=0
#     ret=[]
#     while i<length:
#         if s[i]>='0' and s[i]<='9':
#             i+=1
#         else:
#             break
#     k=i
#     if i==length:
#         return s[::-1]
#     elif i>0:
#         i -= 1
#
#     while k<length:
#         if s[k]=='0':
#             ret.append(s[i])
#             k+=1
#             i-=1
#         elif s[k]>='A' and s[k]<='Z':
#             if k+2<length:
#                 if s[k+2]=='*':
#                     ret.append(s[k+1])
#                     ret.append(s[k])
#                     k+=3
#                 else:
#                     ret.append(s[k])
#                     k+=1
#             else:
#                 ret.append(s[k])
#                 k+=1
#         else:
#             ret.append(s[k])
#             k+=1
#     return "".join(ret)
#
# # print decryptPassword("1234")
#
# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     for i in range(len(apples)):
#         apples[i]=apples[i]+a
#     for i in range(len(oranges)):
#         oranges[i]=oranges[i]+b
#     print apples
#     print oranges
#     app=0
#     org=0
#     for i in apples:
#         if i>=s and i<=t:
#             app+=1
#     for i in oranges:
#         if i>=s and i<=t:
#             org+=1
#     print app
#     print org
#
# # countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
#
#
# def gcd(a, b):
#     if a == 0 :
#         return b
#     return gcd(b%a, a)
#
#
# def lcm(a, b):
#     return (a * b) / gcd(a, b)
#
# def getTotalX(a, b):
#     # Write your code here
#     g=0
#     min = b[0]
#     for i in b: # gets the gcd of b and min of b
#         g=gcd(g,i)
#         if min>i:
#             min=i
#     l=1
#     for i in a: # least common multiplier for a
#         l=lcm(l,i)
#     i=1
#     ans=0
#     while i*l<=min:
#
#         if g%(i*l)==0:
#             ans+=1
#         i+=1
#
#     return ans
#
#
# def birthday(s, d, m):
#     sum=0
#     overall=0
#     for i in range(m):
#         sum+=s[i]
#     i=m
#     if sum==d:
#         overall+=1
#     while i<len(s):
#         sum=sum+s[i]-s[i-m]
#         if sum==d:
#             overall+=1
#         i+=1
#     return overall
# # s = map(int, "2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1".rstrip().split())
# # s = map(int, "4 5 4 2 4 5 2 3 2 1 1 5 4".rstrip().split())
# # print birthday(s,18,7)
#
# def migratoryBirds(arr):
#     ans = dict()
#     max=0
#     id=0
#     for i in arr:
#         if i in ans:
#             ans[i]=ans[i]+1
#             if max<ans[i]:
#                 # print ans[i]
#                 max=ans[i]
#                 id=i
#             elif max==ans[i] and id>i:
#                 max = ans[i]
#                 id = i
#
#         else:
#             ans[i]=1
#             if max<ans[i]:
#                 max=ans[i]
#                 id=i
#     # print ans[3], ans[4]
#     return id
#
#
# # x="1 2 3 4 5 4 3 2 1 3 4"
# # arr = map(int, x.rstrip().split())
# # print migratoryBirds(arr)
#
#
# def formingMagicSquare(s):
#     pres = [
#         [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
#         [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
#         [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
#         [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
#         [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
#         [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
#         [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
#         [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
#     ]
#
#
#     totals = []
#     for p in pres:
#         total = 0
#         for p_row, s_row in zip(p, s):
#             for i, j in zip(p_row, s_row):
#                 if not i == j:
#                     total += max([i, j]) - min([i, j])
#         totals.append(total)
#     return min(totals)
#
#
# # Complete the queensAttack function below.
# def queensAttackII(n, k, r_q, c_q, obstacles):
#     cols=dict()
#     rows=dict()
#     ans=0
#     for elem in obstacles:
#         if elem[0] in rows:
#             rows[elem[0]].append(elem[1])
#         else:
#             rows[elem[0]] = [elem[1]]
#         if elem[1] in cols:
#             cols[elem[1]].append([elem[0]])
#         else:
#             cols[elem[1]]=[elem[0]]
#     run=c_q-1
#     end1=0
#     end2=n+1
#     if r_q in rows:
#         x=rows[r_q]
#         for i in x:
#             if i<c_q:
#                 end1=max(end1,i)
#             elif i>c_q:
#                 # print "here"
#                 end2=min(end2,i)
#
#     while run>end1:
#         ans+=1
#         run-=1
#     run=c_q+1
#
#     while run<end2:
#         ans+=1
#         run+=1
#
#     run=r_q-1
#     end1=0
#     end2=n+1
#     if c_q in cols:
#         x=cols[c_q]
#         # print x
#         for i in x:
#             if i<r_q:
#                 end1=max(end1,i)
#             elif i>r_q:
#                 end2=min(end2,i)
#
#     while run>end1:
#         ans+=1
#         run-=1
#
#     run=r_q+1
#     while run<end2:
#         ans+=1
#         run+=1
#     ### diagnosal
#     run=r_q-1
#     end1=c_q-1
#     while run>0 and end1>0:
#         if run in rows:
#             if end1 in rows[run]:
#                 break
#         ans+=1
#         run-=1
#         end1-=1
#
#     run=r_q+1
#     end1=c_q+1
#     while run<n+1 and end1<n+1:
#         if run in rows:
#             if end1 in rows[run]:
#                 break
#         ans+=1
#         run+=1
#         end1+=1
#
#     run=r_q-1
#     end1=c_q+1
#     while run>0 and end1<n+1:
#         if run in rows:
#             if end1 in rows[run]:
#                 break
#         ans+=1
#         run-=1
#         end1+=1
#     # print ans
#     # print "finish here"
#     run=r_q+1
#     end1=c_q-1
#     while run<n+1 and end1>0:
#         if run in rows:
#             if end1 in rows[run]:
#                 break
#         ans+=1
#         run+=1
#         end1-=1
#     # print ans
#     return ans
#
#
# def queensAttack(n, k, r_q, c_q, obstacles):
#     u = n - r_q
#     d = r_q - 1
#     r = n - c_q
#     l = c_q - 1
#     ru = min(u, r)
#     rd = min(r, d)
#     lu = min(l, u)
#     ld = min(l, d)
#     for o in obstacles:
#         if o[1] == c_q:
#             if o[0] < r_q:
#                 d = min(d, r_q - 1 - o[0])
#             else:
#                 u = min(u, o[0] - r_q - 1)
#         elif o[0] == r_q:
#             if o[1] < c_q:
#                 l = min(l, c_q - 1 - o[1])
#             else:
#                 r = min(r, o[1] - c_q - 1)
#         elif abs(o[0] - r_q) == abs(o[1] - c_q):
#             if o[1] > c_q:
#                 if o[0] > r_q:
#                     ru = min(ru, o[1] - c_q - 1)
#                 else:
#                     rd = min(rd, o[1] - c_q - 1)
#             else:
#                 if o[0] > r_q:
#                     lu = min(lu, c_q - 1 - o[1])
#                 else:
#                     ld = min(ld, c_q - 1 - o[1])
#
#     return u + d + r + l + ru + rd + lu + ld
#
#
#
# def biggerIsGreater(w):
#     org = w
#     w = list(w)
#     n = len(w)
#     zeta = n
#     for i in range(n-2,-1,-1):
#         j = [b for b in w[i+1:n] if b>w[i]]
#         if len(j)!=0:
#             zeta=i
#             k = min(j)
#             myind = i+(w[i+1:].index(k))+1
#             w.insert(i,k)
#             del w[myind+1]
#             break
#     newstri = ''.join(w[:zeta+1]+sorted(w[zeta+1:n]))
#     if newstri==org:
#         newstri='no answer'
#     return newstri
#
#
#
# import math
# def calcAngel():
#     degree_sign= u'\N{DEGREE SIGN}'
#
#     AB = int(raw_input())
#     BC = int(raw_input())
#     hyp = math.pow(((AB*AB) + (BC*BC)), 0.5)
#
#     num = (BC*BC) + (hyp*hyp) - (AB*AB)
#     den = (2*(BC*hyp))
#     angle_C = math.degrees(math.acos(num/den))
#
#     print (str(int(round(angle_C))) + degree_sign)
#
#
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# def checkCases(n,cubes):
#     first = 0
#     last = n-1
#     lastAdded = max(cubes[first],cubes[last])
#     while(first<last):
#         if cubes[first]>=cubes[last]:
#             if cubes[first]<=lastAdded:
#                 lastAdded=cubes[first]
#                 first+=1
#             else:
#                 return "No"
#         else:
#             if cubes[last]<=lastAdded:
#                 lastAdded=cubes[last]
#                 last-=1
#             else:
#                 return "No"
#     return "Yes"
#
# def combinatorics():
#     N=int(raw_input())
#     elems = raw_input().split()
#     K = int(raw_input())
#     # from itertools import combination
#     a=0
#     for i in elems:
#         if i=='a':
#             a+=1
#     up=1
#     down=1
#     for i in range(N-a-K+1,N-K+1):
#         up*=i
#     for i in range(N-a+1,N+1):
#         down*=i
#
# def DefaultDictTutorial():
#     from collections import defaultdict
#     d = defaultdict(list)
#     print len(d["a"])
#     mn = map(int, raw_input().rstrip().split())
#
#     for i in range(mn[0]):
#         d[raw_input()].append(i+1)
#     for i in range(mn[1]):
#         for j in d[input()]:
#             print j,
#         print
#
# # import io
# # with open("test.txt",mode ='r+') as filename:
# #     # x=0
# #     filename.write("first line/n")
# #     filename.seek(0,io.SEEK_END)
# #     filename.write("endiiiiing/n")
# #     # filename.write("hello there/nfinish")
# def udemy1():
#     from random import shuffle,randint
#     st="print only the words that strat with s's only ans sec"
#     x=[w[0] for w in st.split() if w[0]=='s']
#
# # sp=[]
# # m=[]
# # for _ in range(int(raw_input())):
# #     name = raw_input()
# #     score = float(raw_input())
# #     sp.append([score,name])
# # score = max(sp)
# # for i in range(len(sp)):
# #     if score>sp[i][0]:
# #         score=sp[i][0]
# #         m=[i]
# #     elif score==sp[i][0]:
# #         m.append(i)
# # for i in reversed(m):
# #     sp.pop(i)
# # m=[sp[0][1]]
# # score =sp[0][1]
# # for i in range(len(sp)):
# #     if score>sp[i][0]:
# #         score=sp[i][0]
# #         m=[sp[i][1]]
# #     elif score==sp[i][0]:
# #         m.append(sp[i][1])
# # for i in sorted(m):
# #     print i
#
#
# # def fountainActivation(locations):
# #     # Write your code here
# #     ret = 0
# #     d = dict()
# #     for i in range(len(locations)):
# #         m = max((i + 1) - locations[i], 1)
# #         if not m in d:
# #             d[m] = [min((i + 1) + locations[i], len(locations))]
# #         else:
# #             d[m].append(min((i + 1) + locations[i], len(locations)))
# #     # print d
# #     k = 1
# #     l=len(locations)
# #     while k <= l:
# #         if k in d:
# #             q = max(d[k])
# #             if q > last:
# #                 last = q
# #                 k = q + 1
# #                 ret += 1
# #             else:
# #                 k -= 1
# #         else:
# #             k -= 1
# #     return ret
#
# def fountainActivation(locations):
#     # Write your code here
#     ret = 1
#     d = dict()
#     for i in range(len(locations)):
#         m = max((i + 1) - locations[i], 1)
#         if not m in d:
#             d[m] = [min((i + 1) + locations[i], len(locations))]
#         else:
#             d[m].append(min((i + 1) + locations[i], len(locations)))
#
#     currMax = max(d[1])
#     right = currMax
#     for i,j in d.items():
#         # print i,j
#         currMax = max(currMax, max(j))
#         if right==i:
#             ret+=1
#             right = currMax
#     return ret
#
#
# def myfunc(s):
#     ss=list(s.lower())
#     for i in range(1,len(ss),2):
#         ss[i]=ss[i].upper()
#     return "".join(ss)
#
# def canJump(A):
#     if len(A)==1:
#         return 1
#     m=A[0]
#     for i in range(len(A)):
#         if m<=i and A[i]==0:
#             return 0
#         if i+A[i]>m:
#             m=i+A[i]
#         if m>=len(A):
#             return 1
#     return 0
#
#
# # print canJump([ 16, 0, 0, 0, 12, 1, 13, 1, 30, 0, 14, 0, 0, 3, 0, 0, 2, 0, 0, 0, 7, 0, 0, 0, 0, 16, 0, 14, 0, 22, 0, 0, 0, 5, 0, 0, 0, 0, 7, 0, 26, 0, 0, 13, 22, 0, 0, 0, 0, 22, 0, 0, 0, 16, 0, 0, 29, 0, 0, 0, 3, 0, 0, 0, 28, 0, 0, 0, 29, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 3, 0, 0, 0, 19, 0, 0, 15, 0, 0, 30, 0, 0, 0, 0, 0, 0, 12, 0, 19, 6, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 12, 0, 24, 16, 21, 0, 8, 0, 14, 6, 0, 0, 5, 23, 0, 22, 0, 15, 15, 0, 26, 0, 14, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 13, 0, 24, 0, 0, 16, 24, 0, 9, 0, 0, 0, 0, 0, 21, 0, 0, 25, 0, 0, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 30, 10, 0, 18, 30, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 29, 0, 0, 0, 8, 7, 29, 16, 30, 0, 0, 3, 0, 0, 0, 17, 0, 0, 22, 0, 0, 0, 0, 0, 18, 0, 0, 11, 11, 0, 0, 0, 0, 11, 19, 2, 0, 0, 0, 2, 0, 16, 11, 21, 0, 10, 0, 29, 0, 0, 0, 0, 0, 1, 15, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 29, 0, 9, 0, 6, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 11, 0, 0, 21, 0, 0, 0, 0, 4, 0, 0, 0, 0, 14, 21, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 14, 0, 0, 0, 0, 29, 24, 0, 4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 25, 0, 9, 0, 0, 0, 0, 24, 21, 12, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 29, 2, 0, 0, 0, 22, 9, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 8, 29, 19, 0, 0, 0, 14, 24, 0, 22, 0, 24, 0, 0, 5, 0, 0, 0, 28, 0, 0, 29, 0, 0, 27, 13, 0, 18, 0, 0, 0, 0, 11, 11, 0, 0, 28, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 12, 0, 0, 12, 19, 23, 0, 20, 0, 8, 6, 23, 17, 14, 0, 0, 24, 3, 0, 0, 0, 6, 11, 24, 0, 0, 0, 0, 0, 0, 18, 0, 0, 1, 27, 0, 1, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 11, 16, 0, 0, 24, 25, 0, 0, 17, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 9, 19, 0, 0, 0, 0, 0, 0, 6, 0, 0, 5, 0, 15, 17, 14, 1, 27, 0, 0, 24, 16, 28, 0, 18, 0, 20, 20, 0, 29, 0, 2, 29, 0, 0, 17, 0, 30, 0, 0, 0, 0, 0, 29, 15, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 16, 0, 0, 0, 0, 0, 0, 18, 20, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 21, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 28, 11, 19, 0, 0, 25, 0, 0, 20, 0, 0, 0, 0, 0, 15, 0, 0, 6, 3, 4, 0, 0, 0, 0, 22, 0, 2, 0, 0, 0, 14, 0, 0, 5, 0, 18, 27, 0, 0, 0, 0, 0, 28, 0, 0, 0, 9, 0, 20, 4, 28, 0, 0, 4, 0, 0, 3, 0, 3, 9, 3, 0, 6, 0, 0, 0, 0, 0, 0, 13, 0, 23, 0, 0, 16, 5, 0, 27, 4, 0, 28, 0, 0, 0, 0, 0, 0, 0, 5, 0, 24, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 10, 28, 0, 0, 0, 22, 14, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 21, 0, 30, 0, 0, 19, 0, 0, 0, 0, 7, 0, 22, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 13, 29, 18, 0, 0, 0, 0, 0, 0, 0, 0, 29, 30, 0, 0, 0, 28, 0, 0, 18, 26, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 27, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 29, 16, 13, 0, 3, 0, 0, 11, 12, 7, 3, 0, 2, 0, 0, 16, 0, 0, 26, 0, 15, 0, 20, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 25, 3, 27, 0, 0, 0, 13, 0, 0, 0, 0, 22, 25, 0, 22, 25, 0, 17, 29, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 28, 8, 1, 0, 0, 0, 0, 0, 29, 15, 16, 0, 0, 0, 0, 0, 0, 23, 28, 0, 0, 0, 2, 0, 12, 27, 0, 22, 0, 0 ])
# # print canJump([ 10, 0, 1, 1, 0 ])
#
#
# def countDifs(s):
#     d = dict()
#     for i in s:
#         if not i in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     f=s=t=0
#     ff=ss=tt='z'
#     for i,j in d.items():
#         if j>f or (j==f and i<ff):
#             t=s
#             tt=ss
#             s=f
#             ss=ff
#             f=j
#             ff=i
#         elif (j>s or (j==s and ss>i)):
#             t = s
#             tt = ss
#             s = j
#             ss = i
#         elif (j>t or (j==t and i<tt)):
#             t=j
#             tt=i
#     print f,ff
#     print s,ss
#     print t,tt
#
# from collections import Counter
#
#
#
#
# # countDifs("qwertyuiopasdfghjklzxcvbnm")
# # countDifs("szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni")
# # x="szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni"
#
# # chars = Counter(x).items()
# # print sorted(chars, key=lambda c: (-c[1], c[0]))
# # for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
# #     print(char, n)
#
# def master_yude(s):
#     return " ".join(reversed(s.split()))
#
#
#
# def spy_game(lst):
#     z=0
#     for i in lst:
#         if i==0 and z<2:
#             z+=1
#         elif z==2 and i==7:
#             return True
#     return False
#
#
# def vol(rad): return 4.0/3* math.pi* rad**3
# def ran_check(num,low,high):return low<=num<=high
# def up_low(s):
#     u=l=0
#     for i in s:
#         if i.islower():
#             l+=1
#         elif i.isupper():
#             u+=1
#     print l,u
#
# def ispangram(s):
#     s=s.lower()
#     letters=[0]*26
#     for i in s:
#         if 'a'<=i<='z':
#             letters[ord(i)-97]+=1
#     for i in letters:
#         if i==0:
#             return False
#     return True
#
#
#
# def tictactoe():
#     board=[['']*3,['']*3,['']*3]
#     for i in board:print i
#     winner = True
#     choice =""
#     while winner:
#         while choice not in range(1,10):
#             choice = input("first player turn!!")
#         ans = choice-1
#         board[ans/3][ans%3]='X'
#         for i in board: print i
#         if chcekWinner(board):
#             print "Player 1 WINS"
#             return
#         choice=""
#         while choice not in range(1,10):
#             choice = input("second player turn!!")
#         ans = choice-1
#         board[ans/3][ans%3]='O'
#         for i in board: print i
#         if chcekWinner(board):
#             print "Player 2 WINS"
#             return
#
# def chcekWinner(board):
#     for i in range(len(board)):
#         if board[i][0]==board[i][1]==board[i][2]!='': return True
#         if board[0][i]==board[1][i]==board[2][i]!='': return True
#     if board[0][0]==board[1][1]==board[2][2]!='' or board[0][2]==board[1][1]==board[2][0]!='':return True
#     return False
#
# class Animal():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):# means abstract class
#         raise NotImplementedError("sub-classes must impelement this abstract method!!")
# class Dog:
#     def __init__(self):
#         print "Dog created!!!"
#     def bark(self):
#         print "WOOF!!!"
#
# class Huskie(Dog):
#     def __init__(self):
#         Dog.__init__(self)
#         print "Huskie breed"
#     def bark(self):
#         print "WOOOOOOOF!!!!"
# # h=Huskie()
# # h.bark()
#
# class Line:
#
#     def __init__(self, coor1, coor2):
#         self.coor1=coor1
#         self.coor2=coor2
#
#
#     def distance(self):
#         return math.sqrt((self.coor1[0]-self.coor2[0])**2+((self.coor1[1]-self.coor2[1])**2))
#
#
#     def slope(self):
#         return (float(self.coor1[1])-self.coor2[1])/(self.coor1[0]-self.coor2[0])
# # coordinate1 = (3,2)
# # coordinate2 = (8,10)
# #
# # li = Line(coordinate1,coordinate2)
#
# class Account():
#
#     def __init__(self,owner,balance=0):
#         self.owner=owner
#         self.balance=balance
#     def deposite(self,money):
#         self.balance+=money
#     def withdraw(self,money):
#         if self.balance<money:
#             print "Funds Unavailable!"
#             return
#         self.balance-=money
#     def __str__(self):
#         return "Account owner:\t {a} \nAccount balance:  {b}".format(a=self.owner,b=self.balance)
#

# Enter your code here. Read input from STDIN. Print output to STDOUT
# x = input()
# up,low,even,odd=[],[],[],[]
# for i in x:
#     if i.islower():
#         low.append(i)
#     elif i.isupper():
#         up.append(i)
#     elif int(i)%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# low.sort()
# up.sort()
# odd.sort()
# even.sort()
# print("".join(low+up+odd+even))


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

'''
20
x| ||&|& | & | &&  &&x
x& & |&||  || &&& & &x
x| &&||&& |  & |  |||x
x|&&& |&||  &|& |&|| x
x&& |   | ||&| |&|| &x
x|& &||& && &&&  &&| x
x|& &| | |&|& &  &| |x
x &&& |& & &||&|&&||&x
x  & &&| && ||  ||  |x
x&&& &&&  &|  || | ||x
x|&|& &&  |&   &|||&|x
x    &&&|&&| ||&&& &&x
x  & || |&&&&&|&&&&| x
x|&|&&&|&| || | &||& x
x&& |&|   |& &&&| && x
x &    &&&&& &|& &| |x
x|& & |   & |&  | |&|x
x&|&|&||||| &|&& || |x
x&|&  &&  |&|  &&&||&x
x || & | &&  &|&| |&|x

'''

# print(hex(1024))
# print(bin(1024))
# print(round(5.23222,2))
# s = 'hello how are you Mary, are you feeling okay?'
# print(s.islower())
# s = "twywywtwywbwhsjhwuwshshwuwwwjdjdid"
# print(s.count('w'))
# set1 = {2,3,1,5,6,8}
# set2 = {3,1,7,5,6,8}
# print(set1.difference(set2))
# print(set1.intersection(set2))
# d = {k:k**3 for k in range(5)}
# print(d)
#
# list1 = [1,2,3,4]
# list1.reverse()
# print(list1)
# list2 = [3,4,2,5,1]
# list2.sort()
# print(list2)


# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print((10**i//9)**2)


# class EvenStream(object):
#     def __init__(self):
#         self.current = 0
#
#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return
#
# class OddStream(object):
#     def __init__(self):
#         self.current = 1
#
#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return
#
#
# def print_from_stream(n, stream = EvenStream()):
#     stream.__init__()
#     for _ in range(n):
#         print(stream.get_next())
#
#
#
# queries = int(input())
# for _ in range(queries):
#     stream_name, n = input().split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)
#     else:
#         print_from_stream(n, OddStream())

# S = input()
# k = input()
import re


# pattern = re.compile(k)
# r = pattern.search(S)
# if not r: print ("(-1, -1)")
# while r:
#     print ("({0}, {1})".format(r.start(), r.end() - 1))
#     r = pattern.search(S,r.start() + 1)


# import math
#
# c='♥'
# width = 40
#
# print ((c*2).center(width//2)*2)
#
# for i in range(1,width//10+1):
#     print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
#            (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)
#
# for i in range(width//4,0,-1):
#     print ((c*i*4).center(width))
# print ((c*2).center(width))


# def eraseOverlapIntervals( intervals):
#     intervals.sort(key=lambda x: (x[1], x[0]))
#     # print(intervals)
#     ans = 1
#     meanwhile = intervals[0][1]
#     for start, end in intervals:
#         if start >= meanwhile:
#             ans += 1
#             meanwhile = end
#     return len(intervals)-ans

# def maxProfit( prices) -> int:
#     left = [0]*len(prices)
#     right = [0]*len(prices)
#     left[0]=0
#     mn=prices[0]
#     # print(mn)
#     for i in range(1,len(prices)):
#         mn = min(prices[i],mn)
#         left[i] = max(left[i-1],prices[i]-mn)
#
#     # for i in range(100,10,-1):
#     #     print(i)
#     mx=prices[-1]
#     for i in range(len(prices)-2,-1,-1):
#         mx = max(mx,prices[i])
#         right[i] = max(right[i+1],mx-prices[i])
#
#     return sum(max(zip(left,right),key=lambda x: x[0]+x[1]))


# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
#
# shoes = int(input())
# sizes = []
# for i in input().split():
#     sizes.append(int(i))
# cus = int(input())
# shoes = Counter(sizes)
# money=0
# for i in range(cus):
#     size,price =input().split()
#     print(shoes)
#     if int(size) in shoes:
#         if shoes[int(size)]==1:
#             del shoes[int(size)]
#             money += int(price)
#         else:
#             shoes[int(size)]-=1
#             money+=int(price)
#
# print(money)

# def distributeCandies(candies, num_people):
#     ans = [0]*num_people
#     i = 0
#     sm = sum(range(1,num_people+1))
#     while ((num_people**2)*i + sm) < candies:
#         candies-=((num_people**2)*i + sm)
#         i += 1
#
#     ans[0] = sum(range(i))*num_people + i
#     for j in range(1,num_people):
#         ans[j]=ans[j-1]+i
#     q=0
#
#     while candies>0:
#         if candies>=(num_people)*i+(q+1):
#             ans[q]+=(num_people)*i+(q+1)
#             candies -= (num_people) * i + (q + 1)
#             q+=1
#         else:
#             ans[q]+=candies
#             candies=0
#     return ans
#
# print(distributeCandies(60,4))

# def nums(x,K):
#     ans = set()
#     if x-K>=0:
#         ans.add(x-K)
#     if x+K<=9:
#         ans.add(x+K)
#     return ans
# def numsSameConsecDiff(N,K):
#     d = {x:nums(x,K) for x in range(10)}
#     print(d)
#
#     tmp=[]
#     if N==1:
#         ans = list(range(10))
#     else:
#         ans = list(range(1,10))
#     for n in range(N-1):
#         for i in ans:
#             if i % 10 in d:
#                 tmp.extend([i * 10 + j for j in d[i % 10]])
#         ans = tmp
#         tmp = []
#     return ans
#
# print(numsSameConsecDiff(1,0))

# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next
#
#
# def reorderList(head: ListNode):
#     reorderListHelp(head, head)
#
#
# def reorderListHelp(head: ListNode, curr: ListNode) -> ListNode:
#     if head == None:
#         return None
#     if curr.next != None:
#         head = reorderListHelp(head, curr.next)
#
#     elif head == curr or head.next == curr:
#         curr.next = None
#         return None
#
#     n = head.next
#     head.next = curr
#     curr.next = n
#
#     print(n.val)
#     return n
#
#
# arr = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# arr = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# reorderList(arr)
#
# for i in range(4):
#     print(arr.val,end="->")
#     arr = arr.next
# print()



