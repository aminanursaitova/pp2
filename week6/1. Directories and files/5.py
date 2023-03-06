a = [1, 2, 4, 8, 16]
f = open('abc.txt', "w")
for i in a:
    f.write("%s\n" % i)
f.close()

f = open('abc.txt')
print(f.read())
