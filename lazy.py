n = int(input("how many files do you need?"))
for i in range(1, n + 1):
   open(str(i) + ".py", "w")