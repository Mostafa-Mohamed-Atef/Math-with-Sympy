import math

x, base = map(int,list(input("Enter x,base: \n").strip().split(",")))
print(math.log(x,base))