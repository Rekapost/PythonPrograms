# maximum and minimum of an array
#arr[]={90,30,15,12,50]}
#max=90, min=12
"""
#Approach 1  Reka model
arr=[90,30,15,12,50]
print(max(arr))   #90
print(min(arr))   #12
"""
"""
#Appraoch model by comparing within each index value
#maximum of array
arr=[15,30,90,12,50]
max=arr[0]   # first assume index 0 value is max
n=len(arr)   # get the length of the array
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print("maximum of the array:",max)
"""
"""
#minimum of array
arr=[15,30,90,12,50]
min=arr[0]   # first assume index 0 value is max
n=len(arr)   # get the length of the array
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print("minimum of the array:",min)
"""
#sort method
list=[30,20,90,80,1,5]
list.sort()
print(list)
print(list[0])
print(list[-1])






