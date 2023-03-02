n = int(input("Enter your N: "))

class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= n:
        x = self.a
        self.a += 1
        while x % 3 != 0 and x % 4 != 0:
            x = self.a
            self.a += 1
        return x
      
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x, end= ", ")