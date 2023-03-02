import re
a = input("enter your string: ")
print(''.join(x.capitalize() or '_' for x in a.split('_')))