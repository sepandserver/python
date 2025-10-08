class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myplus(self,x):
    return(x + self.age)

  def mymines(self,x):
    return(self.age - x)


p1 = Person("John", 36)
 

print(f"My Name is {p1.name} I am {p1.myplus(4)} year old")
print(f"My Name is {p1.name} I am {p1.mymines(3)} year old")
