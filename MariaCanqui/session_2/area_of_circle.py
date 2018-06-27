#return area of circle
import math
def area_of_circle(radio):
    if radio > 10: return str(math.pi * (radio ** 2))
    else: return "minor than 10"

print("radio 11:", area_of_circle(11))
print("radio 7:", area_of_circle(7))