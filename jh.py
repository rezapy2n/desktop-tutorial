import math
v = float(input("V :"))
t= float(input("T :"))
wind_chill = 13.12 + (0.6215 * t) - ((11.37 * (v ** 0.16))) + 0.3965 * t*(v ** 0.16)
print (wind_chill  )
