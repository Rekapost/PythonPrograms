#Approach 1
x=10
y=20
print("enter x numeber", x)
print("enter y number", y)
x,y=y,x
print("the first number after swapping", x)
print("the second number after swapping", y)
#Approach 2
num1=input("enter the first no:")
num2=input("enter the second no:")
print("the first number before swapping ", num1)
print("the second number before swapping", num2)
temp=num1
num1=num2
num2=temp
print(" the first number after swapping", num1)
print("the second number after swapping", num2)