import re
a = input("enter your string: ")
print('_'.join(
    re.sub('([A-Z][a-z]+)', r' \1',
    re.sub('([A-Z]+)', r' \1',
    a.replace('-', ' '))).split()).lower())