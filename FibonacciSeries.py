#series of numbers , in which each number is sum of 2 preceding numbers
#FIBONACCI 0F 10  =====> 0,1,1,2,3,5,8,13,21,34   (10 counts)
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,10):
# 2,3,4,5,6,7,8,9------>  i counts from 1 to 10
# 1 is declared as n2, in index 10, 10 wont include , so till 9
    sum=n1+n2  #(0+1)
    print(sum)   #1
    n1=n2
    n2=sum