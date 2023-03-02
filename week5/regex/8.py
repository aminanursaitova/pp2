import re
a = input("enter your string: ")
print(re.split("[A-Z]", a))
print(re.findall('[A-Z][^A-Z]*', a))