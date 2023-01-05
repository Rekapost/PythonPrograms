#Sum of Elements in array
#arr[]={1,2,3,4,5,}
#1+2+3+4+5=15

arr=[1,2,3,4,5]
Sum=sum(arr)
print("sum of elements in array:",Sum)   #sum of elements in array: 15

#adding one more number to array
Sum=(sum(arr,10))      # {15,10}
print("sum of array after adding 10:",Sum)  #sum of array after adding 10: 25

#if u want to reduce 10 from sum
print("sum after reducing -10 in sum(arr):",sum(arr,-10))   #sum after reducing -10 in sum(arr): 5

#loop Method
arr=[1,2,3,4,5]
sum=0
for i in arr:
    sum=sum+i
print("loop method sum:",sum)

