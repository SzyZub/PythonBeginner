text = "X-DSPAM-Confidence:    0.8475"
Pos = text.find(" ")
Sli = text[Pos:]
z = Sli.strip()
print(float(z))