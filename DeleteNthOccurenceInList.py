#Delete the nth Occurence of the word from the week
#ie geek word should appear only once, when it occurs second time delete it
#occurence no should be deleted (n)
"""
list=["geeks","reka","geeks"]
word = "geeks"
count=0
n=2      #(appearance of geeks at 2 nd time)
for i in range(0,len(list)):
    if (list[i]==word):
        count=count+1
        if(count==n):
            del list[i]
print(list)
"""
list=["geeks","reka","Raja","geeks","geeks","geeks"]
n=3        # appearance of geeks at 3rd time
word="geeks"
count=0
for i in range(0,len(list)-1):     # note this range -1
    if (list[i]==word):
        count=count+1
        if (count==n):
            del list[i]
print(list)

#for i in range(0,len(list)):
#IndexError: list index out of range
