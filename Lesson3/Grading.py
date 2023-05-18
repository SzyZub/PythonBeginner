score = input("Enter Score: ")
scr = float(score)

if scr > 1 or scr < 0:
    print("Wrong number")
elif scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
else: 
    print("F")