#s="i am at http://www.dash.com"
s="i am a blogger at http://www.blogger.com & http://www.dishyum.com"
import re   # (regular expression)
#http://urlregex.com/
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',s)
print(url)