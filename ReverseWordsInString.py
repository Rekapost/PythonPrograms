s="welcome to python programming"
splitwords=(s.split(" "))  #///////////////////////////////
print(splitwords) # ['welcome', 'to', 'python', 'programming']
splitwords=splitwords[-1::-1]   #////////////////////////////
print(splitwords)     #['programming', 'python', 'to', 'welcome']
print(" ".join(splitwords))  #\\\\\\\\\\\ # join words with empty strings   #programming python to welcome