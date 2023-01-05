#clone or copy a list
#list=[1,2,3,4]
"""
#simple Reka  method
list1=list
print(list1)
"""
"""
#simple method
list=[1,2,3,4]
list1=list[::]
print(list1)
"""
"""
#extend method
list=[1,2,3,4]
list1=[]
list1.extend(list)
print(list1)
"""
"""
#copy method
list=[1,2,3,4]
list1=list.copy()
print(list1)
"""
"""
#list method
list1=[1,2,3,4]
list2=list(list1)
print(list2)
"""
#using List comprehension
list=[1,2,3,4]
copy=[i for i in list]    # /////////////////////////////////////////
print(copy)

