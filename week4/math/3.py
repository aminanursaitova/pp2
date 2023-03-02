import math
from e1 import dtr
s = int(input())
l = int(input())
a = (((l / math.cos(dtr(180 / s))) / 2)** 2 - (l/2)**2)**0.5
A = s * l * a / 2
print(math.ceil(A))