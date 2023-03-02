import re
a = input("enter your string: ")
print(re.sub("[ ,.]", ":", a))