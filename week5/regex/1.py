import re
a = input("enter your string: ")
if re.search(".*ab*", a):
    print("good")
else:
    print("no good")