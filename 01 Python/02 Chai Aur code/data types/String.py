myString = 'spam'  
name = "span's"
bytesObject = b'a\x01c'
#This is a bytes object (bytes). The prefix b means it's a sequence of bytes rather than a Unicode string. 
UnicodeString = u'sp\xc4m'
#This is a Unicode string (str in Python 3). 
# The prefix u is optional in Python 3 since all strings are Unicode by default.


print(myString)
print(name)
print(bytesObject)
print(bytesObject.decode('latin1')) 
print(UnicodeString)
