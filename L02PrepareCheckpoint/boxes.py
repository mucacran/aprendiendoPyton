import math

x = int(input("Enter the number of items: "))
y = int(input("Enter the number of items per box: "))

print(f"For {x} items, packing {y} items in each box, you will need {math.ceil(x/y)} boxes.")