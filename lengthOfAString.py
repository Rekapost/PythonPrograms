s="welcome"
"""
print(len(s))
"""
"""
count=0
for i in s:
    count=count+1   # SINCE COUNTING THE NUMBER OF CHARACTERS
print(count)
"""
"""
s="welcome"
count=0
while s[count:]:     # slicing technique , from count 0 to last
    count=count+1
print(count)
"""
#join and count method
s="welcome"
random_s="x"
print(random_s.join(s))    #wxexlxcxoxmxe   #///////////////////////////
print(random_s.join(s).count(random_s))    #6   ///////////////////////////
print(random_s.join(s).count(random_s)+1)  #7    ///////////////////////////////


