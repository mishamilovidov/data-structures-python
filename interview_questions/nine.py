
# function that finds the square root of a number without build in function

# by Joshua Topacio
def sqrt(num):
  x = 0
  while True:
      if x ** 2 == num:
          break
      x += 1

  return x

print(sqrt(144))