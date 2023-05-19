def computepay(h, r):
    if h <= 40:
        return(h * r)
    else:
        return((h - 40)*1.5*r + 40*r)
        

hrs = input("Enter Hours:")
hf = float(hrs)
rate = input("Enter Rate Per Hour:")
rf = float(rate)
p = computepay(hf, rf)
print("Pay", p)