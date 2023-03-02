A = int(input("Enter your a: "))
b = int(input("Enter your b: "))

class MyNumbers:
  def __iter__(self):
    self.a = A
    return self

  def __next__(self):
    if self.a <= b:
      x = self.a
      self.a += 1
      return x*x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)