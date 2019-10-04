# Calculate the area and circumference of a circle
# 1. Prompt for the radius
# 2. Apply formualae
# 3. Print results

import math

radius_str = input("Input radius: ")

radius_float = float(radius_str)

circumference = 2 * math.pi * radius_float
area = math.pi * (radius_float ** 2)

print("When radius is", radius_float, "circumference is", circumference, "and area is", area)

