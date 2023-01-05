list=input("enter string: ")
print(list)
revstring=list[::-1]
if (revstring==list):
    print(list, "is palindrome")
else:
    print(list,"not a palindrome")

