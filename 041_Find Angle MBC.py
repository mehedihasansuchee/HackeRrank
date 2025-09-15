#Find Angle MBC


import math

ab = int(input())
bc = int(input())

theta = math.degrees(math.atan2(ab, bc))

print(round(theta), '\u00B0', sep='')