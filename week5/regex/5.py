import re
a = input("enter your string: ")
if re.search(".*a.*b$", a):
    print("good")
else:
    print("no good")