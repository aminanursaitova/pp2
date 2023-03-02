import re
a = input("enter your string: ")
if re.search("^[a-z]+_[a-z]+$", a):
    print("good")
else:
    print("no good")