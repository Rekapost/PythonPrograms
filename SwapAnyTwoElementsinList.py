#SWAP ANY TWO ELEMENTS IN A LIST
# SO FIRST DECIDE THE VALUES AND THIER POSITIONS
list=[10,20,30,40,50,60]
print(list)
# i am going to swap list[1]=20 and list[4]=50
"""
# SIMPLE  method 1
list[1],list[4]=list[4],list[1]
print(list)
"""
#SIMPLE method 2
pos1=1               # index no
pos2=4
list[pos1],list[pos2]=list[pos2],list[pos1]
print(list)
#OR
"""
list[1],list[4]=list[4],list[1]
print(list)
"""
"""
#TUPLE METHOD
print(list)
swap=(list[4],list[1])
list[1],list[4]=swap
print(list)
"""
"""
#POP METHOD
print(list)
f=list.pop(1)
l=list.pop(3)
list.insert(1,l)
list.insert(4,f)
print(list)
"""