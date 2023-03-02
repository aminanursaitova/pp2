import re
a = input("enter your string: ")
if re.search(".*ab{2,3}.*", a):
    print("good")
else:
    print("no good")