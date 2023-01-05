list=[1,6,3,4,9]

#METHOD 1
#find the element 3 from the list
ele=3
flag=0       # note ths flag
n=len(list)
for i in list:      # note this range list
    if (i==ele):
        print("element is" ,i)
        flag=1
        break    # it comes out from the if and loop
if (flag==0):  # if the searching element is not there in the list 
    print("element not found")

"""
# METHOD  2
list=[1,3,6,9]
ele=3
if (ele==3):
    print("ele found")
else:
    print("ele not found")
"""