s="welcome@ Reka $to %Diney ^!world||{{>>"
#s="welcome to python programming"
import re
RegularExpression=re.compile('[@_!#$%^&*(){}|:"<>?]')
if(RegularExpression.search(s)==None):
    print("no special character")
else:
    print("strings contains special character")

