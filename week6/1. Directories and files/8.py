import os
print('Exist:', os.access("demofile.txt", os.F_OK))
os.remove("demofile.txt")