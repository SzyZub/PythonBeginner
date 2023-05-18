hrs = input("Enter Hours:")
h = float(hrs)
payr = input("Enter Pay Rate:")
g = float(payr)
if h <= 40:
    print(h * g)
else:
    print(40.0 * g + (h - 40.0) * (1.5 * g))