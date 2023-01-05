# HOW MANY TIMES A NUMBER IS LISTED IN THE LIST
list=[10,12,13,10,14,10]
"""
#METHOD 1
count =0
n=10
for i in list:
    if (i==n):
        count=count+1
print(count)
# OR
print("{} has occureed {} times" .format(n,count))
"""
"""
#METHOD 2
list=[10,12,13,10,14,10]
x=10
y=list.count(x)     # count()  method
#print(y)
#OR
print("{} appears {} times in list" .format(x,list.count(x)))
"""
#method 3
#counter method
from collections import Counter
list=[10,12,13,10,14,10]
x=10
list1=Counter(list)
print(list1)    #Counter({10: 3, 12: 1, 13: 1, 14: 1})
print(list1[x])  #3
