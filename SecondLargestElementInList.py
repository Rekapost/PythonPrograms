list=[20,30,90,1,5]
"""
list.sort()
print(list)
print(list[-2])
"""
list=[20,30,90,1,5]
list1=set(list)
print(list1)                   #{1, 5, 20, 90, 30}
list1.remove(max(list1))       #////////////////////////////////////////////////////
print(list1)                   #{1, 5, 20, 30}
print(max(list1))              #30


