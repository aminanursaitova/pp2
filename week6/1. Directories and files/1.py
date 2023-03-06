import os
p = 'C:\Users\amina\Documents'
print("dirs: ", end="")
print([ name for name in os.listdir(p) if os.p.isdir(os.p.join(p, name)) ])
print("\nfiles: ", end="")
print([ name for name in os.listdir(p) if not os.p.isdir(os.p.join(p, name)) ])
print("\ndirs and files : ", end="")
print([ name for name in os.listdir(p)])