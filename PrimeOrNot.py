#natural numbers >1
#prime number has only factors 1 and the number itself  ,prime has 2 factors
# 19 ===>  19*1=19, 1*19=19   so 1 and 19   so 19 is prime number
#28  ====>  7*4=28, 4*7=28, 14*2=28, 1*28=28, 1,2,4,7,14,28  so 28  is not a prime number, have more than 2 factors
#num=input("enter a number:")  this will not work as num>1 str>int is invalid
num=5
count=0   #to store no of counts
if num>1:
    for i in range (1,num+1):
        if (num % i)== 0:    # if it gives reminder as 0
            count=count+1
    if count==2:
        print("it is prime number")
    else:
        print("it is not prime number")
#if num is 5 , u have to find factors from 1 to 5(1,2,3,4,5)
