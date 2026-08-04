x = "awesome"

def myfunc():
  x = "easy"
  print("Python is " + x)

  global y
  y = "this is global variable"

myfunc()

print("python is "+ x)
print(y)
