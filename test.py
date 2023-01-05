"""
#PRIME OR NOT
n=18
count=0
for i in range (1,n+1):
    if (n%i)==0:
        count=count+1
if (count==2):
    print("it is prime number")
else:
    print("it is not prime number")
"""
"""
#FACTORIAL NO
n=5
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("factorial of n:", factorial)
"""
"""
#fibonacci
n1=0
n2=1
n=10
print(n1)
print(n2)
for i in range(2,n):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
"""
"""
#Max and Min of array
#MAX
list=[10,20,90,70,60]
max=list[0]
n=len(list)
for i in range (1,n):
    if list[i]>max:
        max=list[i]
print(max)
"""
"""
#MIN OF LIST
list=[10,20,80,70,5]
n=len(list)
min=list[0]
for i in range (1,n):
    if list[i]<min:
        min=list[i]
print(min)
"""
"""
#SUM OF ELEMENTS IN AN ARRAY
list=[10,20,30,40]
a=sum(list)
print(a)  #100
a=sum(list,1)
print(a)  #101
a=sum(list,-1)
print(a) #99
"""
#SWAP NUMBERS
"""
a=10
b=20
print(a,b)
a,b=b,a
print(a,b)
"""
"""
x=10
y=20
print(x,y)
temp=x
x=y
y=temp
print(x,y)
"""


