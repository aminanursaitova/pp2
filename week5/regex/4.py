import re
a = input("enter your string: ")
if re.search("^[A-Z]{1}[a-z]+$", a):
    print("good")
else:
    print("no good")