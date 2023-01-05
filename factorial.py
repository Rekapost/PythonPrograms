#factorial of !5 means 5*4*3*2*1=120
#Approach 1
"""
factorial=1
num=5  # input no
if num<0:
     print("factorial does not exist")
elif num==0:
     print("factorial of num 0 is 1")
else:
     for i in range (1,num+1):
          factorial=factorial*i
     print("factorial of ",num, "is", factorial)   #120"""

#Approach 2
#recursion method ==> A FUNCTION WHICH IS CALLING THE SAME FUNCTION MULTIPLE TIMES
# 5!=5*4*3*2*1   descending order
"""
factorial=1
def factorial(n):
     if (n==0 or n==1):
          return 1
     else:
          return n* factorial(n-1)  # 5*4*3*2*1
num=5
print("the factorial of num is ",factorial(num))   #120"""

#ternary operator   single line program
factorial=1
def factorial(n):
     return 1 if (n==1 or n==0) else n*factorial(n-1)
num=5
print("the factorial of num is ",factorial(num))

