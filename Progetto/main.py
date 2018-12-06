from partArray import *

min = int(input("Inserire min: \n"))
max = int(input("Inserire max: \n"))
b = int(input("Inserire b: \n"))

if not b > 6:
    print("b non è maggiore di 6")
elif not ((max - min) % b) == 0:
    print("max-min non è multiplo di b")
else:
    v = Structure(min, max, b)
    print("Array:", v.print())
