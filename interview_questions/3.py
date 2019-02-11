# Write a program that prints a staircase of size n.
# When n = 4

   #
  ##
 ###
####

# Observe that its base and height are both equal to n, and the image is
# drawn using # symbols and spaces. The last line is not preceded by any
# spaces

def print_staircase(n):
  spaces = n-1
  for i in range(1, (n + 1)):
    h = "#" * i
    print((' ' * spaces) +  h)
    n+=1
    spaces -= 1
    
print_staircase(4)