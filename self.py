class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print("hello" +self.name)
  def __init__ (self, name):
    self.name=name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
# p1.greet()