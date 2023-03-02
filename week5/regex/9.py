import re
a = input("enter your string: ")
print(re.sub(r"(\w)([A-Z])", r"\1 \2", a))