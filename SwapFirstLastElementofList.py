#swap first and last numbers in an array
list=[10,20,30,40,50,60]
n=len(list)
"""
#temp method 1:
temp=list[0]
list[0]=list[n-1]
list[n-1]=temp
print(list)
"""
"""
#method 2
list=[10,20,30,40,50,60]
list[0],list[-1]=list[-1],list[0]
print(list)
"""
"""
#method 3
#tuple method
list=[10,20,30,40,50,60]
print(list)
swap=(list[-1],list[0])
list[0],list[-1]=swap
print(list)
"""
""""
#  * operand method
list=[10,20,30,40,50,60]
start,*middle,end=list
list=[end,*middle,start]
print(list)
"""
"""
#POP method
list=[10,20,30,40,50,60]
f=list.pop(0)          # index
l=list.pop(-1)
list.insert(0,l)
list.append(f)
print(list)
"""